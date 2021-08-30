# 中文标题：基于Vrep的机器人学教程

## 英文标题：A Guide Towards Learning Robotics with Vrep



# 第零章：序言

## 0.1 读者对象与必备知识

## 0.2 如何使用本教程

## 0.3 教程内容梗概



# 第一章：前置准备

## 1.1 安装Python

1.下载安装包

Python官网：https://www.python.org/

注：Python3与Python2不兼容，所以尽量使用最新版本的Python3![img1.1](/Users/HenryZhou/Desktop/vrep/教程/img1.1.png)

2.安装Python3

（参考：https://blog.csdn.net/qq_16504067/article/details/88286875）

首先选择 “自定义安装”

注： 请选中![img](https://images2017.cnblogs.com/blog/1117202/201707/1117202-20170728225116227-1831326602.png) 把Python添加到环境变量，这样以后在windows命令行(cmd)也可以运行Python

 ![img](https://images2017.cnblogs.com/blog/1117202/201707/1117202-20170728224413540-30358093.png)

 如果没有特殊需求，就全选上。完成后，点击 Next 进行下一步

 ![img](https://images2017.cnblogs.com/blog/1117202/201707/1117202-20170728230500758-1165099877.png)

选中![img](https://images2017.cnblogs.com/blog/1117202/201707/1117202-20170728231509446-620322371.png) 安装目录会改变，请根据自己的需求修改安装路径（为方便后续查找库函数，尽量安装在浅层） ，再点击 Install 进行下一步

 ![img](https://images2017.cnblogs.com/blog/1117202/201707/1117202-20170728231130477-439253115.png)

正在安装.....

<img src="/Users/HenryZhou/Desktop/vrep/教程/img2.png" alt="img2" style="zoom: 50%;" align='left'/>

 安装完成！！

 ![img](https://images2017.cnblogs.com/blog/1117202/201707/1117202-20170728231954008-2131258040.png)

3.测试Python

A. 在Python3自带的IDLE中运行

   使用IDEL   在windows系统下搜索IDLE  （以W8系统为例）

   ![img](https://images2017.cnblogs.com/blog/1117202/201707/1117202-20170729130312222-1556385399.png)

  使用Python语法中的 print( )进行输出（**每行后不需要加分号**，教程错误）

  输入print(“hello world!” )

  如果返回值为 hello world! 则运行正确

   ![img](https://images2017.cnblogs.com/blog/1117202/201707/1117202-20170729130847816-81845217.png)

B. 使用cmd测试交互式编程

  首先打开cmd，在输入根目录下输入 python 并回，如果返回值如下，证明你已经成功安装了python到环境变量

   ![img](https://images2017.cnblogs.com/blog/1117202/201707/1117202-20170729133029191-2136728564.png)

C. 使用cmd测试文本式编程

  使用IDEL下面的file

  ![img](https://images2017.cnblogs.com/blog/1117202/201707/1117202-20170729133734097-1875624385.png)

  输入print(“hello world!” ) （**每行后不需要加分号**）

  ![img](https://images2017.cnblogs.com/blog/1117202/201707/1117202-20170729134121003-293042992.png)

  Ctrl+S  保存为.py 格式的文件

  ![img](https://images2017.cnblogs.com/blog/1117202/201707/1117202-20170729134304847-560504032.png)

  在  cmd 运行  test.py 文件

  ![img](https://images2017.cnblogs.com/blog/1117202/201707/1117202-20170729140323410-1243644440.png)



## 1.2 安装Vrep

（参考：https://blog.csdn.net/weixin_43956732/article/details/111648977）

1.下载安装包

Vrep (Coppelia) 官网：https://www.coppeliarobotics.com/downloads

![img3](/Users/HenryZhou/Desktop/vrep/教程/img3.png)

点击红框处下载教育版，同意教育使用条例后即可开始下载

<img src="/Users/HenryZhou/Desktop/vrep/教程/img4.png" alt="img4" style="zoom:50%;" align='left'/>

2.安装Vrep

安装过程相对比较简单，因为是EDU版本（教育版），故也不需要激活。安装过程如下：

2.1 双击setup.exe文件

![图2  step1](https://img-blog.csdnimg.cn/20201030213120571.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0JJVF9IWFo=,size_16,color_FFFFFF,t_70#pic_center)

可能会出现如下界面，点击“是”就好，一般如果Windows Defender没关的话，安装几乎所有软件都会提醒一下的。

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020103022051081.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0JJVF9IWFo=,size_16,color_FFFFFF,t_70#pic_center)

2.2 安装程序启动：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201030214649990.png#pic_center)

2.3 在欢迎Welcome截面点击Next，在Lecense Agreement截面选择“YES--I agree……”，然后点击Next。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201030214920690.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0JJVF9IWFo=,size_16,color_FFFFFF,t_70#pic_center)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201030214930159.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0JJVF9IWFo=,size_16,color_FFFFFF,t_70#pic_center)

2.4 设置程序快捷方式
这里我们唯一可以选择的是是否要创建桌面快捷方式——“Create shortcut on the desktop”，然后点击Next。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201030215140286.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0JJVF9IWFo=,size_16,color_FFFFFF,t_70#pic_center)

2.5 确认安装程序设置
这里我们不能修改；我们也可以点击官网进去看看，不过一般是不能修改的（我暂时不懂如何修改）；然后点击Next，就进入安装了。安装位置一般为C盘，我也暂时不清楚怎么改动，应为软件不是很大，所以对于我来说安装在C盘影响不大，不过听别人说可以安装后复制到其他位置（非C盘），然后再配置【想想头都大】。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201030215308980.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0JJVF9IWFo=,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201030215614776.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0JJVF9IWFo=,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201030215614621.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0JJVF9IWFo=,size_16,color_FFFFFF,t_70#pic_center)

2.6 Confirm
这里确认是否要配置编译环境，该版本V-rep对应推荐的是Visual Studio 2010是比较老的版本了，我不推荐大家安装，所以我选NO；此外，电脑上如果已经安装了Visual Studio系列软件，当选择YES时会自动提示安装Visual Studio 2010失败并退出Visual Studio 2010的安装。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201030215944290.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0JJVF9IWFo=,size_16,color_FFFFFF,t_70#pic_center)

勾选其中的"Yes --Launch the program file"，即可启动软件，如下图所示；当然也可以不勾选，稍后可以在“开始/程序菜单”处启动软件。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201030220304792.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0JJVF9IWFo=,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201030220340502.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0JJVF9IWFo=,size_16,color_FFFFFF,t_70#pic_center)



## 1.3 配置git与github

**一、前期准备**

（参考教程：https://blog.csdn.net/qq_16504067/article/details/88286875）

首先下载Git，Git官网: https://git-scm.com/

![img5](/Users/HenryZhou/Desktop/vrep/教程/img5.png)

进入GitHub官网 （https://github.com/）**推荐使用谷歌浏览器，部分浏览器可能会进不去官网，**注册账号。

**二、建立存储代码的库**

注册完GitHub账号以后，新建一个库，取名为test

![img](https://img2018.cnblogs.com/i-beta/1716194/202001/1716194-20200115203116644-277129023.png)

这样一个用来云存储代码的库就建好了，我们会看到一个这样的界面，这将会在后面用到

![img](https://img2018.cnblogs.com/i-beta/1716194/202001/1716194-20200115204849351-703600185.png)

库已经建好，那么如何将电脑中的代码上传到库中呢？ 首先，需要做的是将该库与本地连接起来，也就是将库克隆到本地，接下来有两种方法：1、下载GitHub客户端 ；2、通过地址进行连接

**三、克隆库到本地**

**1.下载GitHub客户端（推荐）**

顾名思义，我们需要先从网上下载GitHub并进行安装

![img](https://img2018.cnblogs.com/i-beta/1716194/202001/1716194-20200115204337874-1075813715.png)下载好后点击运行，登录账号

 登录后，我们再来到GitHub官网，点击建好的那个库，需要用到这个界面，由于下载了客户端，我们可以直接点击 **Set up in Desktop**

**![img](https://img2018.cnblogs.com/i-beta/1716194/202001/1716194-20200115205242498-708484009.png)**

 然后电脑会打开GitHub，点击Clone，浏览路径，选择一个本地的文件夹，这里我选择的是一个叫做workspace的文件夹

![img](https://img2018.cnblogs.com/i-beta/1716194/202001/1716194-20200115205945326-116822851.png)

然后找到并进入这个文件夹，会发现文件夹里出现了test的文件夹，这就说明已经将那个叫做test的代码库克隆到了本地。

![img](https://img2018.cnblogs.com/i-beta/1716194/202001/1716194-20200115214426189-92834246.png)

**2、利用地址将库与本地进行连接**

如果不下载客户端的话，可以利用地址来进行连接。我们还是需要利用建好库之后的那个界面，记住地址

![img](https://img2018.cnblogs.com/i-beta/1716194/202001/1716194-20200115210543763-2056198094.png)

 在本地电脑上选择想要保存位置的文件夹，我用的还是刚才那个叫做workspace的文件夹。进入文件夹，这里我已经把刚才那个test文件夹删除了，会发现workspace现在是一个空文件夹，我们单击右键，选择Git Bash Here**(前提电脑已经下载安装了Git）**

![img](https://img2018.cnblogs.com/i-beta/1716194/202001/1716194-20200115211025587-586650752.png)

进入命令窗，输入**git clone https://github.com/xhj1074376195/test.git** 

**注意：这里的地址需要修改为你自己的地址，上面已经强调记住了**

![img](https://img2018.cnblogs.com/i-beta/1716194/202001/1716194-20200115211655488-255594090.png)

 然后去查看workspace文件夹，发现里面出现了test文件夹，克隆成功！

**四、将代码文件等保存至库**

进入电脑中的test文件夹，将需要保存的文件复制到该test文件夹中，这里我的是一个叫做main的cpp文件。右键Git Bash Here进入命令窗。然后开始输入**git add main.cpp**，**注意需要将main.cpp改为你要上传的文件名与类型，**回车然后输入**git commit -m"c++"**，-m后的是字符串备注内容，可任意填写，回车之后，再输入**git push origin master**回车提交，如果GitHub已经登录就可以提交，否则会让你输入账号和密码。

![img](https://img2018.cnblogs.com/i-beta/1716194/202001/1716194-20200115213706449-823308930.png)

 出现这个界面说明上传成功，我们回到GitHub官网查看到库中上传的文件

![img](https://img2018.cnblogs.com/i-beta/1716194/202001/1716194-20200115213925673-819263535.png)

**以后再在这个仓库下写代码就不需要再clone了，只需要在本地仓库（我的workspace文件夹下的test）的文件夹里右击打开Git Bash，然后输入git pull就行了，GitHub上的代码就会更新到本地。**

**上传代码的时候，只需要输入三句命令：**

　　**1. git add 你要上传的文件名或者写成git add \* .这是表示上传所有修改过的代码，这个命令也很常用**

​		**2. git commit -m"your words"这是提交时的备注，备注内容写在双引号内**

​		**3. git push origin master把本地仓库的修改提交到GitHub上**

 **五、git常用命令汇总**

克隆代码：git clone 远程仓库的url

配置邮箱：git config --global user.email

配置用户名：git config --global user.name

从远程仓库下拉代码到本地：git pull

放弃本地代码的修改：git checkout -- <file>

将本地代码添加到缓冲区：git add * .

移除add到缓冲区的文件：git reset HEAD <file>
将本地代码提交到本地仓库：git commit -m"日志文字"

将本地仓库同步到远程仓库：git push origin master

查看日志：git log

查看某个文件的提交日志：git log 文件名

查看某个用户的提交日志：git log --author=“author”

查看某条提交日志相信信息：git show 版本号

查看git全部命令：git --help

查看git某个命令的使用：git help 命令名

 **六、远程仓库中文件夹的删除**

 打开git bash

敲入$ git rm -r --cached 文件夹名称

敲入$ git commit -m 'delete 文件夹名称 dir'

 敲入$ git push origin master重新提交



## 1.4 Vrep建模

（文案参考：https://blog.csdn.net/SAKURASANN/article/details/100053580）

（操作参考：https://www.youtube.com/watch?v=7zCVTKOZAz8）

### 1.4.1 SolidWorks阶段

### 1.4.2 Vrep阶段

本教程将指导你逐步建立一个简洁的机器人或其他项目的仿真模型。想要得到一个美观，显示速度和模拟速度快并且稳定的仿真模型，这是一个非常重要的专题，可能也是最重要的一个方面。

为了说明建模过程，要创建下图中的机械臂：

![img](https://img-blog.csdnimg.cn/20190824160758775.jpg)

从外部应用程序导入 CAD 数据时，最重要的是确保 CAD 模型的不是太密集，即不包含太多的三角形。这一点很重要，因为密集的模型会让显示速度变得很慢，同时也减慢了可能在后期使用的各种计算模块的计算速度（如最小距离计算或动力学）。下面这个例子通常是不可行的（即使我们稍后将会看到，但是会有办法简化V-REP 中的数据）：



以上的CAD 数据图非常密集：它包含许多三角形（超过47000），如果我们仅在空场景中使用单个实例，这是可行的。但大多数情况下，是要模拟同一个机器人的几个实例，并附加各种类型的夹具，还有可能会让这些机器人与其他机器人、设备或环境相互作用。在这种情况下，模拟场景很快就会变得很慢。一般来说，我们建议对拥有着不超过20000 个三角形的机器人进行建模，但大部分情况下，5000-10000个三角形也可以很好地进行建模。记住：什么都是越少越好。

什么让上面的模型这么密集呢？首先，含有孔和小细节的模型需要更多的三角形面才能正确的表示出来。因此，如果可以的话，请尝试从原始模型数据中删除物体中所有孔、螺丝、以及内部物体等。如果把原始模型数据表示为参数曲面/对象，那么大部分时间只是选择项目并删除它们这么简单（例如，在 Solidworks 中）。第二个重要步骤是以有限的精度导出原始数据：大多数CAD 应用程序允许指定导出网格的层次细节。当绘图由大型和小型对象组成时，分步骤导出对象可能也很重要；这是为了避免把大对象设定的太精确（即设定太多的三角形）并且把小对象设定的太粗略（即设定太少的三角形）：只需要先导出大对象（调整所需的精度设置），然后是小对象（调整精度设置）。

V-REP 目前支持以下的CAD 数据格式：OBJ，STL，DXF，3DS（仅限Windows）和Collada。也支持URDF，但是这里没提到，因为它不是一个基于网格的纯理论的文件格式。

现在假设我们已经应用了上节所述的所有可能的简化格式。在导入后，可能还会出现密集的网格：



可以注意到整个机器人被导入为单个网格。稍后我们会看到如何对其进行适当分割。还要注意导入网格的错误方向：最好是让方向保持原样，直到构建好整个模型为止，因为在稍后阶段，如果我们要导入与同一个机器人相关的其他项目，涉及到原始网格时，他们就会自动保持正确的位置/方向。

在这一阶段，我们可以任意使用一些功能来简化网格：

自动网格划分：允许为所有元素生成新的形状，这些元素没有通过公共边缘链接在一起。这对于所选择的网格并不总是有效，但值得一试，因为在网格元素上工作可以让我们得到更多的控制权，而不是同时处理所有元素。可以点击 [Menu bar --> Edit --> Grouping/Merging --> Divide selected shapes] 来访问该功能。有时候，网格会比预期的多。在这种情况下，只需将逻辑上同属一体的元素（即将具有相同的视觉属性并且是相同链接的一部分）合并成一个单一形状即可（[Menu bar --> Edit -> Grouping/Merging --> Merge selected shapes]）。

提取凸包：允许通过将网格转换为凸包来简化网格。可以点击 [Menu bar --> Edit --> Morph selection into convex shapes] 来访问该功能。

筛选网格：允许减少网格中包含的三角形数量。可以点击 [Menu bar --> Edit --> Decimate selected shape...] 来访问该功能。

删除网格内部：允许通过删除网格内部来简化网格。该功能基于视觉传感器，并且可能会根据所选设置给出或多或少令人满意的结果。可以点击 [Menu bar --> Edit --> Extract inside of selected shape] 访问该功能。

以上可应用的功能没有预定义顺序（除了列表中的第一个项目，总是先用于尝试），它很大程度上取决于我们正在尝试简化的网格的几何形状。以下图片说明了应用于上述导入网格的功能（假设列表中的第一个项目对我们来说无效）：



注意在这一阶段，凸包没法帮助我们。首先我们决定使用网格筛选功能，并运行该功能两次，以便将三角形数量除以总数 50。这一步一旦完成，我们就将其简化形状的内部提取出来并删除。最终剩下一个包含有 2660 个三角形的网格（最开始导入的网格含有136000 个三角形）。我们可以在形状几何对话框中看到三角形/顶点数包含的形状数量。对于整个机器人模型来说，2660 个三角形已经非常少了，只是视觉呈现可能会受到一点点影响。

在这个阶段，我们可以开始将机器人划分成不同的连接块（请记住，我们目前只有整个机器人的一个简单的形状）。你可以通过两种不同的方法来划分：

自动划分网格：此功能已经在上一节中介绍过，它会检查形状，并为所有未通过公共边缘连接在一起的元素生成新的形状。这并不总是奏效，但总是值得一试。可以点击 [Menu bar --> Edit --> Grouping/merging --> Divide selected shapes] 来访问该功能。

手动网格分割：通过三角形编辑模式，可以手动选择逻辑上不属一体的三角形，然后单击 Extract shape。这将在场景中生成一个新的形状。然后删除所选三角形。

在这种情况下时，第一种方法对于我们的模型会奏效：



现在，我们可以进一步细化/简化个体形状。有时，如果使用其凸包，形状可能会更好看。其他时候，你就不得不重复使用上述几种技术，以获得想要的结果。以网格为例：



上面的形状存在的问题是，它含有很多孔，所有我们不能很好地对其进行简化。所以我们必须通过形状编辑模式使用更复杂的方式，在这里我们可以提取逻辑上属于同一个凸子实体的各个元素。这个过程可能需要反复好几次：首先提取3 个近似的凸元素。现在，我们忽略掉两个孔的一部分，即三角形。在形状编辑模式下编辑形状时，方便切换可见层，以便查看其他场景项目所覆盖的内容。



我们最终得到了三种形状，但其中两个还需进一步改进。现在我们可以删除掉孔中的三角形。最后，我们分别提取3 个形状的凸包，然后点击 [Menu bar --> Edit --> Grouping/Merging --> merge selected shapes] 把它们合并起来：



在V-REP 中，我们可以启用/禁用每个形状的边缘显示。还可以指定边缘显示需要计算的角。类似于阴影角度这样的参数，它表明形状会显示出来的多面体。这些参数和其他一些如形状颜色等参数，可以在形状属性中进行调整。要记住，形状有不同的类型。在本教程中，迄今为止我们只处理了一些简单的形状：简单的形状具有单一视觉属性（即一种颜色，一种阴影角度等）。如果将两个形状合并，那么结果还会是一个简单的形状。你也可以对形状进行分组，在这种情况下，每个形状将保留其视觉属性。

在下一步中，我们可以合并逻辑上同属的元素（如果它们是同一刚性元素的一部分，并且具有相同的视觉属性）。然后我们改变各个元素的视觉属性。最简单的方法不是调整一些具有不同颜色和视觉属性的形状，而是我们使用特定的字符串命名颜色，稍后可以通过编程方式更改颜色，同样地，如果形状是复合形状的一部分，也采用同样的方式。然后，我们就选择所有具有相同视觉属性的形状，然后 ctrl 选择已调整的形状，接下来单击 Apply to selection，一次是颜色，一次是其他属性，在形状属性中：这会将所有的视觉属性传输到所选形状（包括颜色名称，如果你提供了的话）。我们最终得到17 个独立形状：




现在我们可以点击 [Menu bar --> Edit --> Grouping/merging -> Group selected shapes] 将与之有相同链接的一部分的形状分组。我们最终得到了 7 个形状：机器人的底座（或机器人层次结构树的底座）和 6 个移动连接。正确命名你的对象也很重要：我们可以双击场景层次结构中的对象名称来命名对象。底座应该始终是机器人或模型的名称，其他对象应始终包含底座对象得名称，如 robot (base) ， robot_link1 ，robot_proximitySensor 等。默认情况下，形状将被分配到可见性层1，但是可以在对象的共同属性中进行更改。默认情况下，只有可见层1-8 可以激活场景。现在可以得到以下场景（在模型属性对话框中临时让模型 ResizableFloor_5_25 隐藏起来）：



当创建或修改形状时，V-REP 将自动设置其参考框架的位置和方向。形状的参考框架将始终位于形状的几何中心。选择框架方向，使形状的边框尽可能小。这样看起来不一定很美观，但我们可以随时重新调整形状的参考框架。现在重新调整我们所创建的所有形状的参考框架，点击 [Menu bar --> Edit --> Reorient bounding box --> with reference frame of world]。在形状几何对话框中，你有更多的选择去重新调整参考框架。

构建关节
现在我们要处理关节/驱动。大多数时候，我们知道每个关节的确切位置和方向。在这种情况下，我们只需点击 [Menu bar --> Add --> Joints --> ...] 添加关节，然后我们可以使用坐标和变换对话框来更改位置和方向。在其他情况下，我们只有 Denavit-Hartenberg（即D-H）参数。在那种情况下，我们可以在模型浏览器中的 Models/tools/Denavit-Hartenberg joint creator.ttm 中的工具模型构建关节。有时候，我们没有关节位置和方向的相关信息。然后，我们需要从导入的网格中提取它们。我们假设这是目前的情况。在近似于网格，而非改良的条件下工作，我们打开一个新的场景，再次导入原始的CAD数据。大多数时候，我们可以从原始网格中提取网格或源形状。第一步是细分原始网格。如果不起作用，就使用三角形编辑模式来编辑。假设我们可以划分原始网格。我们现在就拥有更小的物体，即我们可以对其进行检查的物体。我们正在寻找旋转形状，它可以用作在相同位置和相同方向创建关节的一种参考。首先，删除所有不需要的对象。有时为了使可视化或操作更简单，可以同时打开多个场景。对我们来说，我们首先要关注机器人的底座：它包含有一个圆柱体，对于第一个关节来说，这个圆柱体处于正确的位置。在三角形编辑模式下，我们可以看到以下场景：



我们通过页面选择器工具栏按钮更改摄像机视图，以便从侧面查看对象。 布满视图工具栏按钮可以方便地在编辑模式下中正确构建对象。 然后我们切换到顶点编辑模式并选择属于上部盘的所有顶点。 请记住，通过打开/关闭某些图层，我们可以隐藏场景中的其他对象。 然后我们切换回三角形编辑模式：



现在我们点击 Extract cylinder（Extract shape 也可以在那种情况下工作），这只是基于所选的三角形在场景中创建一个圆柱形。我们退出编辑模式并放弃更改。现在我们单击 [Menu bar --> Add --> Joint --> Revolute] 添加一个旋转关节，保持选中，然后 ctrl 选择所提取的圆柱体形状。在坐标和变换对话框中，单击 position 按钮，然后在“对象/项目方向”部分中单击 Apply to selection：这基本上将圆柱体的 x / y / z 位置复制到关节上了。现在两个位置是一样的。单击 orientation 按钮，单击 Apply to selection：现在我们所选对象的方向也一样了。有时，为了得到正确的方位或旋转方向，我们还要围绕其自身的参考框架另外将关节旋转约90/180度。如果有必要，我们可以在对象/项目旋转操作部分执行此操作（在这种情况下，请勿忘记单击 Own frame 按钮）。按照同样的方式，我们也可以沿着它的轴移动关节，甚至进行更复杂的操作。这就是我们所拥现在所看到的：



现在我们将关节复制到原始场景中，并保存（要记得定期保存工作！撤消/重做功能很有用，但不能保护你免受其他故障的影响）。我们对机器人中的所有关节重复上述步骤，然后重新命名。为了看到他们全部，我们还要使所有关节在关节属性中稍长一点。在默认情况下，关节将被指派到可见性层2，但可以在对象的共同属性中对其进行改变。我们现在将所有关节指派给可见性层10，然后暂时使场景的可见性层10 也可以显现这些关节（在默认情况下，仅为场景激活可见层1-8）。这是我们现在看到的（在模型属性对话框中暂时将模型ResizableFloor_5_25 隐藏起来）：



在这一点上，我们可以开始构建模型层次结构并且完成模型定义。但是如果我们希望我们的机器人能够动态启用，那么就还需要一个中间步骤：

构建动态形状
如果我们想让我们的机器人能够动态启用，即对碰撞，跌倒等做出反应，那么我们需要适当地创建/配置形状：这种形状可以是：

动态或静态：动态（或非静态）形状将下降并受外力或扭矩的影响。另一方面，静态（或非动态）形状会在场景中静止不动，或者在场景层次结构中跟随其上层（即本体）移动。

可响应的或不可响应的：可响应的形状将与其他可响应形状的发生碰撞反应。它们（和/或）他们的对撞机，如果它们是动态，它们的运动将会受到影响。另一方面，如果不可响应形状与其他形状相碰撞，那么他们将不会计算碰撞响应。

以上两点会在这里进行说明。为了进行快速稳定的模拟，可响应的形状要尽可能简单。物理引擎将能够模拟以下 5 种速度和稳定性各具差异的形状：

纯形状：纯形状稳定，且物理引擎可以对其进行有效地处理。简单的说，纯形状在几何方面是有限的：主要是立方体，圆柱体和球体。如果可能，其他项接触时间较长的物体（例如人形机器人的脚，串联式机器人的底座，夹具的手指等）可以使用纯形状。可以点击 [Menu bar --> Add --> Primitive shape] 创建纯形状。

纯复合形状：纯复合形状是几种纯形状的组合。它的性能几乎和纯形状一样，并且有着相似的属性。可以将几个纯形状分组，点击[Menu bar --> Edit --> Grouping/Merging --> Group selected shapes] 来生成纯复合形状。

凸形：凸形会有一点不稳定，用物理引擎对其进行处理时也会多花费一点计算时间。相比较纯形状，凸形考虑到更多的通用几何（唯一的要求是，它只需是凸起的就行）。如果可以，对于那些偶尔会与其他项目接触的项目使用凸形（例如机器人的各种链接）。可以点击 [Menu bar --> Add --> Convex hull of selection] 或 [Menu bar --> Edit --> Morph selection into convex shapes] 生成凸形。

复合凸形或凸分解形状：凸分解形状是几个凸形的分组。它的性能几乎和凸形相似，并具有相似的性质。凸分解的形状可以通过点击 [Menu bar --> Edit --> Grouping/Merging --> Group selected shapes]，使用 [Menu bar --> Add --> Convex decomposition of selection...] 或 [Menu bar --> Edit --> Morph selection into its convex decomposition...] 来生成。

随机形状：随机形状既非凸面也不是纯形状。它的性能通常较差（即计算速度和稳定性）。尽量不用随机形状。

所以它们的优先顺序为：纯形状，纯复合形状，凸形，复合凸形，最后是随机形状。请务必阅读本页。假如我们想要创建机器人，就使用纯圆柱体作为机器人的底座，用其他连接作为凸形或凸分解形状。

我们可以使用动态形状作为机器人的可见部分，但这可能看起来不够好。反之，我们将会为教程第一部分中创建的每个可见形状构建一个动态启用的对等体，然后将其隐藏：隐藏部分将表示动态模型，并由专门的物理引擎使用，而可视部分将用于可视化，还可用于计算最小距离，检测近距离传感器等。

选择对象 robot，将其复制并粘贴到新场景中（以保持原始模型不变）并启动三角形编辑模式。如果该对象是复合形状，我们首先必须取消分组（[Menu bar --> Edit --> Grouping/Merging --> Ungroup selected shapes]），然后合并各个独立的形状（[Menu bar --> Edit --> Grouping/Merging --> Merge selected shapes]），然后才能启动三角形编辑模式。现在选择代表电源线的几个三角形，将其删除。然后我们选择该形状中的所有三角形，然后单击 Extract cylinder。现在可以离开编辑模式，并且我们的底座是纯圆柱体：



重新命名新形状（在场景层次结构中双击其名称）为 robot_dyn，将其指派给可见层 9，然后将其复制到原始场景中。其余的连接杆将被做成凸形或复合凸形模型。现在选择第一个移动连杆（即对象 robot_link1），并点击 [Menu bar --> Add --> Convex hull of selection] 从中生成凸形。我们将它重命名为 robot_link_dyn1，并将其指派给可见层 9。当提取凸包没有保留原始形状的足够的细节时，你仍然可以从其组成元素中手动提取几个凸包，然后点击 [Menu bar --> Edit --> Grouping/Merging --> Group selected shapes] 将所有凸包组合起来。如果这很棘手或耗时，那么可以点击 [Menu bar --> Add --> Convex decomposition of selection...] 自动提取凸分解形状：


原始形状，凸形状

原始形状，凸分解形状
现在对所有剩余的机器人连杆重复相同的步骤。该步骤一完成，就将每个可见的形状与相应的不可见动态装饰连接在一起。选择第一个可见的形状，然后点击Ctrl 键选择其动态装饰，然后点击 [Menu bar --> Edit --> Make last selected object parent] 。想要获得相同的结果可以将可见形状拖动到其层级中的动态装饰上：



我们仍需要注意以下几点：首先，由于我们希望动态形状只对物理引擎可见，而非其他计算模块，因此我们将在对象共同属性中取消选中动态形状的 object special properties。

然后，我们仍须将动态形状设置为动态和可回复的。在形状动力学属性中我们会做到这一点。首先选择基本的动态形状（即robot_dyn），然后选择 Body is respondable。启用前 4 个 Local respondable mask 标志，并禁用最后 4 个 Local respondable mask标志：对于连续的可响应连杆来说，最重要的是它们不会相互冲突。对于机器人中的第一个移动动态连杆（即 robot_link_dyn1 ），我们还启用了 Body is respondable，但是这次我们禁用前 4 个 Local respondable mask标志，并启用最后4 个 Local respondable mask 标志。让所有的其他动态连杆重复上述过程，同时始终让 Local respondable mask 标志交替启用：一旦定义了模型，机器人的连续动态形状将在彼此交互时不产生任何碰撞响应。尽量以机器人的动态底座结构结束，并且机器人最后的动态连杆只启用前 4 个 Local respondable mask 标志，这样我们就可以将机器人与移动平台连接在一起，或者将夹具和机器人的最后一个动态连杆连接在一起，且不受动态碰撞干扰。

最后，我们仍需将我们的动态形状标记为 Body is dynamic。我们在形状动力学属性中也会做到这一点。然后，我们可以手动输入质量和惯性张量属性，或单击 Compute mass & inertia properties for selected convex shapes 来自动计算那些值（推荐）。还要记住这一动态设计和那一动态设计的注意事项。机器人的这种动态底座是一种特殊情况：大部分情况下我们希望机器人的底座（即 robot_dyn）是非动态的（即静态的），否则，在单独使用的情况下，机器人可能会在运动过程中掉落。但是，只要我们将机器人的底座连接到移动平台，我们就希望底座变成动态的（即非静态的）。启用 Set to dynamic if gets parent 来做到这一点，然后禁用Body is dynamic。现在运行模拟：除了机器人的底座之外，所有的动态形状都会掉落。附带的视觉形状会和他们的动态装饰动作一致而掉落。

模型定义
现在我们准备定义我们的模型。我们首先建立模型层级结构： 选择最后一个动态机器人连杆（robot_link_dyn6） ，将与其对应的关节（robot_joint6）连接起来，然后点击 ctr 选择 robot_joint6，然后点击 [Menu bar --> Edit --> Make last selected object parent]。我们也可以将对象 robot_link_dyn6 拖放到场景层次结构中的 robot_link6 上来完成此步骤。现在继续将robot_joint6 与 robot_link_dyn5 连接起来，然后是其他的，直到到达机器人的底座。现在的场景层次结构如下图所示：



因为模型底座也代表模型本身，因此为模型底座取个简单的名称就更合乎逻辑。所以我们将机器人重命名为 robot_visibleBase，将 robot_dyn 重命名为 robot。现在我们选择层次结构树（即对象 robot）的底座，并且在对象共同属性中启用 Object is model base。我们还可以启动 Object/model can transfer or accept DNA。这时出现了一个包围着整个机器人的模型边框。然而，这个边框看起来太大：这是因为边界框还包含不可见的项目，例如关节。我们现在为所有关节启用 Don't show as inside model selection 来排除模型边界框中的关节。我们可以对模型中所有的不可视项目进行同样的步骤。想要从模型边界框中排除大型传感器或其他项，这是一个有用的选择。目前情况如下：



现在要保护我们的模型免受意外的修改。选择机器人中的所有可见对象，然后启用 Select base of model instead：如果现在单击场景中的可见连杆，就会选中机器人的底座。这样我们可以像操纵一个单一对象那样来操纵模型。我们也可以在场景中点击 Ctrl+Shift 键来选择机器人中的可见对象，或在场景层次结构中选择对象。现在将机器人置于正确的默认位置/方位。首先，我们保存当前场景作为参考（例如，如果在稍后阶段，我们需要在当前机器人中导入具有相同方向的CAD 数据）。然后我们选择模型并适当修改其位置/方向。将模型（即其底座）定位在 X = 0 和 Y = 0 这个位置是就很好。



我们现在运行模拟：机器人会崩溃，因为关节默认为不受控制。在前一阶段添加关节时，我们在力/扭矩模式下创建了关节，但是在默认情况下，它们的驱动或控制器被禁用。我们现在可以根据我们的要求来调整关节。对我们而言，每一个关节都需要一个简单的PID 控制器。在关节动态属性中，单击启动 Motor enabled 并调整 maximum torque。接着点击 Control loop enabled， 然后选择 Position control (PID)。现在再次运行模拟：机器人位置应该会保持不变。试着切换到当前的物理引擎，查看所有被支持的物理引擎的行为是否一致。你可以通过相应的工具栏按钮或通用的动态属性来执行此操作。

在模拟期间，我们通过动态内容可视化和验证工具栏按钮验证场景动态内容。现在，仅物理引擎内的项目能显示出来，并且用不同的颜色对显示器进行编码。始终这样做非常重要，特别是当动态模型不按预期运转时，这样可以快速调试模型。同样地，在模拟期间始终盯紧场景层次结构：动态启用的对象会在其名称右侧显示一个球状图标。



最后，我们需要布置好机器人，便于我们能轻松地将夹具连接到机器人上，或者轻松地将机器人连接到移动平台上（举例来说）。两个动态启用的形状可以以两种不同的方式牢牢相连：

通过分组连接：选择形状，然后点击 [Menu bar --> Edit --> Grouping/Merging --> Group selected shapes]。

通过力/扭矩传感器将它们连接起来：力矩传感器也可以作为两个分离的动态启用形状之间的刚性连接。

对我们而言，只有选项 2 是有意义的。我们点击 [Menu bar --> Add --> Force sensor] 创建力/扭矩传感器，然后将其移动到机器人的齿棱， 然后将其与 robot_link_dyn6 连接起来。适当改变其尺寸和视觉外观（红色力/扭矩传感器通常被当做可选附件点，检查各种可用的机器人模型）。我们将其名变更为 robot_attachment：



现在我们将一个夹子模型拖到场景中，保持选中状态，然后按 Ctrl 键单击附件力传感器，然后单击组装/拆卸工具栏按钮。夹具就到位了：



因为在模型定义期间，它已经有过相应配置了，所以夹具知道如何连接自己。现在还需要正确配置机器人模型，这样它就会知道如何将自己连接到移动底座上。我们选择机器人模型，然后在对象共同属性中单击 Assembling。为 'Parent' match values 设置空字符串，然后单击 Set matrix。这会记忆当前的底座对象的局部转关矩阵，并使用它来对相关的移动机器人的附着点来定位或调整自己。想要验证我们的做法是正确的，就将 Models/robots/mobile/KUKA Omnirob.ttm 等模型拖到场景中。然后选择我们的机器人模型，接下来按Ctrl 键单击移动平台上的一个附着点，然后单击组装或拆卸工具栏按钮。正确地将我们的机器人放置在移动机器人的顶部：



现在可以在我们的机器人上添加其他项目，例如传感器。在某些时候，我们也可能希望将嵌入式脚本连接到我们的模型中，以便于控制其行为或将其配置为各种用途。在这种情况下，请确保了解如何从嵌入式脚本访问对象句柄。我们还可以从插件，从远程API客户端，从ROS 平台或附加组件控制/访问/连接我们的模型。

现在我们要确保已经恢复了机器人和夹具附件中进行的更改，我们折叠了机器人模型的层次结构树，选择了模型的底座，然后点击[Menu bar --> File --> Save model as...] 进行保存。如果我们将其保存在模型文件夹中，那就可以在模型浏览器中使用模型。




# 第二章：Vrep基础

## 2.1 通讯原理

（翻译自：https://www.coppeliarobotics.com/helpFiles/en/meansOfCommunication.htm）

在V-REP环境中可以通过多种方式实现内部数据/信息的传输/交互，比如：

- Signals （信号）
- Custom data blocks （自定义数据块）
- Calling plugin functions （调用内嵌函数）

V-REP还可以实现与环境外的应用程序，以及其他计算机和机器之间的数据交互，例如：

- calling script functions （调用脚本函数）
- ROS
- the remote API（外部函数接口）
- serial port （串口）
- Sockets （套接字）

### 2.1.1 内部通讯

#### 2.1.1.1 Signals

信号相当于全局变量，可以被定义、重新定义、读取和清除，例如：

```lua
-- script 1 writes the data to string signal mySignalName:

local myData={1,2,{"Hello","world",true,{value1=63,value2="aString"}}}
sim.setStringSignal("mySignalName",sim.packTable(myData))
```

```lua
-- script 2 reads the data from string signal mySignalName:

local myData=sim.getStringSignal("mySignalName")
if myData then
    myData=sim.unpackTable(myData)
end
```

#### 2.1.1.2 Custom data blocks

自定义数据块是存储在场景本身或场景物体内部的数据，可用于存储与模型或场景一起保存的自定义数据，也可用作通信手段，例如：

```lua
-- script 1 writes the data to the scene:

local myData={1,2,{"Hello","world",true,{value1=63,value2="aString"}}}
sim.writeCustomDataBlock(sim.handle_scene,"myTag",sim.packTable(myData))
```

```lua
-- script 2 reads the data from the scene:

local myData=sim.readCustomDataBlock(sim.handle_scene,"myTag")
if myData then
    myData=sim.unpackTable(myData)
end
```

#### 2.1.1.3 Calling plugin function

脚本 (scripts) 也可以调用特定的插件函数 (plugin functions)，即所谓的回调函数 (callback functions) 。为了能够做到这一点，插件必须先通过 simRegisterScriptFunction 注册其回调函数，这是扩展 CoppeliaSim 功能的便捷机制，但也可用于脚本和插件之间的复杂数据交换。插件函数及其注册代码如下例：

```c++
void myCallbackFunc(SScriptCallBack* p)
{
    int stack=p->stackID;
    CStackArray inArguments;
    inArguments.buildFromStack(stack);
	
    if ( (inArguments.getSize()>0)&&inArguments.isString(0) )
    {
        std::string tmp("we received a string: ");
        tmp+=inArguments.getString(0);
        simAddLog("ABC",sim_verbosity_msgs,tmp.c_str());
		
		CStackArray outArguments;
		outArguments.pushString("Hello to you too!");
		outArguments.buildOntoStack(stack);
    }
    else
        simSetLastError("simABC.func","Not enough arguments or wrong arguments.");
}

// Somewhere in the plugin's initialization code:
simRegisterScriptCallbackFunction("simABC.func@ABC","string reply=simABC.func(string inputStr)",myCallbackFunc);
```

### 2.1.2 外部通讯

#### 2.1.2.1 Calling scipt functions

脚本函数除了能够被同一脚本内的代码调用，同样也可以通过以下途径调用：

- 跨脚本（通过 sim.callScriptFunction）
- 插件（通过 simCallScriptFunctionEx）
- ROS client（通过 callback mechanism）
-  remote API client（通过传统远程API）

#### 2.1.2.2 ROS

ROS与ROS2不仅可以用于外部通讯，还能实现VREP内的通讯。例如，摄像头的ROS2 publisher端如下：

```lua
function sysCall_init()
    visionSensor=sim.getObjectHandle('Vision_sensor')

    -- Enable an image publisher:
    pub=simROS2.createPublisher('/image', 'sensor_msgs/msg/Image')
    simROS2.publisherTreatUInt8ArrayAsString(pub)
end

function sysCall_sensing()
    -- Publish the image of the vision sensor:
    local img,w,h=sim.getVisionSensorCharImage(visionSensor)
    data={}
    data.header={stamp=simROS2.getTime(), frame_id='a'}
    data.height=h
    data.width=w
    data.encoding='rgb8'
    data.is_bigendian=1
    data.step=w*3
    data.data=img
    simROS2.publish(pub,data)
end

function sysCall_cleanup()
    simROS2.shutdownPublisher(pub)
end
```

相对应的subscriber端为：

```lua
function sysCall_init()
    -- Enable an image subscriber:
    sub=simROS2.createSubscription('/image', 'sensor_msgs/msg/Image', 'image_callback')
    simROS2.subscriptionTreatUInt8ArrayAsString(sub)
end

function image_callback(msg)
    -- Here we have received an image
end

function sysCall_cleanup()
    simROS2.shutdownSubscription(sub)
end
```

#### 2.2.2.3 Remote API（重点）

通过远程API同样可以实现内部和外部通讯，以Python接受摄像头图像为例：

```python
import sim
from time import sleep
clientID=sim.simxStart('127.0.0.1',19997,True,True,5000,5)
if clientID!=-1:
    res,sensor1Handle=sim.simxGetObjectHandle(clientID,'VisionSensor1',sim.simx_opmode_oneshot_wait)
    res,sensor2Handle=sim.simxGetObjectHandle(clientID,'VisionSensor2',sim.simx_opmode_oneshot_wait)

    res,resolution,image=sim.simxGetVisionSensorImage(clientID,sensor1Handle,0,sim.simx_opmode_streaming)
    sim.simxStartSimulation(clientID,sim.simx_opmode_oneshot)
    while (sim.simxGetConnectionId(clientID)!=-1):
        res,resolution,image=sim.simxGetVisionSensorImage(clientID,sensor1Handle,0,sim.simx_opmode_buffer)
        if res==sim.simx_return_ok:
            res=sim.simxSetVisionSensorImage(clientID,sensor2Handle,image,0,sim.simx_opmode_oneshot)
        sleep(0.01)
    sim.simxFinish(clientID)
```

在该模式下，客户端和服务器之间使用socket套接字进行通讯。

The remote API functions are interacting with V-REP **via socket communication** in a way that reduces lag and network load to a great extent. The remote API can let one or several external applications interact with V-REP.

　　A remote API function is called in a similar fashion as a regular API function, however with 2 major differences:

1. most remote API functions return a similar value: a return code.
2. most remote API functions require two additional argument: the operation mode, and the clientID (identifier returned by the simxStart function)

　　由于客户端和服务器使用进行通信，因此就涉及到网络编程时常见的同步(Sync)/异步(Async)，阻塞(Block)/非阻塞(Unblock)等调用方式。The need for an operation mode and a specific return code comes from the fact that the remote API function has to travel via socket communication to the server (V-REP), execute a task, then return to the caller (the client). A naive (or *regular*) approach would be to have the client send a request, and wait until the server processed the request and replied: in most situations this would take too much time and the lag would penalize the client application. Instead, the remote API lets the user chose the type of operation mode and the way simulation advances by providing four main mechanisms to execute function calls or to control the simulation progress:



- Blocking function calls（a blocking function call is the naive or regular approach）
- Non-blocking function calls
- Data streaming
- Synchronous operation

　　***\*1.  Blocking function calls（阻塞调用）\****

　　这种方式在调用结果返回之前，当前线程会被挂起。函数只有在得到结果之后才会返回。比如下面代码获取物体句柄，操作模式采用阻塞模式simx_opmode_blocking（A command is sent to the server for execution, and the function waits for the reply from the server）

```
// Following function (blocking mode) will retrieve an object handle:
if (simxGetObjectHandle(clientID,"myJoint",&jointHandle,simx_opmode_blocking)==simx_return_ok)
{
    // here we have the joint handle in variable jointHandle!
}
```

　　下图反映了阻塞调用的流程：

![img](https://bbsmax.ikafan.com/static/L3Byb3h5L2h0dHBzL2ltYWdlczIwMTUuY25ibG9ncy5jb20vYmxvZy84OTA5NjYvMjAxNzAyLzg5MDk2Ni0yMDE3MDIxMzE5MDAxODg0Ny0xNjQ2MDYwMTEyLnBuZw==.jpg)　　**2.  Non-blocking function calls（非阻塞调用）**

　　非阻塞指在不能立刻得到结果之前，该函数不会阻塞当前线程，而会立刻返回。非阻塞调用适用于不需要服务端应答的场合（A non-blocking function call is meant for situations when we simply want to send data to V-REP without the need for a reply）。如下面例子，只是调用函数设置关节位置而不需要服务端返回数据，就可以使用非阻塞模式simx_opmode_oneshot。

```
// Following function (non-blocking mode) will set the position of a joint:
simxSetJointPosition(clientID,jointHandle,jointPosition,simx_opmode_oneshot); 
```



　　下图反映了非阻塞调用的流程：

![img](https://bbsmax.ikafan.com/static/L3Byb3h5L2h0dHBzL2ltYWdlczIwMTUuY25ibG9ncy5jb20vYmxvZy84OTA5NjYvMjAxNzAyLzg5MDk2Ni0yMDE3MDIxMzE5MTA0OTA4Mi0yMDI0MjIwNjE2LnBuZw==.jpg)

　　阻塞/非阻塞，是指程序在等待消息时的状态。简单理解为需要做一件事能不能立即得到应答返回。如果不能立即获得返回，需要等待，那就阻塞了；否则就可以理解为非阻塞。详细区别如下图所示：

![img](https://bbsmax.ikafan.com/static/L3Byb3h5L2h0dHBzL2ltYWdlczIwMTUuY25ibG9ncy5jb20vYmxvZy84OTA5NjYvMjAxNzAyLzg5MDk2Ni0yMDE3MDIxMzE5NTA1MzYxMy00NzIzMTc4MzYucG5n.jpg)

　　有时为了同时发送多条指令给服务端响应，我们可以先暂停通信。In some situations, it is important to be able to send various data within a same message, in order to have that data also applied at the same time on the server side (e.g. we want the 3 joints of a robot to be applied to its V-REP model in the exact same time, i.e. in the same simulation step). In that case, the user can temporarily halt the communication thread in order to achieve this, as shown in following example:

```
simxPauseCommunication(clientID,);  //Allows to temporarily halt the communication thread from sending data.
simxSetJointPosition(clientID,joint1Handle,joint1Value,simx_opmode_oneshot);
simxSetJointPosition(clientID,joint2Handle,joint2Value,simx_opmode_oneshot);
simxSetJointPosition(clientID,joint3Handle,joint3Value,simx_opmode_oneshot);
simxPauseCommunication(clientID,); // Above's 3 joints will be received and set on the V-REP side at the same time
```

　　Following diagram illustrates the effect of temporarily halting the communication thread:

![img](https://bbsmax.ikafan.com/static/L3Byb3h5L2h0dHBzL2ltYWdlczIwMTUuY25ibG9ncy5jb20vYmxvZy84OTA5NjYvMjAxNzAzLzg5MDk2Ni0yMDE3MDMwMTEwMjMxNjUwMS0xMDIwNjQxOTkzLnBuZw==.jpg)

　　***\*3.  Data streaming（数据流模式）\****

　　这一模式下，客户端可以向服务端发起请求连续的数据流。可以将其看做一种客户与服务端之间的命令/信息订阅模式（也可以类比模拟信号采集卡的连续采样功能：Analog Input在采样过程中每相邻两个采样点的时间相等，采集过程中不停顿，连续不间断的采集数据，直到用户主动停止采集任务）。客户端发起数据流请求及读取的代码如下所示：

```
// Streaming operation request (subscription) (function returns immediately (non-blocking)):
simxGetJointPosition(clientID,jointHandle,&jointPosition,simx_opmode_streaming); // The control loop:
while (simxGetConnectionId(clientID)!=-) // while we are connected to the server..
{
    // Fetch the newest joint value from the inbox (func. returns immediately (non-blocking)):
    if (simxGetJointPosition(clientID,jointHandle,&jointPosition,simx_opmode_buffer)==simx_return_ok)
    {
        // here we have the newest joint position in variable jointPosition!
    }
    else
    {
        // once you have enabled data streaming, it will take a few ms until the first value has arrived. So if
        // we landed in this code section, this does not always mean we have an error!!!
    }
} // Streaming operation is enabled/disabled individually for each command and
// object(s) the command applies to. In above case, only the joint position of
// the joint with handle jointHandle will be streamed.
```

　　**simx_opmode_streaming**: non-blocking mode.  Similar to simx_opmode_oneshot, but with the difference that the command will be stored on the server side , continuously executed, and continuously sent back to the client. This mode is often used with "get-functions" (e.g. simxGetJointPosition), where the user requires a specific value constantly.

　　**simx_opmode_buffer**: non-blocking mode. No command is sent to the server, but just a reply to a same command, previously executed. This mode is often used in conjunction with the simx_opmode_streaming mode: first, a constant command execution is started with a streaming command, then only command replies fetched.

　　Following diagram illustrates data streaming:

![img](https://bbsmax.ikafan.com/static/L3Byb3h5L2h0dHBzL2ltYWdlczIwMTUuY25ibG9ncy5jb20vYmxvZy84OTA5NjYvMjAxNzAzLzg5MDk2Ni0yMDE3MDMwMTExMDExOTI5OC0xOTg5MDI0OTAyLnBuZw==.jpg)

　　当完成任务后，客户端需要主动发送请求停止数据流（otherwise the server will continue to stream unessesary data and eventually slow down）。使用simx_opmode_discontinue操作模式来停止数据流。**simx_opmode_discontinue**: non-blocking mode. This mode is used to interrupt streaming commands.

## 2.2 电机控制

1、vrep关节种类
一共有四种关节类型：revolute joint、prismatic joint、screw、spherical joint
screw不能在torque/force模式下运行；
spherical joint仅能够在torque/force模式下运行。

2、vrep关节模式
一共有四种模式：

(1)、passive mode（被动模式）
在这种该模式下，关节不能直接被控制，而是将作为一个固定连接，我们可以使用API函数（比如： simSetJointPositon 、 simSetSphericalJointMatrix).）改变关节的位置。

(2)、inverse kinematics mode （逆运动学模式）
在这种模式下，关节充当被动关节，但在反向运动学计算中使用或者调整。

(3)、dependent mode（依赖模式）
在这种模式下，关节的位置将直接通过一个线性方程，依赖于其他关节。

(4)、torque or force mode（扭矩或力模式）
在这种模式下，关节由动态学模块模拟，当且仅当关节开启动态使能（dynamically enabled）的时候。当动态使能的时候，关节是自由的或者可以通过force/torque、velocity、position进行控制

1）the joint motor is disabled
当关节的电机禁用（joint motor is disabled）的时候，关节是自由的，并且仅受它自己的限制。

2）the joint’s motor is enabled,but the control loop is disabled
启用关节电动机并禁用控制回路后，如果关节能够传递最大扭矩/力，则关节将尝试达到所需的目标速度。

3）the joint’s motor is enabled,and the control loop is enabled
启用关节电动机并启用控制回路后，用户可以使用3种控制模式：
1、custom control
自定义控件：关节回调函数将负责控制关节的动态行为，使您可以使用任何可想象的算法来控制关节。
2、PID control
3、spring-damper mode(弹簧-阻尼器模式)
通过力/转矩调制，关节将像弹簧-阻尼器系统一样工作

3、vrep关节控制
控制关节的方式取决于关节的模式，下面通过对同关节的模式进行控制分析：

(1)、the joint is not force/torque mode
在这个模式下，我们可以直接或者间接地设置关节的位置—通过使用simxSetJointPosition这个API函数来设置。
使用函数如下：

vrep.setJointPosition(client_id, joint,90*math.pi/180,vrep.simx_opmode_streaming) ---- set the position to 90 degrees
1
(2)、the joint is in force/torque mode
关节设置在这种模式之下，并被动态启用（也就是说设置有动态特性），则它将由物理引擎间接处理。关节的动态特性主要包含有两种：电机特性（motor properties）和控制特性（control properties）；如果关节的电动机未被启用，则关节将不受控制（也就是说这个关节是自由的），否则的话，关节将存在下面这两种动态模式：

1)、the joint’s motor is enabled,but the control loop is disabled
在这种模式下，可以使用API函数simxSetJointTargetVelocity达到目标速度，使用API函数simSetJointForce达到指定的maximum force/torque。

2)、the joint’s motor is enabled,and the control loop is enabled
在这种模式下，关节可以在位置控制（例如PID控制）下运行，可以使用API函数simxSetJointTargetPosition达到物体的指定位置

(3)、总结
总的来说，vrep关节控制可以认为是分为以上三种情况，这三种情况下分别使用不同的函数去对我们的关节进行设置。

————————————————
版权声明：本文为CSDN博主「weixin_45650561」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_45650561/article/details/108417417

# 第三章：位姿描述与变换

机器人的位姿描述与坐标变换是进行工业机器人运动学和动力学分析的基础。本节简要介绍上述内容，明确位姿描述和坐标变换的关系，用到的基本数学知识就是——矩阵。

## 3.1 位姿表示

位姿代表位置和姿态。任何一个刚体在空间坐标系(OXYZ)中可以用位置和姿态来精确、唯一表示其位置状态。

- 位置：x、y、z坐标
- 姿态：刚体与OX轴的夹角rx、与OY轴的夹角ry、与OZ轴的夹角rz

假设基坐标系为OXYZ，刚体坐标系为O`X`Y`Z`。对于机器人而言，空间中的任何一个点都必须要用上述六个参数明确指定，即(x,y,z,rx,ry,rz)，即便(x,y,z)都一样，(rx,ry,rz)不同代表机器人以不同的姿态去到达同一个点。

刚体的位置可以用一个3x1的矩阵来表示，即刚体坐标系中心O`在基坐标系中的位置，即

![img](https://pic4.zhimg.com/80/v2-4a1e70a20f2aa8c7f2751ea765397903_1440w.png)

刚体的姿态可以用一个3x3的矩阵来表示，即刚体坐标系在基坐标系中的姿态，即

![img](https://pic2.zhimg.com/80/v2-290d9ab8929891ee0ffbd98c4b3fc375_1440w.jpg)

其中，第一列表示刚体坐标系的O`X`轴在基坐标系的三个轴方向上的分量，称为**单位主矢量**。同理，第二列和第三列分别是刚体坐标系的O`Y`轴和O`Z`轴在基坐标系的三个轴方向上的分量。

举个例子，在下图中，刚体M沿坐标系O中平移了（0,20,15），绕Z轴旋转了90度，因此刚体M在坐标系O的位姿可描述为：

![img](https://pic2.zhimg.com/80/v2-7f40f7a9853f883d3ca16d25a068c495_1440w.jpg)

![img](https://pic2.zhimg.com/80/v2-d9ef206c0cdc04eec9107b67e931db99_1440w.png)

根据上面的例子，很容易得到，刚体坐标系绕X轴（Y轴、Z轴）旋转角度θ后的姿态矩阵为：

![img](https://pic3.zhimg.com/80/v2-6a1324c6383a9189dfb4341ebb442c1a_1440w.png)

## 3.2 齐次坐标与齐次矩阵

### 3.2.1 齐次坐标

![img](https://pic3.zhimg.com/80/v2-8eada188c9a48831561999278713f03a_1440w.jpg)

其中，x=a/w, y=b/w, z=c/w 。

- 点的齐次坐标

对于某一个点(10,20,30)，它的齐次坐标可以表示为

![img](https://pic3.zhimg.com/80/v2-dc1f8cfc10711e227ee822fa25d10f92_1440w.jpg)

- 坐标轴的齐次坐标

![img](https://pic3.zhimg.com/80/v2-4871434e3bba96e9683274713dfaecbe_1440w.jpg)

### 3.2.2 齐次矩阵

机器人学中，用齐次矩阵（4x4）来统一描述刚体的位置和姿态，如下图。通过矩阵的正逆变换和矩阵相乘操作，实现位姿的变换。

![img](https://pic1.zhimg.com/80/v2-dee465f9324b91791a844c3ddbfbf4d4_1440w.png)

其中，**前面的3x3矩阵代表刚体的姿态，后面的3x1矩阵代表刚体的位置**。

### 3.2.3 齐次变换

有了上述基础，接下来可以用齐次变换来描述刚体在空间中的位姿变换了。齐次矩阵不仅可以描述刚体在空间中的位姿，还可以描述位姿变换过程，比如“绕某某坐标系的X轴旋转43°，并且绕Y轴旋转-89°”。齐次变换分为平移变换、旋转变换以及前两者的结合。

#### 3.2.3.1 平移变换

平移变换较为简单，比如坐标系j相对坐标系i的x、y、z分别平移10,-20,30，用齐次矩阵表示如下：

![img](https://pic3.zhimg.com/80/v2-976eb4f1ca31e0f5a9e4b2677fae4dfa_1440w.jpg)

其中，矩阵位置可以交换，因为这是三个相互独立的变量，交换后不影响结果。

#### 3.2.3.2 旋转变换

- 例1：坐标系j相对坐标系i的X轴旋转90°，齐次矩阵描述如下：

![img](https://pic3.zhimg.com/80/v2-42a14ca278ab2cf20fc0034e214bf006_1440w.jpg)

- 例2：坐标系j相对坐标系i的X轴旋转90°，并绕坐标系i的Y轴旋转90°，由例1得到“坐标系j相对坐标系i的X轴旋转90°”的变换描述，也容易得到“绕坐标系i的Y轴旋转90°”的变换描述。但是这两个矩阵能否像平移变换一样随意交换次序呢？答案是否定的，矩阵左乘和矩阵右乘的意义是不一样的：
- **变换算子左乘：表示该变换是相对固定坐标系变换；**
- **变换算子右乘：表示该变换是相对动的坐标系（新坐标系）变换**。

需要解释的是，我们把上述的平移变换和旋转变换称为变换算子。

根据上述原则，则例2中，两个变换都是绕坐标系i的变换，是绕固定坐标系的变换，变换算子应该左乘。假设刚体j原位姿的齐次矩阵描述为P，那么经历“坐标系j相对坐标系i的X轴旋转90°”后的描述为：

![img](https://pic2.zhimg.com/80/v2-130da2111c3f0d6f70ff645dfc9fb3a9_1440w.png)

即，变换算子左乘。接下来第二个变换是“绕坐标系i的Y轴旋转90°”，也应该左乘：

![img](https://pic3.zhimg.com/80/v2-a06cc3f293dd2c1e9c48d104622ebb0a_1440w.png)

- 例3：坐标系j相对坐标系i的X轴旋转90°，并绕坐标系j的Y轴旋转90°。

这一题与例2的区别在于第二个变换改成了“绕坐标系j的Y轴旋转90°”。首先第一个变换没啥变换，与例2的第一个变换一样，绕固定坐标系旋转，左乘。第二个变换应该是：

![img](https://pic4.zhimg.com/80/v2-5591856a2dd5dca7a25af1edc7c45fb3_1440w.jpg)

#### 3.2.3.3 平移＋旋转变换

这里平移变换算子可以直接加到旋转变换算子里（试试就知道了，平移与旋转是相对独立的）。这里既然讲到平移与旋转的综合变换，不如说下“已知刚体i的空间位姿参数为（x,y,z,rx,ry,rz），如何用齐次矩阵来描述？”这就好比刚体坐标系j与固定坐标系i最开始完全重合，然后刚体j沿坐标系i的X、Y、Z方向分别移动距离x，y和z，并且绕坐标系i的X轴、Y轴、Z轴分别旋转rx、ry和rz。

![img](https://pic1.zhimg.com/80/v2-cfb3baf35d0ef6b842d18351282bec18_1440w.jpg)

![img](https://pic4.zhimg.com/80/v2-b509cfc79e4d96f939193d6117228d3f_1440w.jpg)

讲到这里，机器人的位姿描述与坐标变换也就基本结束了。上述知识是进行机器人运动学分析、动力学分析、机器人离线编程软件开发等的基础。尤其在机器人逆运动学分析和仿真过程、工业现场手眼标定等场合，齐次矩阵的变换尤其重要。有了上述基础，再去看Jungle之前的两篇文章：



# 第四章：正运动学

## 4.1 三轴机械臂



## 4.2 六轴机械臂

正运动学是已知关节六个角度求变换矩阵T

其中：

![img](https://img-blog.csdn.net/20180818104404889?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

整理得：

![img](https://img-blog.csdn.net/2018072114161724?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

带入DH参数，求解：

![img](https://img-blog.csdn.net/20180721141732317?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)![img](https://img-blog.csdn.net/20180721141751261?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)![img](https://img-blog.csdn.net/20180721141813319?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721141834152?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)   ![img](https://img-blog.csdn.net/20180914153421357?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  ![img](https://img-blog.csdn.net/20180721141914462?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

最终变换矩阵：

![img](https://img-blog.csdn.net/20180721142022996?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

正运动学求解完毕。

# 第五章：逆运动学

## 5.1 三轴机械臂

### 5.1.1 代数解

计算机器人运动学逆解首先要考虑可解性(solvability)，即考虑无解、多解等情况。在机器人工作空间外的目标点显然是无解的。对于多解的情况从下面的例子可以看出平面二杆机械臂（两个关节可以360°旋转）在工作空间内存在两个解：

 ![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWFnZXMyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvODkwOTY2LzIwMTgwOC84OTA5NjYtMjAxODA4MTAwOTA4MTg0MTAtMzUwNzMwOTg2LnBuZw?x-oss-process=image/format,png)

　　如果逆运动学有多个解，那么控制程序在运行时就必须选择其中一个解，然后发给驱动器驱动机器人关节旋转或平移。如何选择合适的解有许多不同的准则，其中一种比较合理的方法就是选择“最近”的解（the closest solution）。如下图所示，如果机器人在A点，并期望运动到B点，合理的解是关节运动量最小的那一个（A good choice would be the solution that minimizes the amount that each joint is required to move）。因此在不存在障碍物的情况下，上面的虚线构型会被选为逆解。在计算逆解时我们可以考虑将当前位置作为输入参数，这样我们就可以选择关节空间中离当前位置最近的解。

　　这个“最近”有多种定义方式。比如对于典型的6自由度关节型机器人来说，其前三个关节较大，后三个关节较小。因此在定义关节空间内的距离远近时要考虑给不同关节赋予不同的权重，比如前三个关节设置大权重，后三个关节设置小权重。那么在选择解的时候会优先考虑移动较小的关节而非移动大关节。而当存在障碍物时，“最近”的解的运动路径会与其发生碰撞，这时就要选择另一个运动距离较远的解（"farther" solution）。因此在考虑碰撞、路径规划等问题时我们需要计算出可能存在的全部解。
![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWFnZXMyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvODkwOTY2LzIwMTgwOC84OTA5NjYtMjAxODA4MTAwOTA4MjQ4MTQtMTE4MDkzMjM2MC5wbmc?x-oss-process=image/format,png)

　逆解个数取决于机器人关节数目（the number of joints）、机器人的构型（link parameters）以及关节运动范围(the allowable ranges of motion of the joints)。决定机器人构型的D-H参数表中的非零值越多，就有越多的解存在。对于通用型6轴转动关节的机械臂来说，最多可能存在16个不同的解。下图展示了最大解的数量与非零值的连杆长度参数aa （两关节转轴之间的最短距离，即两轴线之间公垂线的长度）的数量之间的关系：

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWFnZXMyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvODkwOTY2LzIwMTgwOC84OTA5NjYtMjAxODA4MTAxMDE4MjU3NjAtMjEyMzQ1MDA1MS5wbmc?x-oss-process=image/format,png)

另外机器人逆运动学求解也有多种方法，一般分为两类：封闭解（closed-form solutions）和数值解（numerical solutions）。不同学者对同一机器人的运动学逆解也提出不同的解法。应该从计算方法的计算效率、计算精度等要求出发，选择较好的解法。通常来说数值迭代解法比计算封闭解的解析表达式更慢、更耗时，因此在设计机器人的构型时就要考虑封闭解的存在性。

 　　求解逆运动学方程的解析解（给出解的具体函数形式，从解的表达式中就可以算出任何对应值）时主要采用代数法（Algebraic solution）或几何法（Geometric solution）。下面我们先用代数法来计算平面二连杆机械臂的运动学逆解（不考虑末端关节的旋转）。正向运动学很容易得到：

x=l1c1+l2c12y=l1s1+l2s12x=l1c1+l2c12y=l1s1+l2s12

 

　　将上面方程两边取平方再相加得到x2+y2=l21+l22+2l1l2c2x2+y2=l12+l22+2l1l2c2 ，消除θ1θ1 。这里用到了三角函数的和差角公式：

c12=c1c2−s1s2s12=s1c2+c1s2c12=c1c2−s1s2s12=s1c2+c1s2

 

　　可以求得cosθ2cos⁡θ2 ：

c2=x2+y2−l21−l222l1l2c2=x2+y2−l12−l222l1l2

 

　　为了使解存在，上式的值必须在-1~1之间，因为余弦函数cosxcos⁡x 的取值范围就是[−1,1][−1,1] 。在计算逆解时需要检查这一条件，当不满足时说明目标位置已经位于工作空间之外（the goal point is too far away for the manipulator to reach）。当目标位置(x,y)(x,y) 位于工作空间内时可以求得sinθ2sin⁡θ2 ：

s2=±1−c22−−−−−√s2=±1−c22

 

　　为了计算θ2θ2 ，可以使用Atan2函数，即：

θ2=Atan2(s2,c2)θ2=Atan2(s2,c2)

 

　　注意对于tan(θ) = y / x ，两种反正切函数的区别是：θ = ATan(y / x)求出的θ取值范围是(−π2,π2)(−π2,π2) ；θ = ATan2(y, x)求出的θ取值范围是(−π,π](−π,π] 。

当 (x, y) 在第一象限, 0 < θ < PI/2

当 (x, y) 在第二象限 PI/2 < θ≤PI

当 (x, y) 在第三象限, -PI < θ < -PI/2

当 (x, y) 在第四象限, -PI/2 < θ < 0

　　s2s2 的符号有两种选择，对应的我们可以选择"elbow-up"或"elbow-down"两种不同构型。求出θ2θ2 后我们可以根据正解方程再计算出θ1θ1 。将正解方程改写为

x=k1c1−k2s1y=k1s1+k2c1x=k1c1−k2s1y=k1s1+k2c1

 

　　其中

k1=l1+l2c2k2=l2s2k1=l1+l2c2k2=l2s2

 

　　为了求解方程对k1k1 、k2k2 进行变量替换：

k1=rcosγk2=rsinγk1=rcos⁡γk2=rsin⁡γ

 

　　其中r=k21+k22−−−−−−√r=k12+k22 ，γ=Atan2(k2,k1)γ=Atan2(k2,k1)

　　于是正解方程可写为：

xr=cosγcosθ1−sinγsinθ1yr=cosγsinθ1+sinγcosθ1xr=cos⁡γcos⁡θ1−sin⁡γsin⁡θ1yr=cos⁡γsin⁡θ1+sin⁡γcos⁡θ1

 

　　因此有：

cos(γ+θ1)=xrsin(γ+θ1)=yrcos⁡(γ+θ1)=xrsin⁡(γ+θ1)=yr

 

　　使用Atan2函数可得到：γ+θ1=Atan2(y,x)γ+θ1=Atan2(y,x)

　　于是第一个关节的转角θ1θ1 为：

θ1=Atan2(y,x)−Atan2(k2,k1)=Atan2(y,x)−Atan2(l2s2,l1+l2c2)θ1=Atan2(y,x)−Atan2(k2,k1)=Atan2(y,x)−Atan2(l2s2,l1+l2c2)

　　注意之前在求解θ2θ2 时对s2s2 的符号进行了选择，这会引起k2k2 符号的变化，并影响θ1θ1 的求解。另外当x=y=0时，函数Atan2是未定义的状态，这种情况下θ1θ1 可以任意取值。

### 5.1.2 几何解

根据机构平面图，由L1L1 、L2L2 以及原点与末端之间的连线构成的三角形的余弦定理可求得θ2θ2 ：

x2+y2=l21+l22−2l1l2cos(180∘+θ2)x2+y2=l12+l22−2l1l2cos⁡(180∘+θ2)

 ![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWFnZXMyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvODkwOTY2LzIwMTgwOC84OTA5NjYtMjAxODA4MTAxMzUxMjQ2MDAtNTU4NDczODY4LnBuZw?x-oss-process=image/format,png)

　　由于cos(180∘+θ2)=−cos(θ2)cos⁡(180∘+θ2)=−cos⁡(θ2) ，可解得：

c2=x2+y2−l21−l222l1l2c2=x2+y2−l12−l222l1l2

 

　　为了保证三角形存在（三角形两边之和大于第三边），即x2+y2−−−−−−√x2+y2 必须小于或等于连杆长度之和l1+l2l1+l2 。在求逆解时需要验证是否满足这一条件，判断解的存在性。另一个可能的解（虚线所示）与之对称，θ′2=−θ2θ2′=−θ2

　　为了计算θ1θ1 ，先求出图中的ββ 和ψψ 角。ββ 可能位于坐标系四象限中的任一象限，取决于xx 和yy 的符号，因此使用Atan2函数来求解：β=Atan2(y,x)β=Atan2(y,x)

　　对ψψ 用余弦定理来计算：

cosψ=x2+y2+l21−l222l1x2+y2−−−−−−√cos⁡ψ=x2+y2+l12−l222l1x2+y2

 

　　于是

θ1=β±ψθ1=β±ψ

 

　　当θ2<0θ2<0 时取正号，θ2>0θ2>0 时取负号


## 5.2 六轴机械臂

### 5.2.1 解析解

逆运动学是已知变换矩阵T，求六个关节角度 。逆运动学求解有解析法，几何法，迭代法，这里采用解析法求解。

2.1 两个简单的数学方法

2.1.1 求角度

 这个逆运动学算法求解的角度范围是

 

![img](https://img-blog.csdn.net/20180721142459706?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

因为标准的反正切arctan的值域是

![img](https://img-blog.csdn.net/20180721142633761?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

所以不能使用，这里介绍一个改进的反正切求法 Atan2(y, x)（Matlab里有这个函数）,它的值域可以满足要求。

2.1.2 解方程

![img](https://img-blog.csdn.net/20180721142904936?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

首先进行三角恒等变换，令

![img](https://img-blog.csdn.net/20180721143002979?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

其中：

![img](https://img-blog.csdn.net/20180721143031274?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

然后带入原方程：

![img](https://img-blog.csdn.net/20180721143122601?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

则

![img](https://img-blog.csdn.net/20180721143159420?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)2.2 约定

为了简化书写，约定：

![img](https://img-blog.csdn.net/20180721143540202?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

2.3 求解1，5，6关节角度

已知：

![img](https://img-blog.csdn.net/20180721143829202?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721143906417?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

则

![img](https://img-blog.csdn.net/20180721144046396?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

其中：

![img](https://img-blog.csdn.net/20180721144117381?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

等式左边：

![img](https://img-blog.csdn.net/20180721144212314?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

等式右边：

![img](https://img-blog.csdn.net/20180721144239883?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)2.3.1 求关节角1

利用等式左右两边第3行，第4列对应相等求关节角1。

利用等式左右两边第3行，第4列对应相等求关节角1。

![img](https://img-blog.csdn.net/20180721144406789?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

整理得：

![img](https://img-blog.csdn.net/2018072114443457?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

设：

![img](https://img-blog.csdn.net/20180721144457247?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

则 

![img](https://img-blog.csdn.net/20180721144649322?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

根据前面介绍的解方程的方法：

![img](https://img-blog.csdn.net/20180721144726741?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

2.3.2 求关节角5

利用等式左右两边第3行，第3列对应相等求关节角5。

![img](https://img-blog.csdn.net/20180721152322379?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

解得：

![img](https://img-blog.csdn.net/20180721152348285?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

2.3.3 求关节角6

利用等式左右两边第3行，第1列对应相等求关节角6。

![img](https://img-blog.csdn.net/2018072115251562?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)设：

![img](https://img-blog.csdn.net/20180721152541856?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

则

![img](https://img-blog.csdn.net/20180721152619648?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)根据前面介绍的方法：

![img](https://img-blog.csdn.net/20180721153045382?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

其实可以通过化简得到式中

![img](https://img-blog.csdn.net/20180721153118393?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

则

![img](https://img-blog.csdn.net/20180721153214590?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

2.4 求解2，3，4关节角度

已知：

![img](https://img-blog.csdn.net/20180721143829202?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721143906417?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

则

![img](https://img-blog.csdn.net/20180721153359848?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

其中：

![img](https://img-blog.csdn.net/20180721153431571?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

等式左边等于

![img](https://img-blog.csdn.net/20180721153505490?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

等式右边等于

![img](https://img-blog.csdn.net/20180721153544527?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

2.4.1 求解关节角3

利用等式左右两边第1行，第4列对应相等，第2行，第4列对应相等，求关节角3。

![img](https://img-blog.csdnimg.cn/20190318192830244.png)

为了简化，设：

![img](https://img-blog.csdnimg.cn/20190318193119509.png)

将m,n带入上式得

![img](https://img-blog.csdn.net/20180721153912205?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

式子③④平方和为

![img](https://img-blog.csdn.net/20180721153939788?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

因为

![img](https://img-blog.csdn.net/20180721154051822?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

所以

![img](https://img-blog.csdn.net/20180721154132270?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

2.4.2 求解关节角2

将③④展开得：

![img](https://img-blog.csdn.net/20180721155031124?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

将关节角3带入⑤⑥，求关节角2得

![img](https://img-blog.csdn.net/20180721155201242?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

则

![img](https://img-blog.csdn.net/20180721155230928?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

2.4.3 求解关节角4

用![img](https://img-blog.csdn.net/20180721155412745?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)的第2行第2列，第1行第2列求 ![img](https://img-blog.csdn.net/20180721155435144?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721155512236?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

则

![img](https://img-blog.csdn.net/20180721155536650?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

2.5 总结

2.5.1 求解公式

![img](https://img-blog.csdn.net/20180721144457247?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721144726741?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721152348285?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721152541856?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721153214590?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721153820815?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721154132270?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721155201242?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721155230928?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721155536650?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

2.5.2 奇异位置

1.肩关节奇异位置

![img](https://img-blog.csdn.net/20180721152541856?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180721160459174?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

此时末端执行器参考点O6位于轴线z1和z2构成的平面内，关节角1无法求解。

2.肘关节奇异位置

![img](https://img-blog.csdn.net/20180721153820815?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)![img](https://img-blog.csdn.net/20180721161254353?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

此时关节角2无法求解。

3.腕关节奇异位置

![img](https://img-blog.csdn.net/20180721160856931?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zlbmd5dTE5OTMwOTIw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)此时轴线z4和z6平行，关节角6无法求解。

### 5.2.2 数值解

#### 5.2.2.1 Jacobian Transpose Method

机器人运动学逆解的问题经常出现在动画仿真和工业机器人的轨迹规划中：We want to know how the upper joints of the hierarchy would rotate if we want the end effector to reach some goal.

![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161010081818836-1058930027.png)

IK Solutions：

- Analytical solutions are desirable because of their speed and exactness of solution.
- For complex kinematics problems, analytical solutions may not be possible.
- Use iterative methods (迭代法)--Optimization methods (e.g., minimize the distance between end effector and goal point)

　　机器人学的教材上一般只介绍了运动学逆解的解析解法，很少涉及数值解（迭代解法）。其中有两方面的原因，一是数值解相对于解析解需要的运算量更大，不太适合实时性要求较高的场合；另一方面是因为一般在设计机器人的结构时就会考虑其逆解的可解性，比如相邻的三个关节轴线相交即存在解析解。下面以最简单的二连杆机构为例子，研究一下机器人运动学逆解的数值解法。如下图所示，其运动学正解很容易得到，根据运动学正解可以写出机器人的雅克比矩阵**J**。

![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161009173052997-1060265767.png)

What is Jacobian? A linear approximation to f(x). 雅克比矩阵相当于函数f(x)的一阶导数，即线性近似。

![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161010082310508-2061507753.png)

Computing the Jacobian Numerically:（**[雅克比矩阵的计算](http://www.cnblogs.com/21207-iHome/p/5948659.html)**有解析法和数值法，当难以根据解析法得到雅克比时可以用差分法代替微分求解）

![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161010082428008-1637522219.png)

下面是Jacobian Transpose方法的主要推导过程：

![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161009173530501-145563332.png)

　　It is recommended that you choose a small positive scalar α < 1 and update the joint angles θ by adding Δθ. Then proceed iteratively by recomputing the Jacobian based on the updated angles and positions, finding new values for Δθ and again updating with a small fraction α. This is repeated until the links are sufficiently close to the desired positions. The question of how small α needs to be depends on the geometry of the links; it would be a good idea to keep α small enough so that the angles are updated by at most 5 or 10° at a time.

　　这一方法运用了最速降法（梯度法）的思想，利用目标函数在迭代点的局部性态，每步搜索都沿着函数值下降最快的方向，即负梯度方向进行搜索。迭代过程的几何概念较为直观，方法和程序简单，容易实现，不足之处是每次迭代都是沿着迭代点的负梯度方向搜索，搜索路径较为曲折，收敛慢。

**Operating Principle:**  

Project difference vector D**X** on those dimensions qwhich can reduce it the most. It is a plausible, justifyable approach, because it is related to the method of steepest decent.( It follows a force that pulls the end-effector towards its desired target location).

**Advantages:**
\1. Simple computation (numerically robust)
\2. No matrix inversions

**Disadvantages:**
\1. Needs many iterations until convergence in certain configurations 
\2. Unpredictable joint configurations
\3. Non conservative

 

　　下面以V-rep中官方自带的例子（在文件夹scenes/ik_fk_simple_examples中）为基础进行修改，添加代码手动实现运动学逆解的求解。为了实现同样的功能先将两个旋转关节从Inverse kinematics mode设为Passive mode，然后将target和tip的Linked dummy设为none，并在Calculation Modules的Inverse kinematics选项卡中取消IK groups enabled。下图中红色的dummy为target dummy，仿真开始后程序会计算连杆末端（tip dummy）与target之间的误差，然后根据Jacobian Transpose方法不断计算关节调整量，直到误差小于容许值。

![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161009173749557-2062036679.png)

　　如下图所示，迭代计算61次收敛后，点击图中的Compute IK按钮，连杆末端能根据计算出的关节角q1,q2移动到target的位置（可以随意拖动target的位置，在合理的范围内经过逆解计算tip都会与target重合）

![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161009173801668-823883227.png)

在child script中由lua API实现了该方法

 

![复制代码](https://common.cnblogs.com/images/copycode.gif)

```
if (sim_call_type==sim_childscriptcall_initialization) then
    ui=simGetUIHandle('UI')
    J1_handle = simGetObjectHandle('j1')
    J2_handle = simGetObjectHandle('j2')
    target_handle = simGetObjectHandle('target')
    consoleHandle = simAuxiliaryConsoleOpen('info', 5, 2+4, {100,100},{800,300})
    
    --link length
    L1 = 0.5
    L2 = 0.5

    gamma = 1       --step size
    stol = 1e-2     --tolerance
    nm = 100        --initial error
    count = 0       --iteration count
    ilimit = 1000   --maximum iteratio
    
    --initial joint value
    q1 = 0   
    q2 = 0
end


if (sim_call_type==sim_childscriptcall_actuation) then
    local a=simGetUIEventButton(ui)
    local target_pos = simGetObjectPosition(target_handle, -1)

    if(nm > stol) 
    then
        simAuxiliaryConsolePrint(consoleHandle, nil)

        local x, y = L1*math.cos(q1)+L2*math.cos(q1+q2), L1*math.sin(q1)+L2*math.sin(q1+q2)
        local delta_x, delta_y = target_pos[1] - x, target_pos[2] - y
        local dq_1 = (-L1*math.sin(q1)-L2*math.sin(q1+q2))*delta_x + (L1*math.cos(q1)+L2*math.cos(q1+q2))*delta_y
        local dq_2 = (-L2*math.sin(q1+q2))*delta_x + (L2*math.cos(q1+q2))*delta_y
        q1, q2 = q1 + gamma*dq_1,  q2 + gamma*dq_2

        nm = math.sqrt(delta_x * delta_x + delta_y * delta_y)

        count = count + 1
        if count > ilimit   then
            simAuxiliaryConsolePrint(consoleHandle,"Solution wouldn't converge\r\n")
        end

        simAuxiliaryConsolePrint(consoleHandle, string.format("q1:%.2f", q1*180/math.pi)..'  '..string.format("q2:%.2f", q2*180/math.pi)..'\r\n') 
        simAuxiliaryConsolePrint(consoleHandle, string.format("x:%.2f",x)..'  '..string.format("y:%.2f", y)..'\r\n') 
        simAuxiliaryConsolePrint(consoleHandle, string.format("%d", count)..'iterations'..'  '..string.format("err:%.4f", nm)..'\r\n')   
    end

    -- if the button(a is the button handle) is pressed
    if a==1 then
        simSetJointPosition(J1_handle, q1+math.pi/2)  -- the angle between L1 and X-axis is 90 degree
        simSetJointPosition(J2_handle, q2)      
    end
end
```

#### 5.2.2.2 Pseudo Inverse Method

There are two ways of using the Jacobian matrix to solve kinematics. One is to use the transpose of the Jacobian **JT**. The other is to calculate the inverse of the Jacobian **J**-1. **J** is most likely redundant and non square,thus an ordinary inverse is not possible. We can try using the pseudo inverse to find a matrix that effectively inverts a non square matrix. **J**+ is the pseudoinverse of **J**, also called the Moore-Penrose inverse of **J** . It is defined for all matrices **J** , even ones which are not square or not of full row rank.

　　雅可比矩阵将关节空间速度映射到直角坐标空间：Δ**P = J(θ)**Δ**θ**。对于机器人运动学逆解来说可以考虑求雅克比矩阵**J**的逆，然后根据Δ**θ=J(θ)**-1Δ**P**计算出关节角变动量并反复迭代。然当很多情况下**J**不可逆，因此可以考虑求其广义逆（Moore-Penrose逆）来求解方程。设**A**∈**C**m×n，**b**∈**C**m，则线性方程组**Ax**=**b**有解的充分必要条件是**A\**A\**\**+\**\**b\****=**b**，且通解为**x**=**A****+****b +** (***I\*-\**\*\*A\*\*\*\*+\*\*A\*\*\*\*\****)**y** (**y**∈**C**n任意)，并且它的唯一极小范数解为**x****0** = **A+b**（矩阵论简明教程 P150 A+在解线性方程组中的应用）。根据矩阵论（《矩阵论简明教程 第二版》 科学出版社 第6章 广义逆矩阵），设**J**为m×n阶实矩阵，当rank**J**=m时，有**J+ = JT(J J****T)-1**；而当rank**J**=n时，有**J+ = (JTJ )-1 JT**，此时方程组**J(θ)**Δ**θ****=Δ\**P\****的解唯一。 对一般机器人来说n≥m，且rank**J**=m，即有**J+ = JT(J J****T)-1**。当n>m，即机构驱动数目多于末端自由度时，会出现多解的情况，pseudo inverse方法会寻找解向量中长度最小的一个（无穷多个解中2范数最小的解，即||Δ**θ**0||2=min||Δ**θ**||2，称为极小范数解）

　Let  Δ**P** be **e = t - P**,where **t** is the target position,**P** is the end effector position and e is the desirable change of the end effector. The first iteration will result in a new **θ** from equation Δθ=J(θ)-1ΔP. By using forward kinematics a new position **P** of the end effector is acquired and a new iteration begins. This is done until either **e** is small enough or the end effector does not move. 使用Pseudo Inverse方法求机器人逆解的基本步骤如下所示：

![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161010075342852-490524363.png)

**Operating Principle**:
\1. Shortest path in q-space
**Advantages:**
\1. Computationally fast (second order method)
**Disadvantages:**
\1. Matrix inversion necessary (numerical problems)
\2. Unpredictable joint configurations
\3. Non conservative

　　The pseudoinverse tends to have stability problems in the neighborhoods of singularities. At a singularity, the Jacobian matrix no longer has full row rank, corresponding to the fact that there is a direction of movement of the end effectors which is not achievable. If the configuration is exactly at a singularity, then the pseudoinverse method will not attempt to move in an impossible direction, and the pseudoinverse will be well-behaved. However, if the configuration is close to a singularity, then the pseudoinverse method will lead to very large changes in joint angles, even for small movements in the target position. In practice, roundoff errors mean that true singularities are rarely reached and instead singularity have to be detected by checking values for being near-zero. 对于平面二连杆机构，当θ2趋近于0°或180°时，机械手接近奇异形位，关节J2速度将趋于无穷大。（参考John J.Craig. *Introduction to Robotics: Mechanics and Control* Chapter 5-->Section 5.8 Singularities）

　　下面使用同样的模型验证Pseudo Inverse方法。从输出窗口可以看出，该方法迭代次数相比Jacobian Transpose法明显减少（迭代5次就达到精度要求）。The Jacobian pseudoinverse method is equivalent to solving by Newton's method.(相当于牛顿法)。Jacobian transpose is also related to solution by the method of steepest descent.（相当于最速降法或梯度法）。牛顿法是梯度法的进一步发展，梯度法在确定搜索方向时只考虑目标函数在迭代点的局部性质，即只利用一阶偏导数的信息，而牛顿法进一步利用了目标函数的二阶偏导数，考虑了梯度的变化趋势，因而可以更为全面的确定合适的搜索方向，以便很快的搜索到极小点。

![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161011223613796-130155719.png)

```
import vrep             #V-rep library
import sys      
import time
import math  
import numpy as np

# Starts a communication thread with the server (i.e. V-REP). 
clientID=vrep.simxStart('127.0.0.1', 20001, True, True, 5000, 5)

# clientID: the client ID, or -1 if the connection to the server was not possible
if clientID!=-1:  #check if client connection successful
    print 'Connected to remote API server'
else:
    print 'Connection not successful'
    sys.exit('Could not connect')    # Exit from Python


# Retrieves an object handle based on its name.
errorCode,J1_handle = vrep.simxGetObjectHandle(clientID,'j1',vrep.simx_opmode_oneshot_wait)
errorCode,J2_handle = vrep.simxGetObjectHandle(clientID,'j2',vrep.simx_opmode_oneshot_wait)
errorCode,target_handle = vrep.simxGetObjectHandle(clientID,'target',vrep.simx_opmode_oneshot_wait)
errorCode,consoleHandle = vrep.simxAuxiliaryConsoleOpen(clientID,'info',5,1+4,None,None,None,None,vrep.simx_opmode_oneshot_wait)

uiHandle = -1
errorCode,uiHandle = vrep.simxGetUIHandle(clientID,"UI", vrep.simx_opmode_oneshot_wait)
buttonEventID = -1
err,buttonEventID,aux = vrep.simxGetUIEventButton(clientID,uiHandle,vrep.simx_opmode_streaming)


L1 = 0.5    # link length
L2 = 0.5
gamma = 1       # step size
stol = 1e-2     # tolerance
nm = 100        # initial error
count = 0       # iteration count
ilimit = 1000   # maximum iteration


# initial joint value
# note that workspace-boundary singularities occur when q2 approach 0 or 180 degree
q = np.array([0,1])   


while True:
    retcode, target_pos = vrep.simxGetObjectPosition(clientID, target_handle, -1, vrep.simx_opmode_streaming)


    if(nm > stol):
        vrep.simxAuxiliaryConsolePrint(clientID, consoleHandle, None, vrep.simx_opmode_oneshot_wait) # "None" to clear the console window

        x = np.array([L1*math.cos(q[0])+L2*math.cos(q[0]+q[1]), L1*math.sin(q[0])+L2*math.sin(q[0]+q[1])])
        error = np.array([target_pos[0],target_pos[1]]) - x

        J = np.array([[-L1*math.sin(q[0])-L2*math.sin(q[0]+q[1]), -L2*math.sin(q[0]+q[1])],\
                      [L1*math.cos(q[0])+L2*math.cos(q[0]+q[1]), L2*math.cos(q[0]+q[1])]])

        J_pseudo = np.dot(J.transpose(), np.linalg.inv(J.dot(J.transpose())))
        dq = J_pseudo.dot(error)
        q = q + dq

        nm = np.linalg.norm(error)

        count = count + 1
        if count > ilimit:
            vrep.simxAuxiliaryConsolePrint(clientID,consoleHandle,"Solution wouldn't converge\r\n",vrep.simx_opmode_oneshot_wait)
        vrep.simxAuxiliaryConsolePrint(clientID,consoleHandle,'q1:'+str(q[0]*180/math.pi)+' q2:'+str(q[1]*180/math.pi)+'\r\n',vrep.simx_opmode_oneshot_wait)  
        vrep.simxAuxiliaryConsolePrint(clientID,consoleHandle,str(count)+' iterations'+'  err:'+str(nm)+'\r\n',vrep.simx_opmode_oneshot_wait)   


    err, buttonEventID, aux = vrep.simxGetUIEventButton(clientID,uiHandle,vrep.simx_opmode_buffer)    
    if ((err==vrep.simx_return_ok) and (buttonEventID == 1)):
        '''A button was pressed/edited/changed. React to it here!'''
        vrep.simxSetJointPosition(clientID,J1_handle, q[0]+math.pi/2, vrep.simx_opmode_oneshot )  
        vrep.simxSetJointPosition(clientID,J2_handle, q[1], vrep.simx_opmode_oneshot )
        
        '''Enable streaming again (was automatically disabled with the positive event):'''
        err,buttonEventID,aux=vrep.simxGetUIEventButton(clientID,uiHandle,vrep.simx_opmode_streaming)

    time.sleep(0.01)
```

　　上面使用Python Remote API来进行逆解计算并控制V-rep中的模型（因为涉及到矩阵求逆等运算，而我不太熟悉Lua的相关数值计算库）。需要注意的是要先在V-rep模型中调用函数simExtRemoteApiStart(portNumber)开启通信服务端，然后在Python程序的客户端进行连接。

#### 5.2.2.3 Damped Least Squares / Levenberg-Marquardt Method

The damped least squares method is also called the Levenberg-Marquardt method. Levenberg-Marquardt算法是最优化算法中的一种。它是使用最广泛的非线性最小二乘算法，具有梯度法和牛顿法的优点。当λ很小时，步长等于牛顿法步长，当λ很大时，步长约等于梯度下降法的步长。

　　The damped least squares method can be theoretically justified as follows.Rather than just finding the minimum vector ∆**θ** that gives a best solution to equation （pseudo inverse method就是求的极小范数解）, we find the value of ∆**θ** that minimizes the quantity：

![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161012172957968-1908346064.png)

where λ ∈ R is a non-zero damping constant. This is equivalent to minimizing the quantity：

****![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161012173009250-1025952627.png)****

The corresponding normal equation is（根据矩阵论简明教程P83 最小二乘问题：设**A**∈**R**m×n，**b**∈**R**m. 若**x**0∈***\*R\****n是**Ax**=**b**的最小二乘解，则**x**0是方程组**ATAx=ATb**的解，称该式为**Ax**=**b**的法方程组.）

****![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161012173017468-1738556088.png)****

This can be equivalently rewritten as：

![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161012173028109-932397158.png)

It can be shown that **J**T**J +** λ2**I** is non-singular when λ is appropriate（选取适当的参数λ可以保证矩阵**J**T**J +** λ2**I非奇异**）. Thus, the damped least squares solution is equal to：

****![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161012173037453-1007299622.png)****

Now **J**T**J** is an n × n matrix, where n is the number of degrees of freedom. It is easy to find that (**J**T**J +** λ2**I**)−1**J**T= **J**T (**J****J**T **+** λ2**I**)−1(等式两边同乘(**J**T**J +** λ2**I**)进行恒等变形). Thus：

![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161012173048890-565901500.png)

The advantage of the equation is that the matrix being inverted is only m×m where m = 3k is the dimension of the space of target positions, and m is often much less than n. Additionally, the equation can be computed without needing to carry out the matrix inversion, instead row operations can find **f** such that (**J****J**T **+** λ2**I**) **f** = **e** and then **J**T**f** is the solution. The damping constant depends on the details of the multibody and the target positions and must be chosen carefully to make equation numerically stable. The damping constant should large enough so that the solutions for ∆**θ** are well-behaved near singularities, but if it is chosen too large, then the convergence rate is too slow. 

　　以平面二连杆机构为例，使用同样的V-rep模型，将目标点放置在接近机构奇异位置处，使用DLS方法求逆解。在下面的Python程序中关节角初始值就给在奇异点上，可以看出最终DLS算法还是能收敛，而pseudo inverse方法在奇异点处就无法收敛。The damped least squares method avoids many of the pseudo inverse method’s problems with singularities and can give a numerically stable method of selecting ∆**θ**

![img](https://images2015.cnblogs.com/blog/890966/201610/890966-20161012205407421-64697141.png)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import vrep             #V-rep library
import sys      
import time
import math  
import numpy as np

# Starts a communication thread with the server (i.e. V-REP). 
clientID=vrep.simxStart('127.0.0.1', 20001, True, True, 5000, 5)

# clientID: the client ID, or -1 if the connection to the server was not possible
if clientID!=-1:  #check if client connection successful
    print 'Connected to remote API server'
else:
    print 'Connection not successful'
    sys.exit('Could not connect')    # Exit from Python


# Retrieves an object handle based on its name.
errorCode,J1_handle = vrep.simxGetObjectHandle(clientID,'j1',vrep.simx_opmode_oneshot_wait)
errorCode,J2_handle = vrep.simxGetObjectHandle(clientID,'j2',vrep.simx_opmode_oneshot_wait)
errorCode,target_handle = vrep.simxGetObjectHandle(clientID,'target',vrep.simx_opmode_oneshot_wait)
errorCode,consoleHandle = vrep.simxAuxiliaryConsoleOpen(clientID,'info',5,1+4,None,None,None,None,vrep.simx_opmode_oneshot_wait)

uiHandle = -1
errorCode,uiHandle = vrep.simxGetUIHandle(clientID,"UI", vrep.simx_opmode_oneshot_wait)
buttonEventID = -1
err,buttonEventID,aux = vrep.simxGetUIEventButton(clientID,uiHandle,vrep.simx_opmode_streaming)


L1 = 0.5        # link length
L2 = 0.5
lamda = 0.2     # damping constant
stol = 1e-2     # tolerance
nm = 100        # initial error
count = 0       # iteration count
ilimit = 1000   # maximum iteration


# initial joint value
# note that workspace-boundary singularities occur when q2 approach 0 or 180 degree
q = np.array([0,0])   


while True:
    retcode, target_pos = vrep.simxGetObjectPosition(clientID, target_handle, -1, vrep.simx_opmode_streaming)

    if(nm > stol):
        vrep.simxAuxiliaryConsolePrint(clientID, consoleHandle, None, vrep.simx_opmode_oneshot_wait) # "None" to clear the console window

        x = np.array([L1*math.cos(q[0])+L2*math.cos(q[0]+q[1]), L1*math.sin(q[0])+L2*math.sin(q[0]+q[1])])
        error = np.array([target_pos[0],target_pos[1]]) - x

        J = np.array([[-L1*math.sin(q[0])-L2*math.sin(q[0]+q[1]), -L2*math.sin(q[0]+q[1])],\
                      [L1*math.cos(q[0])+L2*math.cos(q[0]+q[1]), L2*math.cos(q[0]+q[1])]])

        f = np.linalg.solve(J.dot(J.transpose())+lamda**2*np.identity(2), error)
        
        dq = np.dot(J.transpose(), f)
        q = q + dq

        nm = np.linalg.norm(error)

        count = count + 1
        if count > ilimit:
            vrep.simxAuxiliaryConsolePrint(clientID,consoleHandle,"Solution wouldn't converge\r\n",vrep.simx_opmode_oneshot_wait)
        vrep.simxAuxiliaryConsolePrint(clientID,consoleHandle,'q1:'+str(q[0]*180/math.pi)+' q2:'+str(q[1]*180/math.pi)+'\r\n',vrep.simx_opmode_oneshot_wait)  
        vrep.simxAuxiliaryConsolePrint(clientID,consoleHandle,str(count)+' iterations'+'  err:'+str(nm)+'\r\n',vrep.simx_opmode_oneshot_wait)   


    err, buttonEventID, aux = vrep.simxGetUIEventButton(clientID,uiHandle,vrep.simx_opmode_buffer)    
    if ((err==vrep.simx_return_ok) and (buttonEventID == 1)):
        '''A button was pressed/edited/changed. React to it here!'''
        vrep.simxSetJointPosition(clientID,J1_handle, q[0]+math.pi/2, vrep.simx_opmode_oneshot )  
        vrep.simxSetJointPosition(clientID,J2_handle, q[1], vrep.simx_opmode_oneshot )
        
        '''Enable streaming again (was automatically disabled with the positive event):'''
        err,buttonEventID,aux=vrep.simxGetUIEventButton(clientID,uiHandle,vrep.simx_opmode_streaming)

    time.sleep(0.01)
```

# 第六章：轨迹插补

## 6.1 直线插补

## 6.2 圆弧插补

# 第七章：图像处理



