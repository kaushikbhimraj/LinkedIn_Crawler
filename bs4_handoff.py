"""
Description:
	Program uses beautiful soup, to parse all jobs listed on the LinkedIn job search page. 

Notes:
	Postgres connection will have to be updated to insert values from job details. 
"""

from bs4 import BeautifulSoup
from main import ParseJobs
import requests

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

			print("Link:      " + atag["href"]) if atag else print("Link:      " + "NA")
			print("Job Title: " + spantag.text) if spantag else print("Job Title: " + "NA")
			print("Company:   " + h4tag.text) if h4tag else print("Company:    " +  "NA")
			print("Posted:    " + timetag.text) if timetag else print("Posted:    " +  "NA")

			print("\n")

x = BS4Parse()
x.JobDetails()