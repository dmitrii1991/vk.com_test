import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import TitlePageLocators
from settings import TIME_WAIT


class TitlePage(BasePage):

    def login_fake(self, fake_user: str, fake_password: str) -> None:
        """The main goal is to get an error message when logging in"""
        # FILLING IN THE AUTHORIZATION FORM
        self.browser.find_element(*TitlePageLocators.LOGIN_FORM).send_keys(fake_user)
        self.browser.find_element(*TitlePageLocators.PASSWORD_FORM).send_keys(fake_password)
        self.browser.find_element(*TitlePageLocators.LOGIN_REMEMBER_ME).click()
        self.browser.find_element(*TitlePageLocators.LOGIN_BUTTON).click()
        # PASSAGE OF CAPTCHA, IF CAPTCHA EXIST
        self.manual_definition_of_captcha()
        element_for_wait = WebDriverWait(self.browser, TIME_WAIT).until(
            EC.presence_of_element_located(TitlePageLocators.MESSAGE_TEXT))
        # CHECKING CONDITIONS
        if element_for_wait:
            self.logger.info('login_fake', msg_text=True)
        else:
            self.logger.error('login_fake', msg_text=False)
        assert element_for_wait, "message ERROR is not got"
        assert 'Failed to log in' in element_for_wait.text, "message 'Failed to log in' is not got"

    def register_fake(self, fake_firstname: str, fake_lastname: str, day: int, month: int, year: int,
                      phone: int, code: int, gender: str = "male") -> None:
        """The main goal is to get an error message about registration"""
        # FILLING IN THE REGISTRATION FORM
        self.browser.find_element(*TitlePageLocators.FORM_REGISTER_FIRSTNAME).send_keys(fake_firstname)
        self.browser.find_element(*TitlePageLocators.FORM_REGISTER_LASTNAME).send_keys(fake_lastname)
        self.browser.find_element(*TitlePageLocators.FORM_REGISTER_DATE).click()
        self.browser.find_element(*TitlePageLocators.convert_register_date(day)).click()
        self.browser.find_element(*TitlePageLocators.FORM_REGISTER_MONTH).click()
        self.browser.find_element(*TitlePageLocators.convert_register_month(month)).click()
        self.browser.find_element(*TitlePageLocators.FORM_REGISTER_YEAR).click()
        self.browser.find_element(*TitlePageLocators.convert_register_year(year)).click()
        if gender == "male":
            self.browser.find_element(*TitlePageLocators.REGISTER_RADIO_BUTTON_MALE).click()
        else:
            self.browser.find_element(*TitlePageLocators.REGISTER_RADIO_BUTTON_FEMALE).click()
        self.browser.find_element(*TitlePageLocators.REGISTER_BUTTON).click()
        # PASSAGE OF CAPTCHA, IF CAPTCHA EXIST
        self.manual_definition_of_captcha()
        # FILLING IN THE FORM WITH YOUR PHONE
        WebDriverWait(self.browser, TIME_WAIT).until(EC.presence_of_element_located(TitlePageLocators.JOIN_HEADER))
        self.browser.find_element(*TitlePageLocators.JOIN_PHONE).send_keys(phone)
        self.browser.find_element(*TitlePageLocators.JOIN_SEND_PHONE).click()
        # PASSAGE OF CAPTCHA, IF CAPTCHA EXIST
        self.manual_definition_of_captcha()
        # user simulation
        time.sleep(2)
        # FILLING IN THE SECURITY CODE FORM
        WebDriverWait(self.browser, TIME_WAIT).until(EC.presence_of_element_located(TitlePageLocators.JOIN_CALLED_PHONE))
        self.browser.find_element(*TitlePageLocators.JOIN_CALLED_PHONE).send_keys(code)
        self.browser.find_element(*TitlePageLocators.JOIN_SEND_CODE).click()
        # CHECKING CONDITIONS
        if incorrect_number_message := WebDriverWait(self.browser, TIME_WAIT).until(
                EC.presence_of_element_located(TitlePageLocators.MESSAGE_TEXT)):
            self.logger.info('incorrect_number_message', show=True)
        else:
            self.logger.error('incorrect_number_message', show=False)
            assert incorrect_number_message, "incorrect number message is not presented"

        assert incorrect_number_message, "message ERROR is not got"
        assert "Incorrect number" in incorrect_number_message.text, "message 'Failed to log in' is not got"

    def should_be_forgot_password_link(self):
        """Checking for the existence of a link to a forgotten password"""
        if link_forgot_password := self.is_element_present(*TitlePageLocators.LINK_FORGOT_PASSWORD):
            self.logger.info('link_forgot_password', show=True)
        else:
            self.logger.error('link_forgot_password', show=False)
            assert link_forgot_password, "forgotten password link is not presented"

    def should_be_form_phone_or_email(self):
        """Checking for the existence of a link to a forgotten password"""
        if form_phone_or_email := self.is_element_present(*TitlePageLocators.LOGIN_FORM):
            self.logger.info('form_phone_or_email', show=True)
        else:
            self.logger.error('form_phone_or_email', show=False)
            assert form_phone_or_email, "phone form or email form  is not presented"

    def should_be_form_password(self):
        """Checking for the existence of a password form"""
        if form_password := self.is_element_present(*TitlePageLocators.PASSWORD_FORM):
            self.logger.info('form_password', show=True)
        else:
            self.logger.error('form_password', show=False)
            assert form_password, "password form is not presented"

    def should_be_form_register_name(self):
        """Checking for the existence of a register-name form"""
        if form_register_name := self.is_element_present(*TitlePageLocators.FORM_REGISTER_FIRSTNAME):
            self.logger.info('form_register_name', show=True)
        else:
            self.logger.error('form_register_name', show=False)
            assert form_register_name, "form register firstname is not presented"

    def should_be_form_register_lastname(self):
        """Checking for the existence of a register-lastname form"""
        if form_register_lastname := self.is_element_present(*TitlePageLocators.FORM_REGISTER_LASTNAME):
            self.logger.info('form_register_lastname', show=True)
        else:
            self.logger.error('form_register_lastname', show=False)
            assert form_register_lastname, "form register lastname is not presented"

    def should_be_form_register_date(self):
        """Checking for the existence of a register-date/month/year form"""
        if register_date := self.is_element_present(*TitlePageLocators.FORM_REGISTER_DATE):
            self.logger.info('register_date', show=True)
        else:
            self.logger.error('register_date', show=False)
            assert register_date, "form register date is not presented"
        if register_month := self.is_element_present(*TitlePageLocators.FORM_REGISTER_MONTH):
            self.logger.info('register_month', show=True)
        else:
            self.logger.error('register_month', show=False)
            assert register_month, "form register month is not presented"
        if register_year := self.is_element_present(*TitlePageLocators.FORM_REGISTER_YEAR):
            self.logger.info('register_year', show=True)
        else:
            self.logger.error('register_year', show=False)
            assert register_year, "form register year is not presented"

    def should_be_register_radio_buttons(self):
        """Checking for the existence of register radio buttons"""
        if register_radio_buttons := self.is_element_present(*TitlePageLocators.REGISTER_RADIO_BUTTONS):
            self.logger.info('register_radio_buttons', show=True)
        else:
            self.logger.error('register_radio_buttons', show=False)
            assert register_radio_buttons, "register radio buttons are not presented"

    def should_be_register_button(self):
        """Checking for the existence of a register button"""
        if register_button := self.is_element_present(*TitlePageLocators.REGISTER_RADIO_BUTTONS):
            self.logger.info('register_button', show=True)
        else:
            self.logger.error('register_button', show=False)
            assert register_button, "register radio button is not presented"
