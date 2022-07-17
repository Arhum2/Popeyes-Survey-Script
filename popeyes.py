from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


PATH = 'C:\Program Files (x86)\chromedriver.exe' # Enter your Chrome Webdriver Path
browser = webdriver.Chrome(PATH)

browser.get("https://www.tellpopeyes.com/")

time.sleep(2)

# Navigating to form
next_btn = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/div[1]/input')
next_btn.click()

# Setting store number
store_num = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/p[5]/input')
store_num.click()
store_num.send_keys('11962')

# Setting date
date_month = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/p[7]/select[1]')
date_month.send_keys("1")
date_month.click()


date_day = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/p[7]/select[2]')
date_day.send_keys("1")
date_day.click()

# Setting time
hour = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/p[9]/select[1]')
hour.send_keys("1")
hour.click()

min = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/p[9]/select[2]')
min.send_keys("1")
min.click()

period = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/p[9]/select[3]')
period.send_keys("1")
period.send_keys(Keys.ARROW_DOWN)

# Setting amount
amount = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/p[11]/input')
amount.send_keys('10')

# Submitting form
submit = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/div[1]/input')
submit.click()

time.sleep(2)

next = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/div[3]/input')
next.click()

time.sleep(2)

dot = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/div/fieldset/div/div/div[1]/span/span")
dot.click()

time.sleep(1)

next_btn = browser.find_element(By.ID, 'NextButton')
next_btn.click()

time.sleep(2)

dot = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/fieldset/div/div/div[1]/span/span')
dot.click()

time.sleep(2)

# Reassign next_btn because it does not seem to work otherwise
next_btn = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/div[3]/input')
next_btn.click()



