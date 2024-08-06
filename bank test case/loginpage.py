from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://www.demo.guru99.com/V4/")

driver.find_element(By.XPATH,"//input[@name='uid']").send_keys("mngr584602")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("uzatEqU")
driver.find_element(By.NAME,"btnLogin").click()
time.sleep(5)