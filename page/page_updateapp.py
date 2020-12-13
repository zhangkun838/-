from base.base_action import BaseAction
import page


class PageUpdateApp(BaseAction):

    def page_login_close_update_info(self):
        self.base_click(element=page.page_login_close_update_info)

    def pageupdateapp_tab_me(self):
        self.base_click(element=page.pageupdateapp_tab_me)

    def pageupdateapp_tab_settings(self):
        self.base_click(element=page.pageupdateapp_tab_settings)

    def pageupdateapp_swip_to_about_aolai_and_click(self, msg):
        self.base_swip_to_somewhere(msg=msg).click()

    def pageupdateapp_tab_update_btn(self):
        self.base_click(element=page.pageupdateapp_tab_update_btn)

    def pageupdateapp_update_success(self):
        if self.find_element(element=page.page_login_close_update_info):
            return True
        else:
            return False

    def pageupdateapp(self, msg):
        # self.page_login_close_update_info()
        self.pageupdateapp_tab_me()
        self.pageupdateapp_tab_settings()
        self.pageupdateapp_swip_to_about_aolai_and_click(msg)
        self.pageupdateapp_tab_update_btn()
