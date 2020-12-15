import pytest

from base.base_driver import BaseDriver
from page.page_login import PageLogin
from page.page_ship_to_addr import PageShipToAddr


class TestShipToAddr:
    def setup(self):
        self.driver = BaseDriver().get_driver(noReset=False)
        self.pagelogin = PageLogin(driver=self.driver)
        self.pageshiptoaddr = PageShipToAddr(driver=self.driver)

    def teardown(self):
        self.driver.quit()

    def test_ship_to_addr(self):
        self.pagelogin.page_login_state()
        self.pageshiptoaddr.pageshiptoaddr(recipient="张坤",
                                           phone_number="13273911234",
                                           detailed_address="湖南省衡阳市石鼓区合江套路天下花园12栋1014",
                                           postcode="454100")


if __name__ == '__main__':
    pytest.main(["-s", "test_ship_to_addr.py"])
