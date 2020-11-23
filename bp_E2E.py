from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/raymond.perry/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://rayperry-bpcalculator.azurewebsites.net/")
print(driver.title)

systolic = driver.find_element_by_name("systolic_value")
systolic.send_keys('100')

diastolic = driver.find_element_by_name("diastolic_value")
diastolic.send_keys('80')
diastolic.send_keys(Keys.RETURN)

time.sleep(5)

#driver.quit()







