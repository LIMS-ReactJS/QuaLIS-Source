############################################################################################################################################################################
# 1. click() - || Author: ATE186, Date: 1th June 2022, ID - #11 ||
# 2. sendKeys() - || Author: ATE186, Date: 1th June 2022 ID - #11 ||
# 3. clear() - || Author: ATE186, Date: 1th June 2022 ID - #11 ||
# 4. sleep() - || Author: ATE186, Date: 1th June 2022 ID - #11 ||
# 5. screenshot() - || Author: ATE186, Date: 1th June 2022 ID - #11 ||
# 6. maximize() - || Author: ATE186, Date: 1th June 2022 ID - #11 ||
# 7. minimize() - || Author: ATE186, Date: 1th June 2022 ID - #11 ||
# 8. implicitWait() - || Author: ATE186, Date: 1th June 2022 ID - #11 ||
# 9. title() - || Author: ATE186, Date: 1th June 2022 ID - #11 ||
# 10. url() - || Author: ATE186, Date: 1th June 2022 ID - #11 ||
# 11. text() - || Author: ATE186, Date: 1th June 2022 ID - #11 ||
############################################################################################################################################################################

import time
from selenium.webdriver.common.by import By

from Utilities import BrowserOperation

def click(driver,xpath):
    driver.find_element(By.XPATH,xpath).click()


def sendKeys(driver,xpath,value):
    driver.find_element(By.XPATH, xpath).send_keys(value)


def clear(driver,xpath):
    driver.find_element(By.XPATH, xpath).clear()


def sleep(seconds):
    time.sleep(seconds)


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


