"""
Description:
	Program uses beautiful soup, to parse all jobs listed on the LinkedIn job search page. 
	These job details are loaded into a relationanl database whenever the program is run. 
"""

from bs4 import BeautifulSoup
from main import ParseJobs
import requests

import psycopg2

class BS4Parse:

	def JobDetails(self):

		page_url = ParseJobs().get_linkedin_jobs()
		jobs_page = requests.get(page_url).text
		jobs_parse = BeautifulSoup(jobs_page, "html.parser")

		li_tags = jobs_parse.find_all("li", class_="result-card job-result-card result-card--with-hover-state")

		for i in range(len(li_tags)):
			atag    = li_tags[i].find("a", class_="result-card__full-card-link")
			h3tag   = li_tags[i].find("h3", class_="result-card__title job-result-card__title")
			h4tag   = li_tags[i].find("h4", class_="result-card__subtitle job-result-card__subtitle")
			spantag = li_tags[i].find("span", class_="screen-reader-text")
			timetag = li_tags[i].find("time", class_="job-result-card__listdate")
			
			if atag and spantag and h4tag and timetag:
				link    = atag["href"]
				job     = spantag.text
				company = h4tag.text
				posted  = timetag.text

				self.insert2db(link, job, company, posted)

				print("Link:      " + atag["href"])
				print("Job Title: " + spantag.text)
				print("Company:   " + h4tag.text)
				print("Posted:    " + timetag.text)

				print("\n")

	def insert2db(self, link, job_title, company, posted):
		conn = psycopg2.connect(host="localhost", database="LinkedIn_Jobs_Database_05_09_2021", user="postgres", password="767992")
		curr = conn.cursor()

		build_sql = "insert into joblinks(job_link,job_title,company,posted_days) values ('" + link  + "','" + job_title + "','" + company + "','" + posted + "')"
		curr.execute(build_sql)
		conn.commit()


x = BS4Parse()
x.JobDetails()