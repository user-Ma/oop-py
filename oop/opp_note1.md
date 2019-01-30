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
        
7.类和对象的成员分析
    
    -类和对象都可以存储成员
    -类存储成员时使用的是与类关联的一个对象
    -对象存储成员时存储于当前对象中
    -对象访问一个成员时，若对象中没有该成员，尝试访问类中同名成员；有此成员一定使用此成员
    -创建对象时，类中的成员不会放入对象中，是得到一个没有成员的空对象
    -通过对象对类中成员重新赋值或者通过对象添加成员，对应成员保存在对象中，不会修改类成员
    
8.关于self
    
    -self在对象的方法中表示当前对象本身
    -如果通过对象调用一个方法，该对象会自动传入当前方法的第一个参数中
    -self不是关键字，是一个用于接收对象的普通参数
    
    -方法中有self形参的方法称为非绑定类的方法，可以通过对象访问；
    -没有self是绑定类方法，只能通过类访问
    
    -使用类访问绑定类的方法时，若类方法中需要访问当前类的成员，可以通过__class__成员名

9.面向对象的三大特性
    
    -1.封装
        -对对象成员进行访问限制
        -封装的三个级别：
            -公开 public
            -受保护的 protected
            -私有的 private
        -这三个不是关键字
        -判别对象的位置（访问位置）
            -对象内部
            -对象外部
            -子类中
        -私有
            -私有成员时是最高级别的封装，只能在当前类或对象中访问
            -在成员前面添加 __ 
                class Person:
                    # name是共有的成员
                    name = "liu"
                    # __age是私有成员
                    __age = 18
            -python中私有不是真私有，是一种称为name mangling的改名策略
            -可以使用对象._classaname_attributename访问
        -受保护的封装 protected
            -将对象成员进行一定级别的封装，在类中或子类中都可以进行访问，但是在外部不可以
            -封装方法：成员名称前添加一个下划线 _
        -公开的 public
            -公共的封装实际对成员没有任何操作，任何位置都可以访问
    
    -2.继承
        -即一个类可以获得另外一个类中的成员属性和成员方法
        -减少代码，增加代码的复用功能；可设置类与类的之间的关系
        -继承与被继承：一定存在一个 is-a 关系
            -被继承的类叫父类，基类，超类
            -用于继承的类，叫子类，派生类
        -继承的特征：
            -所有的类都继承自object类
            -子类一旦继承父类，可使用父类中除私有成员外的所有内容
            -子类继承父类后没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
            -子类可定义独有的成员属性和方法
            -子类中定义的成员若和父类成员相同，优先使用子类成员
            -子类如果想扩充父类的方法，可在定义新方法的同时访问父类成员来进行代码调用
        -可使用 [父类名.父类成员] 的格式调用父类成员，也可用[super().父类成员]的格式调用
        -继承变量函数的查找顺序问题
            -优先查找自己的变量
            -没有则查找父类
            -构造函数若本类中没有定义，则自动查找调用父类构造函数；一旦找到，不再向上查找
                -构造函数：一类特殊的函数，在类进行实例化时系统自动调用对实例对象进行初始化；一定有参数（self）
            -父类构造函数带参数时，构造对象时参数按父类参数构造
        
        -super
            -不是关键字，是一个类 class'type'
                class super(object)
            -super的作用是获取MRO（MethodResolutionOrder）列表中的第一个类
            -super与父类没有实质性关系，但通过super可以调用父类
        
        -单继承和多继承
            -优缺点：单继承--传承有序，逻辑清晰，语法简单；功能只能在当前唯一的继承链中扩展
            -多继承：类的功能扩展方便；继承关系混乱（一般不使用）
            
            -菱形继承、钻石继承问题
                -多个子类继承自同一个父类，而这些子类被同一个类继承，继承关系图形成一个菱形图谱
                -[MRO](cnblogs.com/whatisfantasy/...)
                
                -关于多继承的MRO：多继承中，用于保存继承顺序的一个列表；
                    -Python采用C3算法来 保存 多继承的菱形继承进行计算的结果
                    -MRO列表计算原则：
                        -子类永远在父类之前
                        -多个父类时，根据继承语法中括号内的类的书写顺序
                        -多个类继承了同一个父类，孙子类中只会选取继承语法括号中第一个父类的父类
            
    -多态
        -同一个对象在不同情况下有不同的状态出现
        -多态不是语法，是一种设计思想
        -多态性：一种调用方式，不同执行效果
        
        -Mixin设计模式
            -主要采用多继承方式对类的功能进行扩展（功能的增加）
            -使用继承语法来实现Mixin，使用Mixin实现多继承时：
                -必须表示某一单一功能，而不是某个物品
                -Mixin不能依赖于子类的实现
                -子类即使没有继承这个Mixin类，也能工作，只是缺少一个功能
            -优点：
             可在不对类进行任何修改的情况下扩充功能；组织和维护不同功能组件的划分；
             避免创建很多新的类
            
10.类相关函数

    -issubclass:检测一个类是否是另一个类的子类
    -isinstance:检测一个对象是否是一个类的实例
    -hasattr:检测一个对象是否有成员xxx
    -getattr
    -setattr
    -delattr
    -dir:获取对象的成员列表
    
11.类的成员描述符