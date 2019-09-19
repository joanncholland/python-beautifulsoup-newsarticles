# Import libraries
import requests
from bs4 import BeautifulSoup
import csv
from tkinter import *

root = Tk()

introduction = "This program scrapes the Guardian's Health and Wellbeing page, so you can glance through for articles of interest."

w = Label(root, text=introduction)
w.config(bg='white', font=('times', 24))

# Get health and wellness page
page = requests.get(
    'https://www.theguardian.com/lifeandstyle/health-and-wellbeing')

# BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# Find headline links
links = soup.findAll(class_='fc-item__title')

# Set up csv file
f = csv.writer(open('health-and-wellbeing-articles.csv', 'w'))
f.writerow(['Title', 'Link'])

# Retrieve each title and links
for link in links:
    title = link.find(class_='js-headline-text').contents[0]
    url = link.find(class_='fc-item__link').get('href')

    # Write title and url to csv file
    f.writerow([title, url])
