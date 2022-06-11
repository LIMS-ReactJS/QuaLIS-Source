


from selenium import webdriver

from Utilities import Utility

driver = webdriver.Chrome("..\\chromedriver.exe")


Utility.get(driver,"http://agl78:9090/QuaLISWeb/#/login")