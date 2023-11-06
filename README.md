- 👋 Hi, I’m @zhuzhuc
- 👀 I’m interested in C++
- 🌱 I’m currently learning C+=
- 💞️ I’m looking to collaborate on C++
- 📫 My mail is :1727643988@qq.com
<!-- 动态打字效果 -->
<h1 align="center">
  <a href="https://github.com/zhuzhuc">  
    <img src="https://readme-typing-svg.herokuapp.com/?lines=Hello%2C%20World!;欢迎来到zzc的主页!&center=true&size=27">
  </a>
</h1>

<!-- 贪吃蛇代码贡献图 -->
<div align="center"><img src="https://tong-1306822294.cos.ap-beijing.myqcloud.com/tong/picture/202212222311275.svg" /></div>

  <p align="center">
    Visitor count<br><img src="https://profile-counter.glitch.me/zhuzhuc/count.svg" /> 
</p>


## Hey, I'm zzc 🙋
<!-- 敲代码的图片 -->
<div align="center" ><img order-radius="100px" src="https://tong-1306822294.cos.ap-beijing.myqcloud.com/tong/picture/202212222312468.gif"/></div>
<br>

<!-- 个人资料徽标 -->
<div align="center">
  <a href="https://v.kuaishou.com/cDejxp"><img src="https://img.shields.io/badge/website-%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%AB%99-blue"></a>&emsp;

<a href="https://www.zhihu.com/people/qian-lan-wa"><img src="https://img.shields.io/badge/zhihu-%E7%9F%A5%E4%B9%8E-blue"></a>&emsp;
<!-- 访客数统计徽标 -->   
  <img src="https://visitor-badge.glitch.me/badge?page_id=zhuzhuc" alt="访客统计" /></div>
  ## About Me :raised_hands:

- 🔭 一个菜鸡大学生（希望毕业顺利）
- 🤔 方向：后端服务器开发 | 软件开发
- ⚡ 个签：万千不如意，睡得着就过的去。 

</p>
```python
____ ____ ____ ____ ____ ____ ____ ____
||W |||e |||l |||c |||o |||m |||e |||! ||
||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|

### 📈 Github Statistics

<div align="center">
    <span>&emsp;&emsp;</span>
    <img height="175px" src="https://github-readme-stats.vercel.app/api?username=zhuzhuc&count_private=true&show_icons=true" />
    <span>&emsp;&emsp;</span>
    <img height="175px" src="https://github-readme-stats.vercel.app/api/top-langs/?username=zhuzhuc&layout=compact&langs_count=8" />
    <span>&emsp;&emsp;</span>
</div>
# My Awesome Repo

Welcome to my awesome repo! Here, I'm showcasing a motion carrier.

## Motion Carrier

The motion carrier below demonstrates a scrolling effect of the word "CARRIER":

<!-- 播放动画 -->
![Motion Carrier](motion_carrier.gif)

To generate this effect, I used GitHub Actions and Python. The code and setup instructions can be found in the [.github/workflows/motion_carrier.yml](.github/workflows/motion_carrier.yml) file.

Feel free to explore the code and customize it for your own use!
## 界面UI示例

下面是一个简单的猜数字游戏的文本界面UI示例：

```python
# 导入模块
import random

# 生成随机数字
random_number = random.randint(1, 100)

# 游戏循环
while True:
    # 获取用户输入
    guess = input("猜一个1到100之间的数字：")

    # 检查输入是否为数字
    if not guess.isdigit():
        print("请输入有效的数字！")
        continue

    # 将用户输入转换为整数
    guess = int(guess)

    # 比较用户猜测与随机数字
    if guess < random_number:
        print("数字太小了！")
    elif guess > random_number:
        print("数字太大了！")
    else:
        print("恭喜你，猜对了！")
        break



