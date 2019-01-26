关于pycharm工作窗口无法编辑.md文件的解决办法:
    
    -原因是安装了扩展vim编辑器，pycharm在编写代码时默认使用vim编辑
    -'Tools'关闭Vim Emulator

0.OOP-Python面向对象
    
    -基础
    -公有私有
    -继承
    -组合，Mixin
    -魔法函数
        -概述
        -构造类、运算类

1.面向对象（ObjectOriented, OO）
    
    -OOP思想：任务由模型构成
    -OO 面向对象；
    -OOA 面向对象的分析；
    -OOD 面向对象的设计；
    -OOI 面向对象的实现；
    -OOP面向对象的编程

2.类和对象的概念
    
    -类：集合，共性的事物
    -对象：具象的事物，某类事物单个个体
    -类包括两个内容
        -表明事物的特征，即属性---变量
        -表明事物的功能或动作，即成员方法---函数
        
3.类的基本实现
    
    -类的命名
        -命名规范 大驼峰 避免和系统命名相似的命名
    -声明一个类
        -关键字 class
        -类由属性和方法构成，其他不允许出现
        -成员属性定义可以直接使用变量赋值，没有值允许使用None
        -案例 01.py
    -实例化类
        变量 = 类名（）#实例化一个对象
    -访问对象成员
        -使用点操作符
            obj.成员属性名称
            obj.成员方法
    -可以通过默认内置变量检查类和对象的所有成员
        -对象所有成员检查：dict前后各有两个下划线
            obj,__dict__
        -类所有的成员
            class_name.__dict__
   
4.anaconda基本使用
    
    -虚拟环境管理器、安装包管理器
    -conda list：显示anaconda安装的包
    -conda env list：显示anaconda的虚拟环境列表
    
    Anaconda Prompt
    conda create -n xxx python=3.7 #创建Python版本为3.7的虚拟环境，名称为xxx oop
    conda activate xxx #进入虚拟环境
    #e.g.在环境中安装名为TensorFlow的软件
    pip install tensorflow  或者
    pip install -ignore-installed -upgrade tensorflow
    #查看虚拟环境在哪个安装目录下
    conda env list
    
    #pycharm使用虚拟环境
    File->settings->Project:xxxx->Project Interperter
    Anaconda3\envs\xxx\python.ext
    
5.警告解决
    
    Python  pycharm 波浪线警告：block comment should start with #
    错误原因：应该在注释的#号之后加上一个空格。
    
    警告：Triple double-quoted strings should be used for docstrings.
    换成
    """
    ......
    :param xx:
    :return:
    """
    警告：Remove redundant parentheses：将该处的小括号删除
    
    警告：Method xxx may be 'static'：该方法不涉及对该类属性的操作
    编译器建议声明为@staticmethod，面向对象思想体现
    
6.python的@classmethod和@staticmethod
    
    -Python面向对象编程中，类中定义的方法可以是@classmethod 装饰的类方法，也可以
    是@staticmethod 装饰的静态方法，用的最多的还是不带装饰器的实例方法。
    
    -@classmethod和@staticmethod很相似，它们装饰的方法在使用上只有一点区别：
    @classmethod装饰的方法第一个参数必须是一个类（通常为cls），
    @staticmethod装饰的方法则按业务需求设置参数，也可以根本没有参数。
    
    e.g.处理日期信息的类：
    class Date(object):
        def __init__(self, day=0, month=0, year=0)
            self.day = day
            self.month = month
            self.year = year
    # 存储指定日期，__init__函数初始化实例对象，第一个必须参数self指向一个已创建的Date类实例对象
    @classmethod 完成：
        -堆有着特定日期格式的字符串（如'dd-mm-yyyy'）创建很多对应的Date类的实例
        -在项目的各个地方都要进行这样的转换
        -我们要做的是：
            -解析一个字符串来得到day,month,year这三个整数变量或者组装出一个tuple
            -把这些值传递给初始化函数来实例化Date实例对象
        @classmethod
        def from_string(cls, date_as_string):   
            day, month, year = map(int, string_date.split('-'))
            date1 = cls(day, month, year) 
            return date1
    date2 = Date.form_string('11-09-2012')
    
    @staticmethod 完成：
        -检验一个日期的字符串是否有效
        -与Date类相关，又不需要Date实例对象，此时@staticmethod可以派上用场。
        @staticmethod
        def is_date_valid(date_as_string):
            day, month, year = map(int, date_as_string.split('-'))
            return day <= 31 and month <= 12 and year <= 3999
    is_date = Date.is_date_valid('11-09-2012)        
        
    