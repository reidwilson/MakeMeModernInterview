from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://news.ycombinator.com/')
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, "html.parser")
tags = soup.select(".storylink")
textList = []
textListLen = len(tags)
count = 0
totalAvg = 0.0

while count != textListLen:
    textList.append(str(tags[count].text))
    print(textList[count])
    mySplit = textList[count].split()
    myCalc = sum(len(cur) for cur in mySplit) / len(mySplit)
    totalAvg += myCalc
    count += 1

totalAvg = totalAvg / textListLen
print('\nThe average word length is', totalAvg)
