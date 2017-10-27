from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://news.ycombinator.com/')
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, "html.parser")
tags = soup.select(".storylink")
count = 0
tagList = []
tagsLen = len(tags)

while count != tagsLen:
    tagList.append(str(tags[count].text))
    print(tagList[count])
    count += 1

totalAvg = 0.0
count = 0

while count != tagsLen:
    mySplit = tagList[count].split()
    myCalc = sum(len(cur) for cur in mySplit) / len(mySplit)
    totalAvg = totalAvg + myCalc
    count += 1

totalAvg = totalAvg / tagsLen
print('\nThe average word length is', totalAvg)
