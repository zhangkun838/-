import pytest

from base.base_driver import BaseDriver
from page.page_join_vip import PageJoinVip
from page.page_login import PageLogin
from tools.find_keyword import FindKeyWord
from tools.read_data import to_para


class TestJoinVip:
    def setup(self):
        self.driver = BaseDriver().get_driver(noReset=False)
        self.pagelogin = PageLogin(driver=self.driver)
        self.pagejoinvip = PageJoinVip(driver=self.driver)
        self.findkeyword = FindKeyWord(driver=self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", to_para(filename="data_vip.yaml", test_key="test_vip"))
    def test_join_vip(self, args):
        keyword = args["keyword"]
        expect = args["expect"]
        # 如果没有登陆 必须要有先登录
        self.pagelogin.page_login_state()
        # 组合方分为了两个部分
        self.pagejoinvip.pagejoinvip_1()
        # 切换到浏览器的环境
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        # 发送验证码
        self.pagejoinvip.pagejoinvip_2(value=keyword)
        try:
            # 断言"邀请码输入不正确" 是否存在，如果存在就代表没有成为VIP
            assert self.findkeyword.is_key_word_exit_in_page_source(key_word=expect)
        except Exception as ex:
            raise ex

        self.driver.switch_to.context("NATIVE_APP")


if __name__ == '__main__':
    pytest.main(["-s", "test_join_vip.py"])