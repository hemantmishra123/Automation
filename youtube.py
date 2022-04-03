from selenium import webdriver
import os
#it is the header decleration for the programme
import webbrowser
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome("C:\\Users\\Hemant\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.youtube.com/")
ele=driver.find_element_by_name("search_query")
print(ele.is_displayed())
msg=input("what do you want to search ")
print("do you want ")
# automate testing in future 
ele.send_keys(msg)
act=ActionChains(driver)
driver.maximize_window()
#act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.ENTER).perform()
act.send_keys(Keys.ARROW_RIGHT).perform()
act.send_keys(Keys.ENTER).perform()
act.send_keys(Key.TAB).perform()

