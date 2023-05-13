<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <a href="https://github.com/Pears0nLee/SnakeMelon"><img src="docs/SnakeMelonico.png" width="200" height="200" alt="SnakeMelon"></a>
</p>

<div align="center">

# SnakeMelon
</div>
<p align="center">
  <a href="https://t.me/+T8ozejX9rnkwZDE1">
    <img src="https://img.shields.io/badge/telegram-SnakMelon-blue?style=flat-square" alt="Telegram">
  </a>
<div>
Python与西瓜之子--西瓜框架&amp;Python API,主要提供西瓜框架HTTP协议的部分功能,方便您使用Python语言快速快发.欢迎大家使用,让我们一起完善吧!
  

  
<div align="left">
  
# 说明文档

**目录架构**

```bash
SnakeMelon/               #SnakeMelon根目录
├── main.py               #主函数,入口函数
├── information.py        #Flask 默认端口5000
├── config.json           #配置文件
├── plugins/              #插件文件夹
│   ├── __init__.py       #SnakeMelon初始化函数,西瓜事件
│   ├── Points/           #积分系统
│   │   ├── __init__.py   #积分初始化函数,内置读写加减积分函数
│   │   └── data.json     #用于存放用户积分
│   ├── gretting.py       #本来想写欢迎使用,当作help来用吧,内容自行更改
│   └── points.py         #自动接收转账并转化为积分,只做例子,可自行更改触发条件(签到等等)
├── docs/                 #放乱七八糟的,说明文档,图标等等,没啥用
│   ├── SnakeMelon.png    #图标
│   └── ......            #......
├── requirements.txt      #依赖文件
└── README.md             #README.md   
```

