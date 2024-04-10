import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def slurr(link):
    driver = webdriver.Chrome()
    driver.get(link)
    opsi = webdriver.ChromeOptions()
    opsi.add_extension('adblock.crx')
    print("Pastikan Adblock Aktif...")
    time.sleep(5)
    try:
        not_robot = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                    '//*[@id="wpsafelinkhuman"]/img')))
        not_robot.click()
    except Exception:
        print("Gagal")

    time.sleep(5)
    try:
        open_link = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,
                                                                                '//*[@id="wpsafe-generate"]/a/img')))
        open_link.click()
        unlock_dwonloads = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,
                                                                                       '//*[@id="wpsafe-link"]/a/img')))
        unlock_dwonloads.click()
        time.sleep(5)
    except Exception:
        print('gagal')
    return driver.current_url


if __name__ == '__main__':
    os.remove('link.txt')
    with open('link.txt', 'w+') as file:
        file.write(slurr(link=input("Masukkan Link: ")))
        file.close()
    os.system('notepad.exe link.txt')
