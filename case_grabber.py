
import pandas as pd
import sqlalchemy as sa
import urllib.request
import datetime
from datetime import date, timedelta
import dateutil
from dateutil.parser import *
from dateutil.relativedelta import *
import smtplib
import os
from sqlalchemy import create_engine

today_date = str(date.today()-timedelta(1))
print today_date
year = today_date[:4]
print year
month = today_date[5:7]
day = today_date[8:10]
print month
print day

#hill_engine = sa.create_engine('sqlite:///hillsborough_filings.db')
hill_engine = sa.create_engine('postgres://ovoqaxnmmsxikt:b27443398f6d6ac17a24bd90fe94137be3beb9c1fb94ad467c66b57b84458192@ec2-23-21-204-166.compute-1.amazonaws.com:5432/d6lo6kd16njotm')

def create_db():

    civil_family_filings = urllib.request.urlopen(
                'https://publicrec.hillsclerk.com/DailyNewCaseFilings/CivilandFamilyLaw/CivilFiling_'
                +str(year)
                +str(month)
                +str(day)
                +'.csv'
                )
    df_family = pd.read_csv(civil_family_filings)

    df_family.to_sql('civil_family', hill_engine, if_exists='replace')


    criminal_filings = urllib.request.urlopen(
                'https://publicrec.hillsclerk.com/DailyNewCaseFilings/CriminalandTraffic/CriminalFiling_'
                +str(year)
                +str(month)
                +str(day)
                +'.csv'
                )
    df_family = pd.read_csv(criminal_filings)

    df_family.to_sql('criminal', hill_engine, if_exists='replace')

def find_and_email_cases():

  engine = create_engine('postgres://ovoqaxnmmsxikt:b27443398f6d6ac17a24bd90fe94137be3beb9c1fb94ad467c66b57b84458192@ec2-23-21-204-166.compute-1.amazonaws.com:5432/d6lo6kd16njotm')

  diss_w_children_text = 'SELECT * FROM civil_family WHERE "CaseTypeDescription" LIKE "Dissolution of Marriage with Children";'
  dwc = pd.read_sql_query(diss_w_children_text, engine)
  dwc.drop(['index', 'CaseCategory',], axis=1, inplace=True)
  html_dwc = dwc.to_html()

  diss_wo_children_text = 'SELECT * FROM civil_family WHERE "CaseTypeDescription" LIKE "Dissolution of Marriage";'
  dwoc = pd.read_sql_query(diss_wo_children_text, engine)
  dwoc.drop(['index', 'CaseCategory',], axis=1, inplace=True)
  html_dwoc = dwoc.to_html()

  dui_text = 'SELECT * FROM criminal WHERE "ChargeOffenseDescription" LIKE "%DRIVING UNDER THE INFLUENCE%" OR "ChargeOffenseDescription" LIKE "%DUI%";'
  dui = pd.read_sql_query(dui_text, engine)
  dui.drop(['index',
            'CaseCategory',
            'CaseTypeDescription',
            'ChargeNumber',
            'PartyType'], axis=1, inplace=True)

  html_dui = dui.to_html()

  try:

      from email.mime.multipart import MIMEMultipart
      from email.mime.text import MIMEText

      fromaddr = 'info@courtdatesearch.com'
      toaddrs  = 'samharden@gmail.com'
      msg = MIMEMultipart()
      msg['From'] = 'Hillsborough Case Filings'
      msg['To'] = 'samharden@gmail.com'
      msg['Subject'] = 'New Case Filings for %s / %s / %s' % (month, day, year)
      body = """

    <!DOCTYPE html>

    <center style="box-sizing: border-box;">
    				<h2 class="site-title" style="box-sizing: border-box; font-family:
            Montserrat, sans-serif; font-weight: 400; line-height: 1.2; color:
            #444; font-size: 1.777em; letter-spacing: -0.04em; margin: 1.333em 0 .5em;">
            Dissolution With Children </a></h2></div>
    </center>


    <p style="align: center; box-sizing: border-box;">
    <table style="height: auto; border-collapse: collapse; border-spacing: 0;
    box-sizing: border-box; color: #333; width: auto; overflow: auto; margin:
    1em auto;"> <tbody style="align: center; box-sizing: border-box;">

    %s

     </tbody></table> </p>

     <center style="box-sizing: border-box;">
     				<h2 class="site-title" style="box-sizing: border-box; font-family:
             Montserrat, sans-serif; font-weight: 400; line-height: 1.2; color:
             #444; font-size: 1.777em; letter-spacing: -0.04em; margin: 1.333em 0 .5em;">
             Dissolution Without Children </a></h2></div>
     </center>


    <p style="align: center; box-sizing: border-box;">
    <table style="height: auto; border-collapse: collapse; border-spacing: 0;
    box-sizing: border-box; color: #333; width: auto; overflow: auto; margin:
    1em auto;"> <tbody style="align: center; box-sizing: border-box;">

     %s

      </tbody></table> </p>

     <center style="box-sizing: border-box;">
     				<h2 class="site-title" style="box-sizing: border-box; font-family:
             Montserrat, sans-serif; font-weight: 400; line-height: 1.2; color:
             #444; font-size: 1.777em; letter-spacing: -0.04em; margin: 1.333em 0 .5em;">
             DUI</a></h2></div>
     </center>

    <p style="align: center; box-sizing: border-box;">
    <table style="height: auto; border-collapse: collapse; border-spacing: 0;
    box-sizing: border-box; color: #333; width: auto; overflow: auto; margin:
    1em auto;"> <tbody style="align: center; box-sizing: border-box;">

     %s

      </tbody></table> </p>

    </html>

      """ % (html_dwc, html_dwoc, html_dui)

      msg.attach(MIMEText(body, 'html'))
      username = 'info@courtdatesearch.com'
      password = '$$%iN8337269!#$'
      server = smtplib.SMTP('mail.courtdatesearch.com:26')
      server.starttls()
      server.login(username,password)
      email_text = msg.as_string()
      server.sendmail(fromaddr, toaddrs, email_text)
      server.close()
      print('Email sent!')

  except Exception as g:
      print(str(g))

if __name__ == "__main__":
    create_db()
    find_and_email_cases()
