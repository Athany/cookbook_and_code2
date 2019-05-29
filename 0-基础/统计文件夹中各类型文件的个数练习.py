# -*- coding:utf-8 -*-
import os

# 获取到当前文件夹下面所以的文件 os.curdir 表示当前目录curdir：currentdirectory
all_files = os.listdir(os.curdir)  # os.curdir的使用 https://www.runoob.com/python/os-listdir.html

type_dict = dict()  # ={}      # dict()的使用 https://www.runoob.com/python/python-func-dict.html

for each_file in all_files:
    # 如果说我们的each_file是文件夹
    if os.path.isdir(each_file):
        type_dict.setdefault("文件夹", 0)  # Python 字典 setdefault() 函数和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
        # https://www.runoob.com/python/att-dictionary-setdefault.html

        type_dict["文件夹"] += 1

    else:
        # 如果不是文件夹，而是文件，统计文件数
        ext = os.path.splitext(each_file)[1]  # 获取到文件的后缀 https://blog.csdn.net/zzc15806/article/details/81352742
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1

for each_type in type_dict:
    print("该文件夹下面有类型为{0}的文件{1}个。".format(each_type, type_dict[each_type]))