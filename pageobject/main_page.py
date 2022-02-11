import allure

from .base_page import Page


class MainPage(Page):

    @allure.step('Open page and auth with valid credentials: {2}, {3}')
    def open_with_auth(self, login: str, password: str):
        self._page.goto(self._base_url)
        self._page.fill('#user-name', login)
        self._page.fill('#password', password)
        self._page.click("#login-button")

    @allure.step('Add backpack to cart')
    def app_backpack_to_cart(self):
        self._page.click('#add-to-cart-sauce-labs-backpack')
