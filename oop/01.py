"""
定义一个学生类
用来形容学生
"""
# 定义一个空的类


class Student:
    # 一个空类，pass必须有，代表跳过
    pass


# 定义一个对象
my = Student()


class PythonStudent:
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = 'python'

    # 需要注意
    # 1.def do_homework的缩进层级
    # 2.系统默认有一个self参数
    @staticmethod
    def do_homework():
        print('i am doing homework')

        # 推荐函数末尾使用return语句
        return None


# 实例化
yue = PythonStudent()
print(yue.name)
print(yue.age)
# 注意成员函数的调用没有传入参数
yue.do_homework()
