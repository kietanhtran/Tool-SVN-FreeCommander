from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Ie("D:\Downloads\IEDriverServer.exe")
driver.get("https://b2b-gateway.renesas.com/login/ssl")
driver.implicitly_wait(15) 
driver.find_element(By.NAME,'LOGIN_ID').send_keys('a5120009')
driver.find_element(By.CLASS_NAME,'btnCustom').click()
password=""
arr = ["SMX_BTN_0", "SMX_BTN_4", "SMX_BTN_8", "SMX_BTN_12", "SMX_BTN_13", "SMX_BTN_14", "SMX_BTN_15", "SMX_BTN_28"]
for i in arr:
    pass1 = driver.find_element(By.ID,i).get_attribute("alt")
    password += pass1
driver.find_element_by_name("PASSWORD").send_keys(password)
button = driver.find_element_by_class_name("btnCustom").click()
sleep(12)
driver.quit()