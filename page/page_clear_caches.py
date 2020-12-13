from selenium.webdriver.common.by import By

import page
from base.base_action import BaseAction


class PageClearCaches(BaseAction):

    def pageupdateapp_tab_me(self):
        self.base_click(element=page.pageupdateapp_tab_me)

    def pageupdateapp_tab_settings(self):
        self.base_click(element=page.pageupdateapp_tab_settings)

    def pageupdateapp_swip_to_about_aolai_and_click(self, msg):
        self.base_swip_to_somewhere(msg=msg).click()

    def page_login_toast_info(self, msg):
        '''
        查找toast信息
        :param msg:
        :return:
        ''',
        page_login_toast_info = By.XPATH, "//*[contains(@text,'%s')]" % msg
        try:
            self.find_element(page_login_toast_info)
            return True
        except Exception as ex:
            raise ex("没有获取到相对应的toast信息")

    def get_toast_text(self, msg):
        """
        根据 部分内容，获取toast上的所有内容
        :param message: 部分内容
        :return: 所有内容
        """
        if self.page_login_toast_info(msg):
            message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % msg
            return self.find_element(message_xpath, 5, 0.1).text
        else:
            raise Exception("toast未出现，请检查参数是否正确或toast有没有出现在屏幕上")

    # def is_feature_exist(self, feature):
    #     try:
    #         self.find_element(feature)
    #         return True
    #     except Exception:
    #         return False

    def pageclearcaches(self, msg):
        self.pageupdateapp_tab_me()
        self.pageupdateapp_tab_settings()
        self.pageupdateapp_swip_to_about_aolai_and_click(msg)
