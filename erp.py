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
#it is the programme file that i can enter inside my file 
driver=webdriver.Chrome("C:\\Users\\Hemant\\Downloads\\chromedriver_win32\\chromedriver.exe")
#ERP Login for browser.
driver.get("https://erp.aktu.ac.in/")
#it si the programme for redirecting to the website 
userid="1809510031"
userpass="engineer2018"
driver.find_element_by_name("txtUserId").send_keys(userid)
driver.find_element_by_id("txtPassword").send_keys(userpass)
driver.find_element_by_id("btnLogin").click()
time.sleep(10)
driver.quit()
driver.exit()