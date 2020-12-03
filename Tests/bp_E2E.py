from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/raymond.perry/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://rayperry-qa-bpcalculator.azurewebsites.net")
print(driver.title)

systolic = driver.find_element_by_name("systolic_value")
systolic.send_keys("85")

diastolic = driver.find_element_by_name("diastolic_value")
diastolic.send_keys("50")
diastolic.send_keys(Keys.RETURN)

main = driver.find_element_by_class_name("alert")
print(main.text)

time.sleep(3)

systolic = driver.find_element_by_name("systolic_value")
systolic.send_keys("100")

diastolic = driver.find_element_by_name("diastolic_value")
diastolic.send_keys("70")
diastolic.send_keys(Keys.RETURN)

main = driver.find_element_by_class_name("alert")
print(main.text)

time.sleep(3)

systolic = driver.find_element_by_name("systolic_value")
systolic.send_keys("130")

diastolic = driver.find_element_by_name("diastolic_value")
diastolic.send_keys("55")
diastolic.send_keys(Keys.RETURN)

main = driver.find_element_by_class_name("alert")
print(main.text)

time.sleep(3)

systolic = driver.find_element_by_name("systolic_value")
systolic.send_keys("150")

diastolic = driver.find_element_by_name("diastolic_value")
diastolic.send_keys("70")
diastolic.send_keys(Keys.RETURN)

main = driver.find_element_by_class_name("alert")
print(main.text)

time.sleep(3)


systolic = driver.find_element_by_name("systolic_value")
systolic.send_keys("8000")

diastolic = driver.find_element_by_name("diastolic_value")
diastolic.send_keys("80")
diastolic.send_keys(Keys.RETURN)

main = driver.find_element_by_class_name("alert")
print(main.text)

time.sleep(3)


systolic = driver.find_element_by_name("systolic_value")
systolic.send_keys("100")

diastolic = driver.find_element_by_name("diastolic_value")
diastolic.send_keys("8000")
diastolic.send_keys(Keys.RETURN)

main = driver.find_element_by_class_name("alert")
print(main.text)

time.sleep(3)


# driver.quit()
