import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.activite_code import Code_activite
from pages.detals_page import Detals_page
from pages.home_page_test import Home
from pages.new_detals_pade import New_pay


def test_progect():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))




    h = Home(driver)
    h.open_bank_page()

    c = Code_activite(driver)
    c.open_activite_code()

    # dp =Detals_page(driver)
    # dp.select_detal_page()

    nwp =New_pay(driver)
    nwp.open_path_bil()

    time.sleep(5)