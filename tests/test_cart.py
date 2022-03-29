import allure
import pytest

from pageobject.Page import Page


@allure.suite('Cart')
@allure.title('Cart test')
@pytest.mark.cart
def test_add_item_to_cart(context, base_url, creds_for_login):
    main_page = Page.MainPage(context, base_url)
    main_page.open_with_auth(creds_for_login['login'], creds_for_login['password'])
    main_page.app_backpack_to_cart()
    cart_page = Page.CartPage(context, base_url)
    cart_page.open()
    cart_page.should_present_backpack_in_cart()
    cart_page.delete_item_from_cart()
