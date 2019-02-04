1.模块（module）
    
    - 一个模块是一个包含Python代码的文件(.py)
    - 增加代码重复利用的方式；当做命名空间使用，避免命名冲突
    - 根据模块的规范，最好书写
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务的模块）
        - 测试代码
    - 使用模块
        - 模块直接导入
            - 加入模块名称直接以数字开头：借助于importlib包可以实现导入名称以数字开头的模块
        - 语法
            import module_name
            module_name.function_name
            module_name.class_name
            
            import 模块 as 别名
        - from module_name import func_name, class_name
            - 有选择性地导入
            - 不需要前缀
        - from module_name import *
            导入所有，但是不需要写前缀
            
        -# 此判断语句建议作为程序的入口：有效解决模块代码被导入时被动执行的问题
            if __name__ == '__main__':
            
2.模块的搜索路径和存储
    
    -搜索路径：加载模块时搜寻
    -系统默认的模块搜索路径：
        import sys
        sys.path  # 属性可以获取路径列表
    - 添加搜索路径
        sys.path.append(dir)
    -模块的加载顺序
        1.先搜索内存中已经加载好的模块
        2.搜索Python的内置模块
        3.搜索sys.path路径
        
3.包
    
    - 一种组织管理代码的方式，包里面存放的是模块（将模块包含在一起的文件夹）
    - 自定义包的结构
        /---包
        /---/--- __init__.py 包的标志文件
        /---/--- 模块1
        /---/--- 模块2
        /---/--- 子包（子文件夹）
        /---/---/--- __init__.py 包的标志文件
        /---/---/--- 子包模块1
        /---/---/--- 子包模块2
    -包的导入操作
        import package_name
            - 直接导入一个包，可以使用__init__.py的内容
            - 使用方式：
                package_name.func_name
                package_name.class_name.func_name()
            - 这种方式的访问内容
        import package_name as p
        - 注意这种简单导入默认是对__init__.py 的导入
        
        import package.module
            - 导入包中某一个具体的模块
                package.module.func_name
                package.module.class.func()
                package.module.class.var
        import package.module as pm
        
        from package import module1, module2, module3....
            -此种方法不执行'__init__'的内容
                from pkg01 import p01
                p01.say_hello()
        from package import *
            - 导入当前包'__init__.py'文件中所有的函数和类
            - 使用
                func_name()
                class_name.func_name()
                class_name.var
        from package.module import *
            - 导入包中指定模块的所有内容
            - 使用方法
                func_name()
                class_name.func_name()
        - 在开发环境中经常会使用其他模块，可以在当前包中直接导入其他模块内容
            import 完整的包或者模块的路径
            
        -`__all__`的用法
            - 在使用from package import * 的时候，* 可以导入的内容
            - `__init__.py`中如果文件为空，或者没有`__all__`,那么默认是只把`__init__`的内容导入
            -`__init__`若设置了`__all__`的值，那么按照`__all__`指定的模块或子包进行加载，如此则不会载入`__init__`的所有内容
            
            __all__ = [`module1`,`module2`,`package1`, ...]
            
4.命名空间
    
    -区分不同位置不同功能但名称相同的函数或者变量的一个特定前缀，防止命名冲突
        set_name()
        Student.set_name()
        Dog.set_name()
            
            
                           