import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


chromeOptions = Options()
chromeOptions.headless = True
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH, options=chromeOptions)

driver.get("https://rayperry-qa-bpcalculator.azurewebsites.net")
print(driver.title)


class E2ETestBpCalc(unittest.TestCase):

    def test_invalidsys(self):
        systolic = driver.find_element_by_name("systolic_value")
        systolic.send_keys("a")
        diastolic = driver.find_element_by_name("diastolic_value")
        diastolic.send_keys("b")
        diastolic.send_keys(Keys.RETURN)
        main = driver.find_element_by_class_name("alert")
        print(main.text)
        self.assertEqual(main.text, "Please only enter numbers")

    def test_invalddias(self):
        systolic = driver.find_element_by_name("systolic_value")
        systolic.send_keys("100")
        diastolic = driver.find_element_by_name("diastolic_value")
        diastolic.send_keys("?")
        diastolic.send_keys(Keys.RETURN)
        main = driver.find_element_by_class_name("alert")
        print(main.text)
        self.assertEqual(main.text, "Please only enter numbers")

    def test_invalidchar(self):
        systolic = driver.find_element_by_name("systolic_value")
        systolic.send_keys("?")
        diastolic = driver.find_element_by_name("diastolic_value")
        diastolic.send_keys("-")
        diastolic.send_keys(Keys.RETURN)
        main = driver.find_element_by_class_name("alert")
        print(main.text)
        self.assertEqual(main.text, "Please only enter numbers")

    def test_invalidrangesys(self):
        systolic = driver.find_element_by_name("systolic_value")
        systolic.send_keys("8000")
        diastolic = driver.find_element_by_name("diastolic_value")
        diastolic.send_keys("80")
        diastolic.send_keys(Keys.RETURN)
        main = driver.find_element_by_class_name("alert")
        print(main.text)
        self.assertEqual(main.text, "Invalid Systolic Value, please re-enter value.")

    def test_invalidrangedias(self):
        systolic = driver.find_element_by_name("systolic_value")
        systolic.send_keys("100")
        diastolic = driver.find_element_by_name("diastolic_value")
        diastolic.send_keys("8000")
        diastolic.send_keys(Keys.RETURN)
        main = driver.find_element_by_class_name("alert")
        print(main.text)
        self.assertEqual(main.text, "Invalid Diastolic Value, please re-enter value.")

    def test_null(self):
        click = driver.find_element_by_id("calc_btn")
        click.click()
        main = driver.find_element_by_class_name("alert")
        print(main.text)
        self.assertEqual(main.text, "Please only enter numbers")

    def test_lowblood(self):
        systolic = driver.find_element_by_name("systolic_value")
        systolic.send_keys("85")
        diastolic = driver.find_element_by_name("diastolic_value")
        diastolic.send_keys("55")
        diastolic.send_keys(Keys.RETURN)
        main = driver.find_element_by_class_name("alert")
        print(main.text)
        self.assertEqual(main.text, "Low blood pressure")

    def test_idealblood(self):
        systolic = driver.find_element_by_name("systolic_value")
        systolic.send_keys("100")
        diastolic = driver.find_element_by_name("diastolic_value")
        diastolic.send_keys("70")
        diastolic.send_keys(Keys.RETURN)
        main = driver.find_element_by_class_name("alert")
        print(main.text)
        self.assertEqual(main.text, "Ideal blood pressure")

    def test_preblood(self):
        systolic = driver.find_element_by_name("systolic_value")
        systolic.send_keys("130")
        diastolic = driver.find_element_by_name("diastolic_value")
        diastolic.send_keys("55")
        diastolic.send_keys(Keys.RETURN)
        main = driver.find_element_by_class_name("alert")
        print(main.text)
        self.assertEqual(main.text, "Pre-high blood pressure")

    def test_highlood(self):
        systolic = driver.find_element_by_name("systolic_value")
        systolic.send_keys("150")
        diastolic = driver.find_element_by_name("diastolic_value")
        diastolic.send_keys("70")
        diastolic.send_keys(Keys.RETURN)
        main = driver.find_element_by_class_name("alert")
        print(main.text)
        self.assertEqual(main.text, "High blood pressure")

if __name__ == "__main__":
    import xmlrunner

    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="Tests/test-reports"))
