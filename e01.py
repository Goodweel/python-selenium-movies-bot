from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.get('http://www.topnow.se')
#sleep(5)
browser.implicitly_wait(10) #wait for all elements in the code
search_field = browser.find_element_by_id('search')
search_field.click()

print("Exiting ...")
browser.quit()
