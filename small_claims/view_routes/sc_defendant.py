#
# """
# idea: person facing small claims case inputs their name or case number and
# the app uses selenium / phantomJS to go scrape the court docket info (judge,
# defendant, upcoming court dates, etc.) then asks questions based on case type,
# i.e. "Did the accident happen in Hillsborough County?" "Were you driving the
# car?" "Was an accident report filed?"
# Then the system puts out a report on the past five years of data for that judge:
# do cases typically settle in mediation? What happens if they go to trial? Do I do
# better with a lawyer vs. without?
# """
#
# from django.http import HttpResponse
# from django.template import loader
# from django.shortcuts import render, get_object_or_404
# from django.http import Http404
# from small_claims.form_folder.small_claim import *
# from io import StringIO, BytesIO
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# import pickle
# import os
# import urllib2
# import re
# from bs4 import BeautifulSoup
# import urllib
# #Gets to the criminal and traffic search pages:
# 	##Key:	ID=600 	:	Criminal
# 	##		ID=200	:	Probate
# 	##		ID=300	:	All case types
# 	##		ID=400	:	Civil & Family
# #Using PhantomJS because holy shit, chromedriver doesn't work at all
# driver = webdriver.PhantomJS('/Users/samharden/Downloads/phantomjs-2.1.1-macosx 2/bin/phantomjs')
#
# def get_case_info(county, party_name, case_number):
#     try:
#         driver.get('http://pubrec10.hillsclerk.com/Unsecured/default.aspx')
#         driver.execute_script("javascript:LaunchSearch('Search.aspx?ID=900', false, false, sbxControlID1)")
#         #Select the date filed option:
#         driver.implicitly_wait(10)
#         date_filed_element = driver.find_element_by_id("DateFiled")
#         date_filed_element.click()
#
#         #Need to Put in a for or a try loop
#
#         ###
#         closed_open_element = driver.find_element_by_id("ClosedOption")
#         closed_open_element.click()
#         ###
#         #select the On or After box and enter a date:
#         on_or_after_element = driver.find_element_by_id("DateFiledOnAfter")
#         on_or_after_element.send_keys(start_date_to_send)
#         #select the On or Before box and enter a date:
#         on_or_before_element = driver.find_element_by_id("DateFiledOnBefore")
#         on_or_before_element.send_keys(end_date_to_send)
#
#         ##Need to select case type:
#
#         case_type_element = Select(driver.find_element_by_name("CaseTypes"))
#         case_type_element.select_by_visible_text("Misdemeanor")
#         ##
#
#         search_submit = driver.find_element_by_id("SearchSubmit")
#         search_submit.click()
#         page = driver.page_source
#
#
#         soup = BeautifulSoup(page, 'html.parser')
#         case_text = soup.prettify()
#         tags = soup('a')
#         # print case_text
#         list1=list()
#         for tag in tags:
#           x = tag.get('href', None)
#           list1.append(x)
#
#         print "Scraping Misdemeanor Dockets for %s to %s" % (start_date_to_send, end_date_to_send)
#
#         # for link in list1:
#         # link = list1[6]
#         # print link
#         for link in list1[8:]:
#           driver.get("http://pubrec10.hillsclerk.com/Unsecured/"+link.rstrip())
#           #print driver.page_source
#           source = driver.page_source
#           def save_case_text(obj, filename):
#             with open(filename, 'w') as output:
#               pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
#           os.chdir('/home/sam/mycourtcase/Hillsborough/2016/Mar')
#
#           save_case_text(source, 'FL-HILL-2016MA'+str(link[23:])+'.html')
#           print "Saving case FL-HILL-2016MA",str(link[23:])
#           driver.back()
#
#         driver.back()
#
#         driver.implicitly_wait(3)
#         date_filed_element = driver.find_element_by_id("DateFiled")
#         date_filed_element.click()
#
#         #Need to Put in a for or a try loop###
#
#         ###
#         closed_open_element = driver.find_element_by_id("ClosedOption")
#         closed_open_element.click()
#         ###
#
#         #select the On or After box and enter a date:
#         on_or_after_element = driver.find_element_by_id("DateFiledOnAfter")
#         on_or_after_element.send_keys(start_date_to_send)
#         #select the On or Before box and enter a date:
#         on_or_before_element = driver.find_element_by_id("DateFiledOnBefore")
#         on_or_before_element.send_keys(end_date_to_send)
#
#         ##Need to select case type:
#
#         case_type_element = Select(driver.find_element_by_name("CaseTypes"))
#         case_type_element.select_by_visible_text("Traffic Criminal")
#         ##
#
#         search_submit = driver.find_element_by_id("SearchSubmit")
#         search_submit.click()
#         page = driver.page_source
#
#
#         soup = BeautifulSoup(page, 'html.parser')
#         case_text = soup.prettify()
#         tags = soup('a')
#         # print case_text
#         list1=list()
#         for tag in tags:
#           x = tag.get('href', None)
#           list1.append(x)
#         # case_type_element = Select(driver.find_element_by_id("dnn_ctr484_Search_drpCaseType"))
#         # case_type_element.select_by_visible_text("Misdemeanor")
#         print "Scraping Traffic Dockets for %s to %s" % (start_date_to_send, end_date_to_send)
#
#         # for link in list1:
#         # link = list1[6]
#         # print link
#         for link in list1[8:]:
#           driver.get("http://pubrec10.hillsclerk.com/Unsecured/"+link.rstrip())
#           #print driver.page_source
#           source = driver.page_source
#           def save_case_text(obj, filename):
#             with open(filename, 'w') as output:
#               pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
#           os.chdir('/home/sam/mycourtcase/Hillsborough/2016/Mar')
#
#           save_case_text(source, 'FL-HILL-2016MA'+str(link[23:])+'.html')
#           print "Saving case FL-HILL-2016MA",str(link[23:])
#           driver.back()
#
#         driver.quit()
#         print "Done Scraping Dockets for %s to %s" % (start_date_to_send, end_date_to_send)
#     except Exception as f:
#         print str(f)
#
# elif what_county == "P":
#     try:
#         driver.get('https://ccmspa.pinellascounty.org/PublicAccess/default.aspx')
#         driver.execute_script("javascript:LaunchSearch('Search.aspx?ID=100', false, false, sbxControlID2)")
#         #Select the date filed option:
#         driver.implicitly_wait(3)
#         date_filed_element = driver.find_element_by_id("DateFiled")
#         date_filed_element.click()
#
#         closed_element = driver.find_element_by_id("ClosedOption")
#         closed_element.click()
#
#         #select the On or After box and enter a date:
#         on_or_after_element = driver.find_element_by_id("DateFiledOnAfter")
#         on_or_after_element.send_keys(start_date_to_send)
#         #select the On or Before box and enter a date:
#         on_or_before_element = driver.find_element_by_id("DateFiledOnBefore")
#         on_or_before_element.send_keys(end_date_to_send)
#
#         ##Need to select case type:
#
#         case_type_element = Select(driver.find_element_by_name("CaseTypes"))
#         case_type_element.select_by_visible_text("COUNTY CRIMINAL CASES")
#         ##
#
#         search_submit = driver.find_element_by_id("SearchSubmit")
#         search_submit.click()
#         page = driver.page_source
#
#
#         soup = BeautifulSoup(page, 'html.parser')
#         case_text = soup.prettify()
#         tags = soup('a')
#         # print case_text
#         list1=list()
#         for tag in tags:
#           x = tag.get('href', None)
#           list1.append(x)
#
#         print "Scraping Misdemeanor Dockets for %s to %s." % (start_date_to_send, end_date_to_send)
#         print "Number of files = %r" % (len(list1[8:]))
#
#         # for link in list1:
#         # link = list1[6]
#         # print link
#         for link in list1[8:]:
#           driver.get("https://ccmspa.pinellascounty.org/PublicAccess/"+link.rstrip())
#           #print driver.page_source
#           source = driver.page_source
#           def save_case_text(obj, filename):
#             with open(filename, 'w') as output:
#               pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
#           os.chdir('/home/sam/mycourtcase/Pinellas/2016/May')
#
#           save_case_text(source, 'FL-PINE-2016MY'+str(link[23:])+'.html')
#           print "Saving Case Number FL-PINE-2016MY", str(link[23:])
#           driver.back()
#
#         driver.quit()
#         print "Done scraping dockets from %s to %s." % (start_date_to_send, end_date_to_send)
#     except Exception as g:
#         print str(g)
#
# elif what_county == "M":
#     case_type_input = raw_input("""What case type? \n
#     M = Misdemeanor \n
#     T = Traffic \n
#     F = Felony \n
#     ...> """)
#     if case_type_input == "M":
#         case_type_num = "35"
#     elif case_type_input == "T":
#         case_type_num = "18"
#
#     # from itertools import count
#     # case_filename = ("FL-MANA-2015DE%04i.html" % i for i in count(1))
#
#
#     try:
#         driver.get('http://www.manateeclerk.org/PublicRecords/CourtRecordsSearch/tabid/57/st/4/Default.aspx')
#
#         case_type_element = Select(driver.find_element_by_name("dnn$ctr484$Search$drpCaseType"))
#         case_type_element.select_by_value(case_type_num)
#
#         #Select the date filed option:
#         driver.implicitly_wait(3)
#
#         #select the On or After box and enter a date:
#         on_or_after_element = driver.find_element_by_id("dnn_ctr484_Search_txtFrom_dateInput")
#         on_or_after_element.send_keys(start_date_to_send)
#         driver.implicitly_wait(3)
#         #select the On or Before box and enter a date:
#         on_or_before_element = driver.find_element_by_id("dnn_ctr484_Search_txtTo_dateInput")
#         on_or_before_element.send_keys(end_date_to_send)
#         driver.implicitly_wait(3)
#
#         ##Need to select case type:
#
#         search_submit = driver.find_element_by_id("dnn_ctr484_Search_cmdSearch")
#         search_submit.click()
#         driver.implicitly_wait(3)
#
#         #find the nex page link arrow:
#         next_page = driver.find_element_by_class_name('rgPageNext')
#
#         page = driver.page_source
#         soup = BeautifulSoup(page, 'html.parser')
#         case_text = soup.prettify()
#         tags = soup('a')
#         #tags = driver.find_elements_by_partial_link_text('http://www.manateeclerk.org/PublicRecords/CourtRecordsSearch')
#         #need this to be class="caseLink"  - was 'a'
#         # print case_text
#         list1=list()
#         for tag in tags:
#           x = tag.get('href', None)
#           #x = driver.get(tag)
#           list1.append(x)
#         print list1
#         print "Scraping Dockets for %s to %s." % (start_date_to_send, end_date_to_send)
#
#         # for link in list1:
#         # link = list1[6]
#         # print link
#         end_list = len(list1)-6
#         #print end_list
#         #print list1
#         for link in list1[8:end_list]:
#           driver.get(link)
#           #print driver.page_source
#           source = driver.page_source
#           case_soup = BeautifulSoup(source, 'html.parser')
#           try:
#               case_no = case_soup.find('span', id="dnn_ctr484_Details_lblCaseNumber")
#           except:
#               case_no = "99999999999999999999999"
#           case_name = ''.join(map(str, case_no.contents))
#           print "Saving Case Number ", case_name[3:]
#           def save_case_text(obj, filename):
#             with open(filename, 'w') as output:
#               pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
#           os.chdir('/home/sam/mycourtcase/Manatee/test')
#
#           save_case_text(source, case_name[3:]+'.html')
#           driver.implicitly_wait(5)
#           #driver.back()
#         #print "Going to next page"
#         print "Done"
#
#     except Exception as e:
#         print str(e)
#
# else:
#     print "Didn't understand you."
