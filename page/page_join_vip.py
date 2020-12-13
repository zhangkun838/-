from time import sleep

from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import page


class PageJoinVip(BaseAction):
    # 点击我
    def pagejoinvip_tab_me(self):
        self.base_click(element=page.page_login_tab_me)

    # 点击加入超级会员按钮
    def pagejoinvip_tab_join_vip(self):
        self.base_swip_to_somewhere(page.pagejoinvip_tab_join_vip).click()

    # 输入验证码
    def pagejoinvip_input_verification_code(self, value):
        self.base_send_keys(element=page.pagejoinvip_input_verification_code, value=value)

    # 点击成为会员
    def pagejoinvip_tab_become_vip(self):
        self.base_click(element=page.pagejoinvip_tab_become_vip)

    def pagejoinvip_get_toast_info(self, msg):
        '''
        查找toast信息
        :param msg:
        :return:
        ''',
        page_login_toast_info = By.XPATH, "//*[contains(@text,'%s')]" % msg
        try:
            return self.base_get_text_info(element=page_login_toast_info)
        except Exception as ex:
            raise ex("没有获取到相对应的toast信息")

    def pagejoinvip_1(self):
        self.pagejoinvip_tab_me()
        self.pagejoinvip_tab_join_vip()
        sleep(3)

    def pagejoinvip_2(self, value):
        self.pagejoinvip_input_verification_code(value=value)
        self.pagejoinvip_tab_become_vip()
        sleep(3)
