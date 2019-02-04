import p01  # 相当于粘贴模块的内容并运行一遍

stu = p01.Student("xiao", 19)

stu.say()

p01.say_hello


# 借助importlib包可以实现导入名称以数字开头的模块
import importlib

# 相当于导入名为01的模块并把导入模块赋值给Turing
Turing = importlib.import_module("01")

stu = Turing.Student("xu", 89)
stu.say()

"""
# as用法
import p01 as p

stu = p.Student("yue", 18)
stu.say()

"""
