from selenium.webdriver import Keys

from base.buse_page import Buse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class New_pay(Buse):


    def __init__(self,  driver):
        super().__init__(driver)
        self.driver = driver


    # LOCATORS

    payment_tab = "//a[@id='payments-form']"
    mob_pay = "//div[@title='Мой телефон']//div[@class='logo']"
    as_date ="//a[@id='as-recurrent-link']"
    mobile_phonr  = "//input[@name='phoneNumber']"
    chek_box_sus = "//input[@id='show-suggest-subscription']"
    pay_btn_mob = "//button[@id='forward']"


    # GETERS

    def get_payment_tab(self):
        return  WebDriverWait(self.driver, 30).until( EC.presence_of_element_located((By.XPATH, self.payment_tab)))

    def get_mob_pay(self):
        return WebDriverWait(self.driver, 30).until( EC.presence_of_element_located((By.XPATH, self.mob_pay)))

    def get_as_date(self):
        return WebDriverWait(self.driver, 30).until( EC.presence_of_element_located((By.XPATH, self.as_date)))

    def get_mobile_phonr(self):
        return WebDriverWait(self.driver, 30).until( EC.presence_of_element_located((By.XPATH, self.mobile_phonr)))

    def get_chek_box_sus(self):
        return WebDriverWait(self.driver, 30).until( EC.presence_of_element_located((By.XPATH, self.chek_box_sus)))

    def get_pay_btn_mob(self):
        return WebDriverWait(self.driver, 30).until( EC.presence_of_element_located((By.XPATH, self.pay_btn_mob)))


    # ACTIONS

    def click_payment_tab(self):
        self.get_payment_tab().click()
        print("click payments tab")

    def click_mob_pay(self):
        self.get_mob_pay().click()
        print("select payments")

    def click_as_date(self):
        self.get_as_date().click()
        print("Click date link")


    def input_mobile_phonr_cl(self):
        self.get_mobile_phonr().clear()
        print("clear find phoen ")

    def imput_mobile_phonr(self , mobile_phonr):
        self.get_mobile_phonr().send_keys(mobile_phonr)
        print("inpur phopne number")

    def click_chek_box_sus(self):
        self.get_chek_box_sus().click()
        print("click check box ")

    def click_pay_btn_mob(self):
        self.get_pay_btn_mob().click()
        print("click pey button")






    # METHOD

    def open_path_bil(self):
        self.click_payment_tab()
        self.click_mob_pay()
        self.click_as_date()
        self.input_mobile_phonr_cl()
        self.imput_mobile_phonr("+7 (911) 999-99-99")
        self.click_on_checkbox()
        self.click_pay_btn_mob()




