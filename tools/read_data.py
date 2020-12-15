import os

import yaml


# with open(file="../data/data_login.yaml", mode="r", encoding="utf-8") as f:
#     a = yaml.load(stream=f, Loader=yaml.SafeLoader)
#     for i in a.values():
#         print(i)


def to_para(filename, test_key):
    with open(".." + os.sep + "data" + os.sep + filename, "r", encoding="utf-8") as f:
        a = yaml.load(stream=f, Loader=yaml.SafeLoader)
        data = a[test_key]
        data_list = []
        for i in data.values():
            data_list.append(i)
        return data_list


if __name__ == '__main__':
    print(to_para(filename="data_vip.yaml", test_key="test_vip"))
