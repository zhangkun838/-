import time

from base.base_action import BaseAction


class FindKeyWord(BaseAction):
    def is_key_word_exit_in_page_source(self, key_word="邀请码输入不正确", t=10, interval_time=0.1):
        """
        :param self:
        :param t: 搜索关键字的时长，限定的时间
        :param interval_time: 查找关键字的间隔时间
        :param key_word: 要查找的关键字
        :return: 如果找到了就返回 True ,没找到就返回 False
        """
        # 限定的时间
        timeout = time.time() + t
        while True:
            # time.time()表示当前的时间 ；如果结束时间大于当前时间，那么就认为超时了
            if time.time() > timeout:
                print("超时，没有找到提示信息：%s" % key_word)
                return False
            # 如果结束时间不大于当前时间，继续轮询
            else:
                if key_word in self.driver.page_source:
                    print("找到提示信息：%s" % key_word)
                    return True
                # else:
                #     print("页面中没有包含邀请码输入不正确的字符串")
            # 利用time.sleep设置查询的频率
            time.sleep(interval_time)
