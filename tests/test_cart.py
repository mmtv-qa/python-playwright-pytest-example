import allure
import pytest

from pageobject.cart_page import CartPage
from pageobject.main_page import MainPage


@allure.suite('Cart')
@allure.title('Cart test')
@pytest.mark.cart
def test_add_item_to_cart(context, base_url, creds_for_login):
    main_page = MainPage(context)
    main_page.open_with_auth(base_url, creds_for_login['login'], creds_for_login['password'])
    main_page.app_backpack_to_cart()
    cart_page = CartPage(context)
    cart_page.open(base_url)
    cart_page.should_present_backpack_in_cart()
    cart_page.delete_item_from_cart()
