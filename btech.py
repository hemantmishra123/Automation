from selenium import webdriver
import os
#it is the header decleration for the programme 
import webbrowser
import time
from selenium.webdriver.support.ui import Select
import pandas as pd
import numpy as np
#it is the plotting library for ploting the data
import matplotlib.pyplot as plt
driver=webdriver.Chrome("C:\\Users\\Hemant\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://abesit.in/library/question-paper-bank/")
#btech=driver.find_element_by_link_text("B Tech.")
driver.find_element_by_link_text("B Tech.").click()
#driver.find_element_by_xpath("//img[starts-with(@alt,'Icon of Sem.1.')]").click()
#print(btech.is_displayed())
#btech.click()
mca=driver.find_element_by_link_text("MCA")
mca.click()
driver.find_element_by_xpath("//img[starts-with(@alt,'Icon of Sem.1')]").click()
# it is the prototype function
# //img[]
time.sleep(10)
driver.exit()
