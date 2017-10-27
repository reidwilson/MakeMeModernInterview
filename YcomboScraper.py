from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://news.ycombinator.com/')
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, "html.parser")
letters = soup.select(".storylink")
count = 0
wordList = []
lettersLen = len(letters)

while count != lettersLen:
    wordList.append(str(letters[count].text))
    print(wordList[count])
    count += 1

totalAvg = 0.0
count = 0

while count != lettersLen:
    mySplit = wordList[count].split()
    myCalc = sum(len(cur) for cur in mySplit) / len(mySplit)
    totalAvg = totalAvg + myCalc
    count += 1

totalAvg = totalAvg/lettersLen
print('\nThe average word length is', totalAvg)
