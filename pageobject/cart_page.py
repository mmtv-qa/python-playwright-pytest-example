import allure

from .base_page import Page


class CartPage(Page):

    @allure.step('Open cart page')
    def open(self, base_url: str):
        self._page.goto(base_url + 'cart.html')

    @allure.step('Check that backpack in cart')
    def should_present_backpack_in_cart(self):
        assert self._page.is_visible("//div[@class='inventory_item_name' and "
                                     "normalize-space(text())='Sauce Labs Backpack']")

    @allure.step('Delete item from cart')
    def delete_item_from_cart(self):
        self._page.click("//div[@class='inventory_item_name' and normalize-space(text())]/../.."
                         "//button[normalize-space(text())='Remove']")
