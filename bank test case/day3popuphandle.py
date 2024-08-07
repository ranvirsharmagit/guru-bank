from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://www.demo.guru99.com/V4/")
#tc1 - use valid id valid password and then logout
driver.find_element(By.XPATH,"//input[@name='uid']").send_keys("mngr584602")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("uzatEqU")
driver.find_element(By.NAME,"btnLogin").click()
driver.find_element(By.LINK_TEXT,"Log out").click()
time.sleep(3)
alert = driver.switch_to.alert   #its by javascript by switch to alert mode
alerttext = alert.text    #this to grab the text in alert box
print(alerttext)
assert "Succesfully Logged Out" in alerttext
alert.accept()  #to click OK button in alert
#alert.dismiss() #to click cancle if available
time.sleep(3)
#tc2 - use valid password but invalid id
driver.find_element(By.XPATH,"//input[@name='uid']").send_keys("mngr58460")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("uzatEqU")
driver.find_element(By.NAME,"btnLogin").click()
time.sleep(3)
alert = driver.switch_to.alert   #its by javascript by switch to alert mode
alerttext = alert.text    #this to grab the text in alert box
print(alerttext)
alert.accept()
#tc3 - use invalid password but ivalid id
driver.find_element(By.XPATH,"//input[@name='uid']").send_keys("mngr584602")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("uzatEq")
driver.find_element(By.NAME,"btnLogin").click()
time.sleep(3)
alert = driver.switch_to.alert   #its by javascript by switch to alert mode
alerttext = alert.text    #this to grab the text in alert box
print(alerttext)
alert.accept()
#tc4 - use invalid password and invalid id
driver.find_element(By.XPATH,"//input[@name='uid']").send_keys("mngr58460")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("uzatEU")
driver.find_element(By.NAME,"btnLogin").click()
time.sleep(3)
alert = driver.switch_to.alert   #its by javascript by switch to alert mode
alerttext = alert.text    #this to grab the text in alert box
print(alerttext)
alert.accept()