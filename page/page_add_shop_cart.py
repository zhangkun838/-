# 收货地址
import random
from time import sleep

import page
from base.base_action import BaseAction


class PageAddShopCart(BaseAction):
    # 点击分类
    def pageaddshopcart_tab_classification(self):
        self.base_click(element=page.pageaddshopcart_tab_classification)

    # 随机点击一个商品分类
    def pageaddshopcart_add_commodity_Randomly(self):
        all_commodity_classification = self.find_elements(
            element=page.pageaddshopcart_add_commodity_Randomly)
        index = random.randint(a=0, b=len(all_commodity_classification) - 1)
        all_commodity_classification[index].click()
        sleep(2)

    # 随机点击一个商品
    def pageaddshopcart_tab_add_goods_to_cart_Randomly(self):
        all_commodity = self.find_elements(
            element=page.pageaddshopcart_tab_add_goods_to_cart_Randomly)
        index = random.randint(a=0, b=len(all_commodity) - 1)
        all_commodity[index].click()
        sleep(2)

    # 点击加入购物车按钮
    def pageaddshopcart_tab_add_to_cart(self):
        self.base_click(element=page.pageaddshopcart_tab_add_to_cart)

    # 点击商品的颜色分类
    def pageaddshopcart_tab_color_classification(self):
        pass

    # 选择商品规格
    def pageaddshopcart_tab_specification(self):
        pass

    # 点击购买数量
    def pageaddshopcart_tab_purchase_quantity(self):
        pass

    # 点击确定购买
    def pageaddshopcart_tab_confirm_btn(self):
        pass

    # 组装函数
    def pageaddshopcart(self):
        self.pageaddshopcart_tab_classification()
        self.pageaddshopcart_add_commodity_Randomly()
        self.pageaddshopcart_tab_add_goods_to_cart_Randomly()
        self.pageaddshopcart_tab_add_to_cart()
        # self.pageaddshopcart_tab_color_classification()
        # self.pageaddshopcart_tab_specification()
        # self.pageaddshopcart_tab_purchase_quantity()
        # self.pageaddshopcart_tab_confirm_btn()
