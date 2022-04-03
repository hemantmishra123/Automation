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
driver.get("https://www.gadgetheory.com/worldwide/paused-scenes/17")
#it si the programme for redirecting to the website 
flag=True

while(flag):
    driver.find_element_by_class_name("nextpostlink").click()
    #time limit ->2 second every time for opening new postlink
    time.sleep(2)