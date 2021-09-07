from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
import pandas as pd
from icecream import ic
from time import sleep
from bs4 import BeautifulSoup


def main():
	driver = webdriver.Firefox(executable_path='bin/geckodriver.exe')


	driver.get("https://www.office.com/")
	driver.find_element_by_id('mectrl_headerPicture').click()
	sleep(1)
	email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "loginfmt")))

	email.send_keys('sciss@na.edu')


	driver.find_element_by_id('idSIButton9').click()
	sleep(2)

	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "i0118"))).click()
	# pwd = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "i0118")))
	pwd = driver.find_element_by_id('i0118')
	pwd.send_keys('Lollipop270915')
	sleep(2)

	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

	# driver.find_element_by_id('idSIButton9').click()
	# sleep(2)
	# driver.find_element_by_id('idSIButton9').click()


	sleep(1.5)

	driver.get('https://www.office.com/apps?auth=2&home=1')


	driver.get('https://account.activedirectory.windowsazure.com/applications/signin/120f4192-cada-45eb-9de5-e351fda20d41?tenantId=4001e375-31b4-4f03-b7d2-cb95ac6f5ff7')


	student = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.tabs:nth-child(3) > a:nth-child(1)")))
	

	driver.get('https://portal.na.edu/ICS/Students/NAU_Academic_Calendar.jnz')

	sleep(3)
	calender = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fc-body")))

	with open('Calendar_dump.txt', 'a') as file:
		file.write(calender.get_attribute('innerHTML'))

	# for i in range(1, len(rows)+1):

 #   		name =driver.find_elements_by_xpath(f'//*[@class="fc-view fc-month-view fc-basic-view"]/table/tbody/tr[{i}]/td[2]')[0].text
 #   		link = driver.find_elements_by_xpath(f'//*[@class="fc-view fc-month-view fc-basic-view"]/tbody/tr[{i}]/td[2]/ul/li/span/a')[0].get_attribute('href')  
 #   		image = driver.find_elements_by_xpath(f'//*[@class="a-normal a-none-tripes a-spacing-none a-size-base a-span12 search-result-body-wrapper"]/tbody/tr[{i}]/td[1]/img')[0].get_attribute("src")
 #   		price = driver.find_elements_by_xpath(f'//*[@class="a-normal a-none-stripes a-spacing-none a-size-base a-span12 search-result-body-wrapper"]/tbody/tr[{i}]/td[3]')[0].text
 #   		prod_type = search_name

if __name__ == '__main__':
	main()