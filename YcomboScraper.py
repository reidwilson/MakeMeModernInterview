from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://news.ycombinator.com/')
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, "html.parser")
#print(soup.prettify()[:])
letters = soup.select(".storylink")
foo = 0
wordList = []
while foo != 30:
    wordList.append(str(letters[foo].text))
    print(wordList[foo])
    foo += 1
#avgList = []
totalAvg = 0.0
foo = 0
while foo != 30:
    mySplit = wordList[foo].split()
    myCalc = sum(len(cur) for cur in mySplit) / len(mySplit)
    totalAvg = totalAvg + myCalc
    foo += 1
    #avgList.append(myCalc)
totalAvg = totalAvg/30
print('\nThe total average word length is', totalAvg)
