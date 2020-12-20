import random
from time import sleep

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
        self.base_click(element=page.pageshiptoaddr_tab_location)

    # 选择省市区
    def pageshiptoaddr_tab_provinces_and_municipalities(self):
        self.pageshiptoaddr_tab_location()
        while True:
            if self.driver.current_activity == "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                # 获取所有的可选的省市区
                all_provinces_and_municipalities = self.find_elements(
                    element=page.pageshiptoaddr_tab_provinces_and_municipalities)
                # 随机选取一个城市，当作收件地址的城市 ； 比如获取到的城市数量是10，所以就是10个当中随机选一个， 而random.randint 是从0开始计数的，0. 1 . 2 开始算不减1就多算了一个
                index = random.randint(a=0, b=len(all_provinces_and_municipalities) - 1)
                # 获得随机城市之后点击
                all_provinces_and_municipalities[index].click()
                sleep(2)
            else:
                break

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
        self.base_click(element=page.pageshiptoaddr_tab_save_btn)

    # 增加收货地址之后的断言
    def pageshiptoaddr_addr_same_as_before(self):
        return self.base_get_text_info(element=page.pageshiptoaddr_addr_same_as_before)

    # 查看地址栏中是否已经存有地址
    def pageshiptoaddr_if_address_has_one_Addr(self):
        return self.base_is_element_existence(element=page.pageshiptoaddr_if_address_has_one_Addr)

    # 点击编辑按钮修改地址
    def pageshiptoaddr_edit_address_btn(self):
        self.base_click(element=page.pageshiptoaddr_if_address_has_one_Addr)

    # 断言是否修改成功
    def pageshiptoaddr_if_edit_address_success(self, toast):
        return self.base_assert_toast_info(msg=toast)

    # 判断是否有地址可以进行删除
    def pageshiptoaddr_if_have_address_to_del(self):
        return self.base_is_element_existence(element=page.pageshiptoaddr_if_address_has_one_Addr)

    # 点击编辑按钮
    def pageshiptoaddr_tab_edit_btn(self):
        self.base_click(element=page.pageshiptoaddr_tab_edit_btn)

    # 点击删除按钮
    def pageshiptoaddr_tab_del_btn(self):
        self.base_click(element=page.pageshiptoaddr_tab_del_btn)

    def pageshiptoaddr_tab_confrim_del_btn(self):
        self.base_click(element=page.pageshiptoaddr_tab_confrim_del_btn)

    # 组装函数调用
    def pageshiptoaddr(self, recipient, phone_number, detailed_address, postcode):
        self.pageshiptoaddr_tab_me()
        self.pageshiptoaddr_tab_settings()
        self.pageshiptoaddr_tab_address_management()
        self.pageshiptoaddr_tab_add_address()
        self.pageshiptoaddr_input_recipient(recipient)
        self.pageshiptoaddr_input_phone_number(phone_number)
        self.pageshiptoaddr_tab_provinces_and_municipalities()
        self.pageshiptoaddr_input_detailed_address(detailed_address)
        self.pageshiptoaddr_input_postcode(postcode)
        self.pageshiptoaddr_tab_set_as_default_addr()
        self.pageshiptoaddr_tab_save_btn()
        sleep(3)

    def pageshiptoaddr_2(self):
        self.pageshiptoaddr_tab_me()
        self.pageshiptoaddr_tab_settings()
        self.pageshiptoaddr_tab_address_management()

    def pageshiptoaddr_3(self, recipient, phone_number, detailed_address, postcode):
        self.pageshiptoaddr_tab_add_address()
        self.pageshiptoaddr_input_recipient(recipient)
        self.pageshiptoaddr_input_phone_number(phone_number)
        self.pageshiptoaddr_tab_provinces_and_municipalities()
        self.pageshiptoaddr_input_detailed_address(detailed_address)
        self.pageshiptoaddr_input_postcode(postcode)
        self.pageshiptoaddr_tab_set_as_default_addr()
        self.pageshiptoaddr_tab_save_btn()
        sleep(3)

    def pageshiptoaddr_4(self, recipient, phone_number, detailed_address, postcode):
        self.pageshiptoaddr_tab_add_address()
        self.pageshiptoaddr_input_recipient(recipient)
        self.pageshiptoaddr_input_phone_number(phone_number)
        self.pageshiptoaddr_tab_provinces_and_municipalities()
        self.pageshiptoaddr_input_detailed_address(detailed_address)
        self.pageshiptoaddr_input_postcode(postcode)
        self.pageshiptoaddr_tab_save_btn()

    def pageshiptoaddr_edit_del_and_confirm(self):
        self.pageshiptoaddr_tab_edit_btn()
        self.pageshiptoaddr_tab_del_btn()
        self.pageshiptoaddr_tab_confrim_del_btn()
