from selenium import webdriver
import os
#it is the header decleration for the programme.
import webbrowser
from pymongo import MongoClient
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import numpy as np
#it is the plotting library for ploting the 
import matplotlib.pyplot as plt
driver=webdriver.Chrome("C:\\Users\\Hemant\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.ltfs.com/companies/lnt-investment-management/statutory-disclosures.html")
#it is the month 

#month=driver.find_element_by_xpath("//span[text()='Month']")
"//h1[text"
#driver.find_element_by_link_text("About Us").click()
#time.sleep(5)
# * $ ^
# first middle last
# first constant tag[attribute*="title"]
# last constant tag[attribut^="title"
# 
#driver.find_element_by_link_text("Home").click()
#time.sleep(5)
value=driver.find_element_by_link_text("Statutory Disclosures")
print(value.is_displayed())
#attr=driver.find_element_by_xpath("h1[text(),'Monthly Fund Portfolios']")
#print(attr.is_displayed())
#msg="Apr"
#driver.find_element_by_link_text("Month").send_keys(msg)
#var=driver.find_element_by_css_selector("span.select2-selection__rendered")
val1=driver.find_element_by_css_selector("span[id^='select2-'][id$='-container']")
print(val1.is_displayed())
val1.click()
act=ActionChains(driver)
act.send_keys(Keys.ARROW_DOWN).perform()
act.send_keys(Keys.ENTER).perform()
date=driver.find_element_by_xpath("//span[text()='2020-21']")
print(date.is_displayed())
date.click()
driver.execute_script("window.scrollTo(0,4)")

act.send_keys(Keys.ARROW_DOWN).perform()
act.send_keys(Keys.ENTER).perform()
act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.ENTER).perform()
#data=driver.find_element_by_xpath("//span[@title='Month']")
#print(data.is_displayed())
#usepass="Apr"
#data.send_keys("Apr")
#driver.find_element_by_xpath("//span[contains(@id,'select2-') and contains(@id,'-container')]").send_keys("Apr")
#print(var.is_displayed())
#driver.find_element_by_css_selector("")
#var.send_keys("Apr")
#driver.find_element_by_css_selector("span.select2-selection__rendered").send_keys("Apr")
#register=driver.find_element_by_class_name("mr-dbp-inb mr-rel")
#print(register.is_displayed())
#register.click()
#element=driver.find_element_by_xpath("//span[@title='Month']")
#print(element.is_displayed())
#element.click()
#month=Select(element)
#month.select_by_visible_text('Apr')
#ele=driver.find_element_by_xpath("//span[@title='Apr']")
#flag bit for the element exist inside my website for the data accessment for the particular function
#print(ele.is_displayed())
#ele.click()
time.sleep(20)
#driver.find_element_by_class_name("mr-sec-nav-tab").click()
driver.quit()
