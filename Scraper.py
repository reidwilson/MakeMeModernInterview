from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('http://www.bbc.com/')
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, "html.parser")
ostream = open('titled bbc-links.txt', 'w')
for link in soup.find_all('a'):
    Test1 = 'http://'
    Test2 = 'https://'
    myLink = link.get('href')
    if Test1 not in foo and Test2 not in foo:
        foo = Test1 + 'www.bbc.com' + myLink
    ostream.write(myLink + '\n')
ostream.close()
