from time import sleep

from base.base_action import BaseAction
import page


class PageLogin(BaseAction):
    # 点击我去登陆 账号
    def page_login_tab_me(self):
        self.base_click(element=page.page_login_tab_me)

    # 点击已有账号，去登录
    def page_login_tab_already_have_account(self):
        self.base_click(element=page.page_login_tab_already_have_account)

    # 输入账号
    def page_login_input_account(self, account):
        self.base_send_keys(element=page.page_login_input_account, value=account)

    # 输入账号
    def page_login_input_pwd(self, pwd):
        self.base_send_keys(element=page.page_login_input_pwd, value=pwd)

    # 点击登录按钮
    def page_login_tab_login_btn(self):
        self.base_click(element=page.page_login_tab_login_btn)

    # 关闭应用更新提醒
    def page_login_close_update_info(self):
        self.base_click(element=page.page_login_close_update_info)

    # 判断是否登录成功
    def page_login_sucess_info(self):
        return self.base_get_text_info(element=page.page_login_sucess_info)

    # 组合方法
    def pagelogin(self, account, pwd):
        self.page_login_close_update_info()
        self.page_login_tab_me()
        self.page_login_tab_already_have_account()
        self.page_login_input_account(account=account)
        self.page_login_input_pwd(pwd=pwd)
        self.page_login_tab_login_btn()
        sleep(3)
