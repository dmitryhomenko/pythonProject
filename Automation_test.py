from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.get('http://netpeak.ua')
    under_us = driver.find_element(By.XPATH, '//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[1]/div[1]/ul/li[3]')
    under_us.click()
    time.sleep(2)

    comand = driver.find_element(By.PARTIAL_LINK_TEXT, 'Команда')
    comand.click()
    time.sleep(5)

    html = driver.find_element(By.TAG_NAME, "html") # Гортаємо сторінку вниз
    for i in range(5):
        html.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

    part_of_comand = driver.find_element(By.XPATH,'//*[@id="rec278626926"]/div/div/div[10]/a')
    part_of_comand.click()
    time.sleep(3)

    tabs = driver.window_handles  # список вкладок
    driver.switch_to.window(tabs[1])
    assert "Работа в Netpeak" in driver.title
    print(driver.title)
    time.sleep(3)
    html = driver.find_element(By.TAG_NAME, "html")
    for i in range(4):
        html.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Я хочу работать в Netpeak')))
    print(element.text)
    time.sleep(3)

    driver.switch_to.window(tabs[0])  # Повертаємось на попередню вкладку
    time.sleep(3)
    personal = driver.find_element(By.XPATH, '//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[1]/div[2]/ul/li[1]/a')
    personal.click()

    time.sleep(3)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[2])
    login_input = driver.find_element(By.ID, 'login')
    login_input.send_keys("log")
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys("pas")
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[5]/button').click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div[4]/div/md-checkbox/div[1]'))).click()

    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[5]/button').click()
    time.sleep(3)

    driver.close()
    driver.quit()



