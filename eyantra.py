from selenium import webdriver 
import os
driver=webdriver.Chromedriver("C:\\Users\\Hemant\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("http://eyic.e-yantra.org/login")
email="hemantmishra575@gmail.com"
val1=driver.find_element_by_name(email)
print(val1.is_displayed())
val1.click()
