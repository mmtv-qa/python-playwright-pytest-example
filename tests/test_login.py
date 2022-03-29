import allure
import pytest

from app.Page import Page


@allure.suite('Authentication')
@allure.title('Test authentication with valid credentials')
@pytest.mark.auth
def test_auth_with_valid_credentials(context, creds_for_login, base_url):
    page = Page.LoginPage(context, base_url)
    page.open()
    page.enter_login(creds_for_login["login"])
    page.enter_password(creds_for_login["password"])
    page.tap_login_button()
    page.should_open_main_page()


@allure.suite('Authentication')
@allure.title('Test authentication with valid credentials')
@pytest.mark.auth
def test_auth_with_invalid_credentials(context, fake_login, fake_password, base_url):
    page = Page.LoginPage(context, base_url)
    page.open()
    page.enter_login(fake_login)
    page.enter_password(fake_password)
    page.tap_login_button()
    page.should_be_epic_sadface_text()
