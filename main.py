# import module
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#path lacation chromedriver.exe
Path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(executable_path=Path)
driver.get('https://www.instagram.com/')

# seacrh xpath html tag 
iduser = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
# username ig
iduser.send_keys('Your username....')# example

passuser = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
#password ig
passuser.send_keys('Your password....')# example
passuser.send_keys(Keys.RETURN)