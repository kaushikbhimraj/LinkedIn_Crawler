"""
Description:
	Program uses user's credential to log in to their LinkedIn profile. 
	Search creteria for the jobs can be changed at line 17 and 18. 
	User credentials shall be loaded using a JSON file. (Update link in line 28).
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import json

class ParseJobs:
	def __init__(self):
		self.path      = "chromedriver.exe"
		self.driver    = webdriver.Chrome(self.path)
		self.job_title = "software developer"
		self.location  = "Atlanta, Georgia, United States"

		self.driver.get("https://www.linkedin.com/home")


	def get_linkedin_jobs(self):
		self.driver.find_element_by_xpath("//a[contains(text(), 'Sign in')]").click()
		sleep(3)

		with open("C:/Users/kaush/Desktop/log.json") as loginFile:
			login = json.load(loginFile)
			loginFile.close()

		usr = login["username"]
		pwd = login["password"]

		self.driver.find_element_by_id("username").click()
		self.driver.find_element_by_id("username").send_keys(usr)

		self.driver.find_element_by_id("password").click()
		self.driver.find_element_by_id("password").send_keys(pwd)
		self.driver.find_element_by_id("password").send_keys(Keys.ENTER)
		sleep(3)

		# Get List of Jobs. 
		self.driver.find_element_by_xpath("/html/body/div[6]/header/div/nav/ul/li[3]/a").click()
		sleep(3)

		# Enter Job Title
		self.driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-keyword-id-')]").click()
		self.driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-keyword-id-')]").send_keys(self.job_title)

		# Enter Location
		self.driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-location-id-')]").click()
		self.driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-location-id-')]").send_keys(self.location)
		self.driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-location-id-')]").send_keys(Keys.ENTER)
		sleep(3)

		# Set Date Posted to 24 hours. 
		self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[3]/section/div/div/div/div[1]/div/div[2]/ul/li[4]/div/span/button").click()
		self.driver.find_element_by_xpath("//input[@name=\"Past 24 hours\"]").send_keys(Keys.SPACE)
		self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[3]/section/div/div/div/div[1]/div/div[2]/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]").click()

		url = self.driver.current_url
		self.driver.quit()

		return url