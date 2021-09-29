"""
    EXPLANATION OF LOGIC

    "Now when @pytest.fixture is applied more than once to the same function a ValueError is raised. This buggy behavior
    would cause surprising problems and if was working for a test suite it was mostly by accident." -The solution is to
    not apply the @fixture decorator twice to the function.
    https://github.com/pytest-dev/pytest/issues/3518#issuecomment-392599173

    we can't use it like this :(

    def title_page(request):
        ...

    title_page = pytest.fixture(title_page, scope="class")
    title_page_func = title_page
    title_page_func = pytest.fixture((title_page_func := title_page), scope="function")
"""

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.titile_page import TitlePage
from settings import logger_vk, LINK_VK


logger_get_browser = logger_vk.new(head="browser")
logger_get_title_page = logger_vk.new(head="page")


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser language")


@pytest.fixture(scope="class")
def title_page(request):
    """
    fixture for configure and launch the browser
    """
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    logger_get_title_page_ = logger_get_title_page.new(browser=browser_name)
    logger_get_title_page_.info('start_page')
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.to_capabilities()
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        logger_get_title_page_.error(exception=f"the {browser_name} is not support")
        raise type("NoSupportBrowser",
                   (Exception,),
                   {
                       '__doc__': 'the browser is not support',
                   })
    page = TitlePage(
        browser=browser,
        url=LINK_VK,
        logger=logger_get_title_page_
    )
    page.open()
    yield page
    logger_get_browser.info("close_page", browser=browser_name)
    browser.quit()


@pytest.fixture(scope="function")
def title_page_for_every_request(request):
    """
    fixture for configure and launch the browser.
    """
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    logger_get_title_page_ = logger_get_title_page.new(browser=browser_name)
    logger_get_title_page_.info('start_page')
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.to_capabilities()
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        logger_get_title_page_.error(exception=f"the {browser_name} is not support")
        raise type("NoSupportBrowser",
                   (Exception,),
                   {
                       '__doc__': 'the browser is not support',
                   })
    page = TitlePage(
        browser=browser,
        url=LINK_VK,
        logger=logger_get_title_page_
    )
    page.open()
    yield page
    logger_get_browser.info("close_page", browser=browser_name)
    browser.quit()



