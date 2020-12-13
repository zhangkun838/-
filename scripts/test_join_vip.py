from time import sleep

import pytest

from base.base_driver import BaseDriver
from page.page_join_vip import PageJoinVip
from page.page_login import PageLogin


class TestJoinVip:
    def setup(self):
        self.driver = BaseDriver().get_driver(noReset=False)
        self.pagelogin = PageLogin(driver=self.driver)
        self.pagejoinvip = PageJoinVip(driver=self.driver)

    def teardown(self):
        self.driver.quit()

    def test_join_vip(self):
        # 如果没有登陆 必须要有先登录
        self.pagelogin.page_login_state()
        # 组合方分为了两个部分
        self.pagejoinvip.pagejoinvip_1()
        # 切换到浏览器的环境
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        # 发送验证码
        self.pagejoinvip.pagejoinvip_2(value="1111")
        self.driver.switch_to.context("NATIVE_APP")

        # try:
        #     pass
        #     # 断言是否正确
        #     # assert self.pagejoinvip.pagejoinvip_get_toast_info(msg="邀请码输入不正确") == "邀请码输入不正确"
        #     # sleep(3)
        #     # 切换回原来的环境
        #     self.driver.switch_to.context("NATIVE_APP")
        # except Exception as ex:
        #     raise ex


if __name__ == '__main__':
    pytest.main(["-s", "test_join_vip.py"])
