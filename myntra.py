from selenium import webdriver
import os
#it is the header decleration for the programme
import webbrowser
import time
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome("C:\\Users\\Hemant\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.myntra.com")
driver.find_element_by_css_selector("span.desktop-userTitle").click()
driver.find_element_by_link_text("MEN").click()
time.sleep(5)
driver.find_element_by_link_text("WOMEN").click()

driver.find_element_by_link_text("Kid").click()
driver.find_element_by_css_selector("a.desktop-linkbutton").click()
driver.find_element_by_css_selector("input.form-control mobileNumberInput").send_keys("9758834349")