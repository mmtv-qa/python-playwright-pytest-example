from pageobject.cart_page import CartPage
from pageobject.login_page import LoginPage
from pageobject.main_page import MainPage


class Page:

    @staticmethod
    def MainPage(context, base_url):
        return MainPage(context=context, base_url=base_url)

    @staticmethod
    def CartPage(context, base_url):
        return CartPage(context=context, base_url=base_url)

    @staticmethod
    def LoginPage(context, base_url):
        return LoginPage(context=context, base_url=base_url)
