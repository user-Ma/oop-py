
# 包举例
# 一个类
# 一个say_hello函数
# 一个打印语句


class Student:
    def __init__(self, name="Noname", age=18 ):
        self.name = name
        self.age = age

    def say(self):
        print("my name is {0}, i am {1}.".format(self.name, self.age))


def say_hello():
    print("Welcome!")


# 此判断语句建议作为程序的入口
if __name__ == '__main__':
    # 文件单独执行时，执行下列语句；文件作为模块引用时，不执行
    print("i am module 01")
