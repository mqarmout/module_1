# Python script to scrape an article given the url of the article and store the extracted text in a file
# Url: https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7

# Modified by Younes your collaborator

import os
import requests
import re
# Code here - Import BeautifulSoup library
from bs4 import BeautifulSoup
# Code ends here

# function to get the html source text of the medium article
def get_page():
	global url
	
	# Code here - Ask the user to input "Enter url of a medium article: " and collect it in url
	url = input("please provide the the URL of a medium article for scrapping: ")
	# Code ends here
	
	# handling possible error
	if not re.match(r'https?://medium.com/',url):
		print('Please enter a valid website, or make sure it is a medium article')
		os.system.exit(1)

	# Code here - Call get method in requests object, pass url and collect it in res
	headers = {
    	'User-Agent': 'Mozilla/5.0'
	}
	# headers was needed to get past the capthca denying entry for scripts
	res = requests.get(url, headers=headers)
	# Code ends here

	res.raise_for_status()
	soup = BeautifulSoup(res.text, 'html.parser')
	return soup

# function to remove all the html tags and replace some with specific strings
def clean(text):
    rep = {"<br>": "\n", "<br/>": "\n", "<li>":  "\n",
		   "\nSign up\n": "", "\nSign in\n": "", "\nListen\n": "",
		   "\nShare\n": "", "\nFollow\n": "", "\nHelp\n": "",
		   "\nStatus\n": "", "\nAbout\n": "", "\nCareers\n": "",
		   "\nBlog\n": "", "\nPrivacy\n": "", "\nBlog\n": "",
		   "\nTerms\n": "", "\nText to speech\n": "",
		   "\nTeams\n": "", "\nCS Teacher to ...\n": "",
		   "\n--\n": ""}
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    text = re.sub('\<(.*?)\>', '', text)
    return text.strip()

def collect_text(soup):
	text = f'url: {url}\n\n'
	para_text = soup.find_all('p')
	for para in para_text:
		text += f"{para.text}\n\n"
	return text

# function to save file in the current directory
def save_file(text):
	name = url.split("/")[-1]
	fname = f'{name}.txt'
	
	# Code here - write a file using with (2 lines)
	with open(fname, "w") as file:
		file.write(clean(text))
	# Code ends here

	print(f'File saved in directory {fname}')


if __name__ == '__main__':
	text = collect_text(get_page())
	save_file(text)
	# Instructions to Run this python code
	# Give url as https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7