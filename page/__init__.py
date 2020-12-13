from selenium.webdriver.common.by import By

"登录模块配置"
# 关闭应用更新提醒
page_login_close_update_info = By.XPATH, "//*[@content-desc='关闭对话框']"
# 点击我去登陆 账号
page_login_tab_me = By.ID, "com.yunmall.lc:id/tab_me"
# 已有账号，去登录
page_login_tab_already_have_account = By.XPATH, "//*[@text='已有账号，去登录']"
# 输入账号
page_login_input_account = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 输入密码
page_login_input_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 点击登录按钮
page_login_tab_login_btn = By.ID, "com.yunmall.lc:id/logon_button"
# 判断是否登录成功
page_login_sucess_info = By.ID, "com.yunmall.lc:id/tv_user_nikename"

"应用更新模块配置"
# 点击我去登陆 账号
pageupdateapp_tab_me = By.ID, "com.yunmall.lc:id/tab_me"
# 点击应用的设置按钮
pageupdateapp_tab_settings = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 滑动到底部点击关于百年奥莱
pageupdateapp_swip_to_about_aolai_and_click = By.XPATH, "//*[@text='关于百年奥莱']"
# 点击升级更新应用按钮
pageupdateapp_tab_update_btn = By.XPATH, "//*[@text='版本更新']"

"成为会员模块配置"
pagejoinvip_tab_join_vip = "加入超级VIP"
pagejoinvip_input_verification_code = By.XPATH, "//*[@type='tel']"
pagejoinvip_tab_become_vip = By.XPATH, "//input[@value='立即成为会员']"
