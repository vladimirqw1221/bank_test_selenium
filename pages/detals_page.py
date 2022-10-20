from selenium.webdriver import Keys

from base.buse_page import Buse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Detals_page(Buse):


    def __init__(self,  driver):
        super().__init__(driver)
        self.driver = driver


    # LOCATORS

    payments = "//a[@id='payments-form']"
    fovourite_spb = "//div[@title='Избранное сбп']//a[@title='Pay']"
    credit_account = "//select[@name='accountId']"
    amount = "//input[@name='amount']"
    transfer_btn = "//button[@id='transfer']"
    confirm = "//button[@id='confirm']"
    active_btn = "//button[@id='submit-button']"


    # GETERS

    def get_payments(self):
        return  WebDriverWait(self.driver, 30).until( EC.presence_of_element_located((By.XPATH, self.payments)))

    def get_fovourite_spb(self):
        return  WebDriverWait(self.driver, 30).until( EC.presence_of_element_located((By.XPATH, self.fovourite_spb)))

    def get_credit_account(self):
        return  WebDriverWait(self.driver, 30).until( EC.presence_of_element_located((By.XPATH, self.credit_account)))

    def get_active_btn(self):
        return  WebDriverWait(self.driver, 30).until( EC.presence_of_element_located((By.XPATH, self.active_btn)))




    # ACTIONS

    def click_payments(self):
        self.get_payments().click()
        print("click tab payments")

    def click_fovourite_spb(self):
        self.get_fovourite_spb().click()
        print("click fovourite button ")

    def click_credit_account(self):
        self.get_credit_account().click()
        print("select credit account")

    def select_credit_account(self):
        self.get_credit_account().send_keys(Keys.ARROW_DOWN)
        print("Select accounr ")

    def select_another_accounr(self):
        self.get_credit_account().send_keys(Keys.RETURN)
        print("Enter find anotger accoubt")

    def click_active_btn(self):
        self.get_active_btn().cleck()
        print("click button activite btn ")


    # METHOD

    def select_detal_page(self):
        # self.get_current_url()
        # self.allert_clouse()
        self.click_payments()
        self.click_fovourite_spb()
        self.click_credit_account()
        self.select_credit_account()
        self.select_another_accounr()
        self.click_active_btn()




