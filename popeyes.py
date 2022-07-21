from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


PATH = 'C:\Program Files (x86)\chromedriver.exe' # Enter your Chrome Webdriver Path
browser = webdriver.Chrome(PATH)

browser.get("https://www.tellpopeyes.com/")

time.sleep(2)

# Navigating to form
next_btn = browser.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input')
next_btn.click()

# Setting store number
time.sleep(3)
store_num = browser.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[5]/div[3]/div/fieldset/div/div/table/tbody/tr[1]/td[2]/input')
store_num.click()
store_num.send_keys('11962')

# Setting date
date_month = browser.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[5]/div[3]/div/fieldset/div/div/table/tbody/tr[2]/td[2]/input')
date_month.click()
time.sleep(2)
days = browser.find_element(By.TAG_NAME, 'td')
days.click()

# Setting time
hour = browser.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[7]/div[3]/div/fieldset/fieldset/div/table/tbody/tr/td[3]/select')
hour.click()
hour.send_keys(Keys.ARROW_UP)
hour.send_keys(Keys.ARROW_UP)
hour.click()

min = browser.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[7]/div[3]/div/fieldset/fieldset/div/table/tbody/tr/td[6]/select')
min.click()
min.send_keys("0")

period = browser.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[7]/div[3]/div/fieldset/fieldset/div/table/tbody/tr/td[9]/select')
period.send_keys("1")
period.send_keys(Keys.ARROW_DOWN)
period.send_keys(Keys.ARROW_DOWN)
period.click()

# Setting amount
amount = browser.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[9]/div[3]/div/fieldset/div/div/table/tbody/tr/td[2]/input')
amount.send_keys('10')


time.sleep(10)
# Submitting form
submit = browser.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input[2]')
submit.click()



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



