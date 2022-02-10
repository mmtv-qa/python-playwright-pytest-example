import allure

from .base_page import Page


class LoginPage(Page):

    @allure.step('Open login page')
    def open(self, base_url: str):
        self._page.goto(base_url)

    @allure.step('Input login: {1}')
    def enter_login(self, login: str):
        self._page.fill('#user-name', login)

    @allure.step('Input password: {1}')
    def enter_password(self, password: str):
        self._page.fill('#password', password)

    @allure.step('Tap login button')
    def tap_login_button(self):
        self._page.click("#login-button")

    @allure.step('Check that main page opened')
    def should_open_main_page(self, base_url: str):
        self._page.wait_for_load_state()
        assert self._page.url == base_url + 'inventory.html', 'Didn`t open main page'

    @allure.step('Check that alert text come to sight')
    def should_be_epic_sadface_text(self):
        assert self._page.is_visible("//h3[normalize-space(text())="
                                     "'Epic sadface: Username and password do not match any user in this service']"), \
                                        'Text not come'
