############################################################################################################################################################################
# 1. click() - || Author: ATE186, Date: 11th June 2022, ID - #11 ||
# 2. sendKeys() - || Author: ATE186, Date: 11th June 2022 ID - #11 ||
# 3. clear() - || Author: ATE186, Date: 11th June 2022 ID - #11 ||
# 4. sleep() - || Author: ATE186, Date: 11th June 2022 ID - #11 ||
# 5. screenshot() - || Author: ATE186, Date: 11th June 2022 ID - #11 ||
# 6. maximize() - || Author: ATE186, Date: 11th June 2022 ID - #11 ||
# 7. minimize() - || Author: ATE186, Date: 11th June 2022 ID - #11 ||
# 8. implicitWait() - || Author: ATE186, Date: 11th June 2022 ID - #11 ||
# 9. title() - || Author: ATE186, Date: 11th June 2022 ID - #11 ||
# 10. url() - || Author: ATE186, Date: 11th June 2022 ID - #11 ||
# 11. text() - || Author: ATE186, Date: 11th June 2022 ID - #11 ||
# 12. refresh() - || Author: ATE186, Date: 11th June 2022 ID - #11 ||
############################################################################################################################################################################
import os
import time
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from ObjectRepository import ElementCalender


def click(driver,xpath):
    driver.find_element(By.XPATH,xpath).click()


def sendKeys(driver,xpath,value):
    driver.find_element(By.XPATH, xpath).send_keys(value)


def clear(driver,xpath):
    driver.find_element(By.XPATH, xpath).clear()



def screenshot(driver,location):
    driver.save_screenshot(location)


def maximize(driver):
    driver.maximize_window()


def minimize(driver):
    driver.minimize_window()


def get(driver,link):
    driver.get(link);


def implicitWait(driver,time):
    driver.implicitly_wait(time)


def title(driver):
    titleValue=driver.title
    return titleValue

def url(driver):
    urlValue=driver.current_url
    return urlValue

def text(driver,xpath):
    driver.find_element(By.XPATH,xpath)

def refresh(driver):
    driver.refresh()

def projectDirectory():
    projectDirectory = ""
    fileDirectory = os.path.abspath(__file__)
    fileDirectoryArray = fileDirectory.split("\\")
    for i in fileDirectoryArray:
        projectDirectory = projectDirectory + "\\" + i
        if i == "QuaLIS-Source":
                break
    projectDirectory = projectDirectory[1:]
    return projectDirectory

def selectByText(driver,xpath,text):
    driver.find_element(By.XPATH,xpath).click()
    textXpath="//*[text()='{}']".format(text)
    driver.find_element(By.XPATH,textXpath).click()

def scrollToElement(driver,xpath):
    element = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].scrollIntoView();", element)

def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

def calender(driver,xpath,date):
    click(driver,xpath)
    dateDetail=date.split('-')
    day=dateDetail[0]
    month=dateDetail[1].capitalize()
    year=dateDetail[2]
    dateSelect=Select(driver.find_element(By.XPATH,ElementCalender.year))
    dateSelect.select_by_visible_text(year)
    monthSelect=Select(driver.find_element(By.XPATH,ElementCalender.month))
    monthSelect.select_by_visible_text(month)
    driver.find_element(By.XPATH,"//*[text()='{}']".format(day)).click()