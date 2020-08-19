from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import TIME_WAIT
from pages.locators import TitlePageLocators


class BasePage:

    def __init__(self, browser, url, logger, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.logger = logger

    def open(self):
        """Opening the desired page"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """Search for an element on a page"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def manual_definition_of_captcha(self, time_wait_capcha: int = TIME_WAIT):
        """Passage of capcha, if captcha exist"""
        try:
            if WebDriverWait(self.browser, time_wait_capcha).until(
                    EC.presence_of_element_located(TitlePageLocators.RECAPTCHA)):
                self.logger.info('login_fake', recapcha="catch")
                WebDriverWait(self.browser, 150).until(
                    EC.invisibility_of_element_located(TitlePageLocators.RECAPTCHA)
                )
                self.logger.info('login_fake', recapcha="traversed")
        except TimeoutException:
            self.logger.info('login_fake', recapcha="no detected")
