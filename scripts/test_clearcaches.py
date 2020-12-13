import pytest

from base.base_driver import BaseDriver
from page.page_clear_caches import PageClearCaches
from page.page_login import PageLogin


class TestLogin:
    def setup(self):
        # 再base_driver中设置一个默认的参数，在这里调整就可以选应用不在重置
        self.driver = BaseDriver().get_driver(noReset=False)
        self.pagelogin = PageLogin(driver=self.driver)
        self.clearcaches = PageClearCaches(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_clearcaches(self):
        self.pagelogin.page_login_state()
        try:
            self.clearcaches.pageclearcaches(msg="清理缓存")
            print(self.clearcaches.get_toast_text(msg="清理缓存"))
            assert self.clearcaches.get_toast_text(msg="清理缓存")
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    pytest.main(["-s", "test_clearcaches.py"])
