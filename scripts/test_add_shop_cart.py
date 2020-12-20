import pytest

from base.base_driver import BaseDriver
from page.page_add_shop_cart import PageAddShopCart
from page.page_login import PageLogin


class TestLogin:
    def setup(self):
        self.driver = BaseDriver().get_driver(noReset=False)
        self.pagelogin = PageLogin(driver=self.driver)
        self.pageaddshopcart = PageAddShopCart(driver=self.driver)

    def teardown(self):
        self.driver.quit()

    def test_add_shop_cart(self):
        self.pagelogin.page_login_state()
        self.pageaddshopcart.pageaddshopcart()


if __name__ == '__main__':
    pytest.main(["-s", "test_add_shop_cart.py"])
