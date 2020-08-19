from selenium.webdriver.common.by import By


class TitlePageLocators:
    # AUTHORIZATION FORMS
    LOGIN_FORM = (By.ID, "index_email")
    PASSWORD_FORM = (By.ID, "index_pass")
    LOGIN_BUTTON = (By.ID, "index_login_button")
    LOGIN_REMEMBER_ME = (By.ID, "index_expire")
    LOGIN_MESSAGE_ERROR = (By.CLASS_NAME, "msg error")
    # REGISTRATION FORMS
    LINK_FORGOT_PASSWORD = (By.ID, "index_forgot")
    FORM_REGISTER_FIRSTNAME = (By.ID, "ij_first_name")
    FORM_REGISTER_LASTNAME = (By.ID, "ij_last_name")
    FORM_REGISTER_DATE = (By.XPATH, f"//div[contains(@id, 'container1')]/table/tbody/tr/td[contains(@class, 'selector_dropdown')]")
    FORM_REGISTER_MONTH = (By.XPATH, f"//div[contains(@id, 'container2')]/table/tbody/tr/td[contains(@class, 'selector_dropdown')]")
    FORM_REGISTER_YEAR = (By.XPATH, f"//div[contains(@id, 'container3')]/table/tbody/tr/td[contains(@class, 'selector_dropdown')]")
    REGISTER_RADIO_BUTTONS = (By.ID, "ij_sex_row")
    REGISTER_RADIO_BUTTON_FEMALE = (By.XPATH, "//div/div[contains(@class, 'radiobtn')][1]")
    REGISTER_RADIO_BUTTON_MALE = (By.XPATH, "//div/div[contains(@class, 'radiobtn')][2]")
    REGISTER_BUTTON = (By.ID, "ij_submit")
    JOIN_HEADER = (By.CLASS_NAME, "join_header")
    JOIN_PHONE = (By.ID, "join_phone")
    JOIN_SEND_PHONE = (By.ID, "join_send_phone")
    JOIN_CALLED_PHONE = (By.ID, "join_called_phone")
    JOIN_SEND_CODE = (By.ID, "join_send_code")
    # RECAPTCHA AND MESSAGE FORM
    RECAPTCHA = (By.CLASS_NAME, "box_layout")
    MESSAGE_TEXT = (By.CLASS_NAME, "msg_text")

    @classmethod
    def convert_register_date(cls, day):
        return By.ID, f"option_list_options_container_1_{day + 1}"

    @classmethod
    def convert_register_month(cls, month):
        return By.ID, f"option_list_options_container_2_{month + 1}"

    @classmethod
    def convert_register_year(cls, year):
        return By.ID, f"option_list_options_container_3_{2008 - year}"


