## 环境配置
1. Windows10
2. visual studio code
3. python 3.8


## 作业需求
上次作业使用了newton法实现开平方，这次作业要求使用其他方法，实现开二次方和三次方，需要使用基类接口，并利用继承类完成创建。

使用课件二中 Singleton(单体)、SimpleFactory、FactoryMethod 三种设计模式(Design Pattern)来得到这种开方多个实例。

加法项使用AbstractFactory模式。

## 作业分析
1. 定义基类接口文件
2. 编写基本要求中的三种设计模式，分为三种文件。
3. 完成加分项

### python中的基类接口和继承类
在想面向对象中，基类就是父类，是被继承的类，继承这个父类的类，被称为子类，一个子类可以继承多个父类，但是一般情况下，一个子类只能有一个基类，如果要实现多重继承，就需要通过多级继承来实现。

### Singleton(单例设计模式)设计模式
单例模式属于创造性设计模式，保证一个类只有一个实例，并提供一个访问该实例的全局节点。

python的模块就是天然的单例模式，因为模块在第一次导入的时候，会产生.pyc文件，当二次导入的时候，就会直接加载.pyc文件，不会再执行模块代码，所以只需要把相关函数和数据定理在一个模块中，就可以获得一个单例对象。

### SimpleFactory 设计模式