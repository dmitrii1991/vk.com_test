import pytest


@pytest.mark.title_vk
class TestTitlePage:
    """Checking the location of elements of the registration and authorization form"""

    def test_guest_can_see_login_elements(self, title_page):
        """Checking the location of elements of the authorization form"""
        title_page.should_be_forgot_password_link()
        title_page.should_be_form_phone_or_email()
        title_page.should_be_form_password()

    def test_guest_can_see_register_elements(self, title_page):
        """Checking the location of elements of the registration form"""
        title_page.should_be_form_register_name()
        title_page.should_be_form_register_lastname()
        title_page.should_be_form_register_date()
        title_page.should_be_register_radio_buttons()
        title_page.should_be_register_button()


@pytest.mark.login_guest
class TestLoginRegister:

    def test_guest_can_login(self, title_page_for_every_request):
        title_page_for_every_request.open()
        title_page_for_every_request.login_fake('fake', '123456789')

    def test_guest_can_register(self, title_page_for_every_request):
        title_page_for_every_request.open()
        title_page_for_every_request.register_fake(
            fake_firstname='Dino',
            fake_lastname='Dinamo',
            day=10,
            month=1,
            year=2001,
            phone=9817888720,
            code=9317
        )

