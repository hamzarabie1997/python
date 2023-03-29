import webbrowser
import requests
from bs4 import BeautifulSoup as bs

user_name = input('Enter GitHub user that you want to get its photo: ')
url = 'https://github.com/' + user_name
r = requests.get(url)
soup = bs(r.content, 'html.parser')
pro_img = soup.find('img', {'alt' : 'Avatar'})['src']
webbrowser.open(pro_img)