from selenium import webdriver

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
browser.get('http:./localhost:8000')

assert 'Django' in browser.title
