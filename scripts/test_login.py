import pytest

from base.base_driver import BaseDriver
from page.page_login import PageLogin


class TestLogin:
    def setup(self):
        self.driver = BaseDriver().get_driver()
        self.pagelogin = PageLogin(driver=self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("account,pwd", [("itheima_test", "itheima")])
    def test_login(self, account, pwd):
        self.pagelogin.pagelogin(account=account, pwd=pwd)
        try:
            assert self.pagelogin.page_login_sucess_info() == "itheima_test", "用户名前后不一致"
        except Exception as ex:
            raise ex


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])
