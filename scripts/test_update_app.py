import pytest

from base.base_driver import BaseDriver
from page.page_login import PageLogin
from page.page_updateapp import PageUpdateApp


class TestLogin:
    def setup(self):
        self.driver = BaseDriver().get_driver(noReset=False)
        self.pagelogin = PageLogin(driver=self.driver)
        self.pageupdateapp = PageUpdateApp(driver=self.driver)

    def teardown(self):
        self.driver.quit()

    def test_update_app(self):
        # 判断当前是否登录，因为更改设置需要登录状态才能进行修改
        self.pagelogin.page_login_state()
        self.pageupdateapp.pageupdateapp(msg="关于百年奥莱")
        try:
            assert self.pageupdateapp.pageupdateapp_update_success() == True
            print("测试更新应用成功")
        except Exception as ex:
            print("测试更新应用失败", ex)


if __name__ == '__main__':
    pytest.main(["-s", "test_update_app.py"])
