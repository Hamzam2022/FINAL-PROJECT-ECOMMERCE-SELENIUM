# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture()
def driver():
    chrome_driver_binary = "./drivers/chromedriver"
    ser_chrome = ChromeService(chrome_driver_binary)
    driver = webdriver.Chrome(service=ser_chrome)
    driver.get('https://www.shein.com')
    yield driver
    driver.close()


def test_testregister(driver):
    element = driver.find_element(By.CSS_SELECTOR, ".sui_icon_nav_me_24px")
    driver.execute_script("arguments[0].click();", element)
    driver.find_element(By.CSS_SELECTOR,
                             ".page-signup__emailLoginItem > .input-area-email .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                             ".page-signup__emailLoginItem > .input-area-email .S-input__inner").send_keys(
        "tfakotttg@gmail.com")
    driver.find_element(By.CSS_SELECTOR,
                             ".page-signup__emailLoginItem > .input-area-password .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                             ".page-signup__emailLoginItem > .input-area-password .S-input__inner").send_keys(
        "h1234567")
    driver.find_element(By.CSS_SELECTOR, ".input-area-confirm-password .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".input-area-confirm-password .S-input__inner").send_keys("h1234567")
    driver.find_element(By.CSS_SELECTOR,
                             ".page-login__stylePreference:nth-child(4) .S-checkbox:nth-child(2) .S-checkbox__input-inner").click()
    driver.find_element(By.CSS_SELECTOR, ".login-btn:nth-child(6) span").click()
    time.sleep(5)
    element1 = driver.find_element(By.CSS_SELECTOR, ".reg-show-top > p")
    driver.execute_script("arguments[0].click();", element1)
    assert element1.text == "Congratulations! You have successfully registered!"




def test_verifyInvalidEmailAddress(driver):
        element1 = driver.find_element(By.CSS_SELECTOR, ".sui_icon_nav_me_24px")
        driver.execute_script("arguments[0].click();", element1)
        driver.find_element(By.CSS_SELECTOR,
                                 ".page-login__container_item:nth-child(1) .input-area-email .S-input__inner").click()
        driver.find_element(By.CSS_SELECTOR,
                                 ".page-login__container_item:nth-child(1) .input-area-email .S-input__inner").send_keys(
            "stewqd1d@fdsdhf.com")
        driver.find_element(By.CSS_SELECTOR,
                                 ".page-login__container_item:nth-child(1) .input-area-password .S-input__inner").click()
        driver.find_element(By.CSS_SELECTOR,
                                 ".page-login__container_item:nth-child(1) .input-area-password .S-input__inner").send_keys("6jdhfdkldl")
        driver.find_element(By.CSS_SELECTOR, ".page-login__emailLoginItem > .login-btn:nth-child(5) span").click()
        time.sleep(5)

        element2 = driver.find_element(By.CSS_SELECTOR,
                                        ".error .error-tip")
        assert element2.text == "The Email Address or Password you entered is incorrect."
        time.sleep(3)
