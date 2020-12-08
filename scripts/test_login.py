import pytest

from base.base_driver import BaseDriver


class TestLogin:
    def setup(self):
        self.driver = BaseDriver().get_driver()

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        print("运行百年奥莱！")


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])
