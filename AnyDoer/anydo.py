# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 18:19:26 2018

Any.Do start the day reviewing your Tasks and priorities

@author: Ruben Seoane
"""

#Importing libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Login
login_url ='https://desktop.any.do/tasks/all'
driver = webdriver.Chrome()
driver.get(login_url)
driver.maximize_window()
#wait = WebDriverWait(driver, 1)

# Use Google Secure Login Button
elem = driver.find_element_by_xpath('//*[@id="root"]/div/section/div/div[3]/section/div/div/section[1]/div/div/div/div[1]/button[2]').click()

# Enter email
elem = driver.find_element_by_id('identifierId')
elem.send_keys("your@email.com")
elem.send_keys(Keys.RETURN)


# Select password field and enter yours
elem = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
elem.click()
elem.send_keys("yourpassword")
elem.send_keys(Keys.RETURN)