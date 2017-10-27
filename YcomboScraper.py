from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://news.ycombinator.com/')
html = driver.page_source
driver.quit()
ostream = open('foo.txt', 'w')
soup = BeautifulSoup(html, "html.parser")
#print(soup.prettify()[:])
letters = soup.select(".storylink")#works
foo = 0
zee = []
while foo != 30:
    zee.append(str(letters[foo].text))
    print(zee[foo])
    foo = foo + 1
#avgList = []
totalAvg = 0.0
foo = 0
while foo != 30:
    mySplit = zee[foo].split()
    myCalc = sum(len(cur) for cur in mySplit) / len(mySplit)
    totalAvg = totalAvg + myCalc
    foo = foo+1
    #avgList.append(myCalc)
totalAvg = totalAvg/30
print('\nThe total average word length is '+str(totalAvg))
