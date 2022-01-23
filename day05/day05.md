### let



- 变量不能重复声明（var可以）

- 块级作用域，只在代码块里有效（if else while for {} )

- 不存在变量提升：var有声明提前，在定义之前使用会输出undefined，不会报错。而let不行，在声明前使用会报错。

- 不影响作用域链，如：一个函数是使用某个变量但作用域内没有，会往上找

- 常用于for 或 if 之类的结构中。（因为某些情况下用var会报错）

- 在for循环中，let效果实际上是利用了闭包的机制，并且，对于循环块中的let 和 执行块中的let是两个块中分别定义的变量，互不影响。

- ~~~js
  //声明变量
  let a;
  let b,c,d;;
  let e = 100;
  ~~~

  ### const

- const 是在let 的基础上添加了一个**只读**属性，即变量一旦声明过后就不允许在修改，这里是不允许修改定义的地址，而不是不可以修改他内部的属性值。

- 也就是说对于数组和对象的属性修改，不算做对常量的修改，不会报错

- 一定要赋初始值，一般常量使用大写。块级作用域。

  ~~~js
  const obj = {name: 'aaa'}
  obj.name = 'bbb'
  ~~~

- 在使用上，不要使用var，主要使用 const 并配合着 let 使用

### 变量解构赋值

- 允许按照一定模式从数组和对象中提取值，对变量进行赋值

  ~~~javascript
  const zhao = {
      name:'白敬亭',
      age:'不详',
      xiaopin:function(){
          console.log("我可以当演员");
      }
  }
  let{xiaopin} = zhao;
  xiaopin();//这样如果要重复使用的话就不用zhao.xiaopin()了可以简略一点
  ~~~

  ### 字符串

  引入新的声明字符串的方式``

  内容中可以直接出现换行符             变量拼接

  ~~~javascript
  let str = `<ul>
  				<li>123<li>
  				<li>00<li>
  				</ul>`;
  let lovest = '白敬亭';
  let out = `${是大帅哥}`;
  console.log(out);//输出的内容：白敬亭是大帅哥
  ~~~

  

  ### 数值


  
  

  ### 数组


  
  

  ### 对象扩展

  ##### 对象的简化写法：

  允许在大括号里面，直接写入变量和函数，作为对象的属性和方法，这样的书写更加简洁

  ~~~javascript
  let name = 'hhhh';
  let change = function(){
      console.log('xxxxxx');
  }
  const school = {
      name,
      change,
      improve(){
          console.log("kkkkkk")//把function省略了
      }
  }
  ~~~

  对象声明时，如果属性值与变量名相同，可以直接把变量放过来

  ### 



###  箭头函数

允许使用[箭头]  （=>）定义函数

this是静态的，this始终指向函数声明时所在作用域下的this的值

不能作为构造实例化对象

不能使用arguments变量

简写：（1）可省略小括号，当形参有且只有一个的时候

（2）省略花括号，当代码体只有一条语句的时候，此时return必须省略。而且语句的执行结果就是函数的返回值。

`let pow = n => n * n;`

`console.log(pow(8));`

##### 应用：

适合于与this无关的回调，如：定时器，数组的方法回调

不适合事件的回调，对象的方法等。

### Symbol

一种新的原始数据类型，表示独一无二的值。

创建symbol

`let s = Symbol();`                  括号里面的东西只是一个说明、标志，不是参数。括号里面的东西一样的symbol不相等

`let s4 = Symbol.for('hhhh');`

不能与其他数据进行运算

##### 应用：

安全地向对象中添加方法，不会担心重名

~~~javascript
let youxi = {
    name:"狼人杀"
    [Symbol('say')]:function(){
        console.log("我可以发言")
    },
        [Symbol('zibao')]:function(){
            console.log('我可以自爆');
        }
}
~~~

还有很多内置属性

### Set 和 Map 数据结构

### Proxy 和 Reflect（目前阶段了解）

### Promise & async / await 异步编程

### Generator 函数异步编程（目前阶段了解）

###  Class类

~~~javascript
class Phone{
    constructor(band,price){
        this.band = band;
        this.price = price;
    }
    call(){
        console.log("我可以打电竞")
    }
    let onePlus = new Phone("1+",1999);
}
~~~

static标注的属性和方法属于类而不属于对象

class的类继承性、重写

###  Module模块

**import()**：动态导入(返回`Promise`)

- 背景：`import命令`被JS引擎静态分析，先于模块内的其他语句执行，无法取代`require()`的动态加载功能，提案建议引入`import()`来代替`require()`
- 位置：可在任何地方使用
- 区别：`require()`是**同步加载**，`import()`是**异步加载**
- 场景：按需加载、条件加载、模块路径动态化











































# to do list

先分析，进行组件划分（通过功能点划分）

拆完组件给它起个名

1.实现静态组件：抽取组件，使用组件实现静态页面的效果（其他的先别考虑）