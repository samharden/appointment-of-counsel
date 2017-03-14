from django.db import models

# Create your models here.
import pandas as pd
from pandas import DataFrame
import sqlalchemy as sa

def search_all(first, last, county):
  hill_engine = sa.create_engine('sqlite:///crim/odyssey.db')
  #hill_engine = sa.create_engine('postgres://ovoqaxnmmsxikt:b27443398f6d6ac17a24bd90fe94137be3beb9c1fb94ad467c66b57b84458192@ec2-23-21-204-166.compute-1.amazonaws.com:5432/d6lo6kd16njotm')
  if county == "hill":
    date = ""
    appearance_type = ""
    if last and first:
      sql_text = 'SELECT * FROM hillsborough WHERE lastname_stripped LIKE "%' + last + '%" AND firstname_stripped LIKE "%' + first + '%" AND "Case Type" LIKE "CRIMINAL TRAFFIC";'
      df = pd.read_sql_query(sql_text, hill_engine)
      #df = pd.read_sql(sql_text, hill_engine)
      judge = df.get('Judicial Officer')
      date = df.get('Hearing Date/Time')
      appearance_type = df.get('Hearing Type')
    elif first:
      sql_text = 'SELECT * FROM hillsborough WHERE first_name LIKE "%' + first + '%";'
      df = pd.read_sql_query(sql_text, hill_engine)
      judge = df.get('Judicial Officer')
    elif last:
      sql_text = 'SELECT * FROM hillsborough WHERE lastname_stripped LIKE "%' + last + '%";'
      df = pd.read_sql_query(sql_text, hill_engine)
      judge = df.get('Judicial Officer')

    if len(df) == 0:
        judge = str('notsure')
    # judge = df.get('Judicial Officer')
    case_number = df.get('Case Number')
    print(case_number)
    print("Models says the Judge is", judge)
    print(county)
    return judge, case_number, date, appearance_type



  elif county == "pine":
    if last:
      sql_text = 'SELECT * FROM pinellas WHERE lastname_stripped LIKE "%' + last + '%";'
      df = pd.read_sql_query(sql_text, pine_engine)
      #print 'len(df) = ', len(df)
    elif first:
      #print 'Only first name entered, searching for first name= ', first
      sql_text = 'SELECT * FROM pinellas WHERE firstname_stripped LIKE "%' + first + '%";'
      df = pd.read_sql_query(sql_text, pine_engine)

    if len(df) > 1:
      if first:
        df = df.loc[df['firstname_stripped'].str.contains(first, na=False)]
    if len(df) == 0:
        judge = "notsure"
    #   #drop extraneous columns from result display
    # df.drop(['last_name', 'firstname_stripped',
    #           'first_name', 'lastname_stripped',
    #           'index', 'Connection Type',
    #           'Case Type', 'Hearing Type', 'Judicial Officer'], axis=1, inplace=True)
    #   # DataFrame.add(df, axis=1, fill_value=None)
    #   #rename column headers:
    # df.columns = ['Party Name:', 'Courtroom Location:',
    #               'Date & Time:', 'Case Number:']

    judge = df.get('Judicial Officer')
    print("Judge is", judge)
  #return judge
