import page
from base.base_action import BaseAction


# 收货地址
class PageShipToAddr(BaseAction):
    # 点击我
    def pageshiptoaddr_tab_me(self):
        self.base_click(element=page.page_login_tab_me)

    # 点击设置按钮
    def pageshiptoaddr_tab_settings(self):
        self.base_click(element=page.pageupdateapp_tab_settings)

    # 点击地址管理
    def pageshiptoaddr_tab_address_management(self):
        self.base_swip_to_somewhere(msg=page.pageshiptoaddr_tab_address_management).click()

    # 点击新增地址
    def pageshiptoaddr_tab_add_address(self):
        self.base_swip_to_somewhere(msg=page.pageshiptoaddr_tab_add_address).click()

    # 输入收件人
    def pageshiptoaddr_input_recipient(self, recipient):
        self.base_send_keys(element=page.pageshiptoaddr_input_recipient, value=recipient)

    # 输入手机号
    def pageshiptoaddr_input_phone_number(self, phone_number):
        self.base_send_keys(element=page.pageshiptoaddr_input_phone_number, value=phone_number)

    # 选择所在地区
    def pageshiptoaddr_tab_location(self):
        pass

    # 输入详细地址
    def pageshiptoaddr_input_detailed_address(self, detailed_address):
        self.base_send_keys(element=page.pageshiptoaddr_input_detailed_address, value=detailed_address)

    # 输入邮编
    def pageshiptoaddr_input_postcode(self, postcode):
        self.base_send_keys(element=page.pageshiptoaddr_input_postcode, value=postcode)

    # 点击设为默认地址按钮
    def pageshiptoaddr_tab_set_as_default_addr(self):
        self.base_click(element=page.pageshiptoaddr_tab_set_as_default_addr)

    # 点击保存按钮
    def pageshiptoaddr_tab_save_btn(self):
        pass

    # 组装函数调用
    def pageshiptoaddr(self, recipient, phone_number, detailed_address, postcode):
        self.pageshiptoaddr_tab_me()
        self.pageshiptoaddr_tab_settings()
        self.pageshiptoaddr_tab_address_management()
        self.pageshiptoaddr_tab_add_address()
        self.pageshiptoaddr_input_recipient(recipient)
        self.pageshiptoaddr_input_phone_number(phone_number)
        # self.pageshiptoaddr_tab_location()
        self.pageshiptoaddr_input_detailed_address(detailed_address)
        self.pageshiptoaddr_input_postcode(postcode)
        self.pageshiptoaddr_tab_set_as_default_addr()
        # self.pageshiptoaddr_tab_save_btn()
