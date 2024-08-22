import time
import os
import datetime
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
chrome_options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

display = Display(visible=0, size=(1600, 1200))
display.start()
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',options=options)

start_log_file_path = "PATH_OF_START_LOG" #this log write one thing on start the program writing program's started date 
with open(start_log_file_path, "a") as start_log:
  start_log.write(f"auto_subscribtion.py is started on {date_time} \n")
log_file_path = "PATH_OF_PROGRAM" #this log wrtiing trys of subscribtion (line 48)
open(log_file_path,'a').close()
num_calls = 0
start_time = datetime.datetime.now()

#If the page have member system you must log in firstly
driver.get("LINK_OF_LOGIN_PAGE")
username = driver.find_element(By.ID, 'ID_OF_USERNAME_OR_EMAIL_ELEMENT')
password = driver.find_element(By.ID, 'ID_OF_PASSWORD_ELEMENT')
username.send_keys("")
password.send_keys("")
driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').click() 
driver.get("LINK_OF_SUBSCRIBTION_BUTTONS_PAGE") #program will try the submit in this page

while True:
  driver.refresh()
  try:
    driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').click()
    is_button_present = True
    exit()
  except:
    is_button_present = False
  num_calls += 1
  date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  elapsed_time = datetime.datetime.now() - start_time
  with open(log_file_path, "a") as dosya:
      dosya.write(
          f"called {num_calls} times. Program has been running for {elapsed_time}. Date is {date_time}. Result = {is_button_present}.\n")
  time.sleep(30*60)


driver.quit()
display.stop()
