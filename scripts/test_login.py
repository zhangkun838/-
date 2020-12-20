import pytest

from base.base_driver import BaseDriver
from page.page_login import PageLogin
from tools.read_data import to_para


class TestLogin:
    def setup(self):
        # 再base_driver中设置一个默认的参数，在这里调整就可以选应用不在重置
        self.driver = BaseDriver().get_driver(noReset=False)
        self.pagelogin = PageLogin(driver=self.driver)

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.parametrize("account,pwd",
    #                          [("itheima_test", "itheima"), ("itheima_test123", "itheima"), ("itheima_test", "123")])
    # @pytest.mark.parametrize("account,pwd",
    #                          [("itheima_test", "itheima")])

    @pytest.mark.parametrize("args", to_para(filename="data_login.yaml", test_key="test_ship_to_addr"))
    def test_login(self, args):
        # 解析yaml数据
        account = args["account"]
        pwd = args["pwd"]
        toast = args["toast"]
        self.pagelogin.pagelogin(account=account, pwd=pwd)

        try:
            if toast is None:
                print("\n", self.pagelogin.page_login_sucess_info())
                assert self.pagelogin.page_login_sucess_info() == "itheima_test", "用户名前后不一致"
            else:
                print("获取应用的提示信息：", self.pagelogin.page_login_toast_info(msg=toast))
                print("data_login.yaml的toast信息：", toast)
                assert self.pagelogin.page_login_toast_info(msg=toast) == toast

        except Exception as ex:
            raise ex

    # 测试登录状态函数
    def test_login_state(self):
        self.pagelogin.page_login_state()


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])
