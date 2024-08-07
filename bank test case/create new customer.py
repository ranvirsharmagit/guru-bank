from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://www.demo.guru99.com/V4/")

driver.find_element(By.XPATH,"//input[@name='uid']").send_keys("mngr584602")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("uzatEqU")
driver.find_element(By.NAME,"btnLogin").click()
driver.find_element(By.LINK_TEXT, "New Customer").click() #after that we have to close the popup add manually
time.sleep(5)
#alert = driver.switch_to.default_content()
#alert.accept()
#alert.dismiss()
driver.find_element(By.NAME, "name").send_keys("ranvir")
driver.find_element(By.XPATH, "//textarea[@name='addr']").send_keys("sdfkas, sfds")
driver.find_element(By.NAME, "city").send_keys("delhi")
driver.find_element(By.CSS_SELECTOR, "input[name='state']").send_keys("delhi")
datefield = driver.find_element(By.XPATH,"//input[@id='dob']").send_keys('30/08/1986')
#ActionChains(driver).move_to_element(datefield).click().send_keys('30081986').perform()
driver.find_element(By.NAME, "pinno").send_keys("110017")
time.sleep(5)