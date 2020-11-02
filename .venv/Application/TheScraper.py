from bs4 import BeautifulSoup
import requests

url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

tweet = content.find_All('p', attrs={"class": "content"}).text
# using BS selectors, we want to select pTags, but only ones w/ class name Content
# .text says that if pTag with class Content found, select text Content of tag
for tweet in content.find_All('p', attrs={"class": "content"}):
    print(tweet)

#11/02/20@1:12PM



