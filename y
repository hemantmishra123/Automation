from selenium import webdriver
import os
#it is the header decleration for the programme 
import webbrowser
import time
from selenium.webdriver.support.ui import Select
import pandas as pd
import numpy as np
#it is the plotting library for ploting the 
import matplotlib.pyplot as plt
driver=webdriver.Chrome("C:\\Users\\Hemant\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.ltfs.com/companies/lnt-investment-management/statutory-disclosures.html")
#it is the month 
driver.find_element_by_class_name("select2-selection_rendered").send_keys("Apr")
driver.find_element_by_xpath("//a[@title='Month']").send_keys("Apr")
time.sleep(10)
driver.find_element_by_class_name("mr-sec-nav-tab").click()
driver.quit()
driver.exit()
