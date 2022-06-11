############################################################################################################################################################################
# 1. click() - || Author: ATE186, Date: 1th June 2022, ID - ||
# 2. sendKeys() - || Author: ATE186, Date: 1th June 2022 ||
# 3. clear() - || Author: ATE186, Date: 1th June 2022 ||
# 4. sleep() - || Author: ATE186, Date: 1th June 2022 ||
# 5. screenshot() - || Author: ATE186, Date: 1th June 2022 ||
# 6. maximize() - || Author: ATE186, Date: 1th June 2022 ||
# 7. minimize() - || Author: ATE186, Date: 1th June 2022 ||
# 8. get() - || Author: ATE186, Date: 1th June 2022 ||
############################################################################################################################################################################
import time
from selenium.webdriver.common.by import By



def click(driver, xpath):
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



