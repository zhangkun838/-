import pytest

from base.base_driver import BaseDriver
from page.page_login import PageLogin
from page.page_ship_to_addr import PageShipToAddr
from tools.read_data import to_para


class TestShipToAddr:
    def setup(self):
        self.driver = BaseDriver().get_driver(noReset=False)
        self.pagelogin = PageLogin(driver=self.driver)
        self.pageshiptoaddr = PageShipToAddr(driver=self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", to_para(filename="data_ship_to_addr.yaml", test_key="test_ship_to_addr"))
    def test_ship_to_addr(self, args):

        name = args["name"]
        phone = args["phone"]
        detailed_address = args["detailed_address"]
        postcode = args["postcode"]
        toast = args["toast"]

        self.pagelogin.page_login_state()
        self.pageshiptoaddr.pageshiptoaddr(recipient=name,
                                           phone_number=phone,
                                           detailed_address=detailed_address,
                                           postcode=postcode)
        try:
            if toast != None:
                # print(self.pageshiptoaddr.base_get_toast(message=toast))
                assert self.pageshiptoaddr.base_assert_toast_info(msg=toast), "保存失败，toast内容和预期不符"
            else:
                assert self.pageshiptoaddr.pageshiptoaddr_addr_same_as_before() == "%s  %s" % (
                    name, phone), "保存成功，但是未在此页面找到保存的姓名和电话，可能没有将刚才输入的地址设置为默认的"
        except Exception as ex:
            raise ex

    # 测试编辑地址功能
    def test_edit_address(self):
        # 先登录
        self.pagelogin.page_login_state()
        # 进入到收货地址管理的界面
        self.pageshiptoaddr.pageshiptoaddr_2()
        # 判断是否有收货地址，如果有就进行修改
        if self.pageshiptoaddr.pageshiptoaddr_if_address_has_one_Addr():
            self.pageshiptoaddr.pageshiptoaddr_edit_address_btn()
            self.pageshiptoaddr.pageshiptoaddr_4(recipient="哈哈哈1",
                                                 phone_number="11111111111",
                                                 detailed_address="2单元  10号",
                                                 postcode="454100")
            print(self.pageshiptoaddr.base_get_toast(message="保存成功"))
            assert self.pageshiptoaddr.pageshiptoaddr_if_edit_address_success("保存成功"), "修改可能失败了"
        #     如果没有，就添加一条地址
        else:
            self.pageshiptoaddr.pageshiptoaddr_3(recipient="天下影音",
                                                 phone_number="13273911234",
                                                 detailed_address="2单元  10号",
                                                 postcode="454100")

    # 测试删除地址的功能
    def test_del_address(self):
        # 先登录
        self.pagelogin.page_login_state()
        # 进入到收货地址管理的界面
        self.pageshiptoaddr.pageshiptoaddr_2()
        # 判断地址栏中是否有“默认”的标签，如果有代表有可以删的地址
        if self.pageshiptoaddr.pageshiptoaddr_if_have_address_to_del():
            self.pageshiptoaddr.pageshiptoaddr_edit_del_and_confirm()
            # 由于不知道有多少个地址需要删除，所以使用while循环
            while True:
                if self.pageshiptoaddr.pageshiptoaddr_if_have_address_to_del():
                    self.pageshiptoaddr.pageshiptoaddr_edit_del_and_confirm()
                else:
                    assert self.pageshiptoaddr.pageshiptoaddr_if_have_address_to_del() is False, "还有没删除完的地址"
                    break
        else:
            assert self.pageshiptoaddr.pageshiptoaddr_if_have_address_to_del() is False, "还有没删除完的地址"
            # print("没有可以删除的收货地址")


if __name__ == '__main__':
    pytest.main(["-s", "test_ship_to_addr.py"])
