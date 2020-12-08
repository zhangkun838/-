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
