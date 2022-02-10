import allure
import pytest

from pageobject.login_page import LoginPage


@allure.suite('Authentication')
@allure.title('Test authentication with valid credentials')
@pytest.mark.auth
def test_auth_with_valid_credentials(context, creds_for_login, base_url):
    page = LoginPage(context)
    page.open(base_url)
    page.enter_login(creds_for_login["login"])
    page.enter_password(creds_for_login["password"])
    page.tap_login_button()
    page.should_open_main_page(base_url)


@allure.suite('Authentication')
@allure.title('Test authentication with valid credentials')
@pytest.mark.auth
def test_auth_with_invalid_credentials(context, fake_login, fake_password, base_url):
    page = LoginPage(context)
    page.open(base_url)
    page.enter_login(fake_login)
    page.enter_password(fake_password)
    page.tap_login_button()
    page.should_be_epic_sadface_text()
