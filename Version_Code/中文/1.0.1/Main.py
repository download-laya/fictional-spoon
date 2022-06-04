# -*- coding: UTF-8 -*-

# from tkinter.messagebox import *
import os
import tkinter as tk
import wget
import easygui
from file_modification import *

root = tk.Tk()
root.title("fictional spoon主程序")

dir_if = os.path.exists('D:/MineCraftServer')
if dir_if:  # 此处直接调用 dir_if 是因为如果等于 True 就直接运行 if 语句
    enter = easygui.buttonbox(msg="虚构勺子官方下载路径为D:/MineCraftServer，我们检测到已有同名文件夹", title="Warning!",
                              choices=['我已知晓，立即退出', '我已知晓，继续'])
    if enter == '我已知晓，继续':
        pass
    elif enter == '我已知晓，立即退出':
        exit()
    else:
        exit()
elif not dir_if:
    os.mkdir("D:/MineCraftServer")

root.lift()


def runserver(version):
    os.chdir("D:/MineCraftServer/")
    os.system("D:/MineCraftServer/" + version)
    file_modification("D:/MineCraftServer/" + "eula.txt")


def button_1_19_rc1():
    url = 'https://launcher.mojang.com/v1/objects/76ebdba03954e5a2185fb7a1d3a25096eb6bd195/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.19_rc1 Server.jar")
    runserver('1.19_rc1 Server.jar')


def button_1_18_2():
    url = 'https://launcher.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.18.2 Server.jar")
    runserver('1.18.2 Server.jar')


def button_1_18_1():
    url = 'https://launcher.mojang.com/v1/objects/125e5adf40c659fd3bce3e66e67a16bb49ecc1b9/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.18.1 Server.jar")
    runserver('1.18.1 Server.jar')


def button_1_18():
    url = 'https://launcher.mojang.com/v1/objects/3cf24a8694aca6267883b17d934efacc5e44440d/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.18 Server.jar")
    runserver('1.18 Server.jar')


def button_1_17_1():
    url = 'https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.17.1 Server.jar")
    runserver('1.17.1 Server.jar')


def button_1_17():
    url = 'https://launcher.mojang.com/v1/objects/0a269b5f2c5b93b1712d0f5dc43b6182b9ab254e/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.17 Server.jar")
    runserver('1.17 Server.jar')


def button_1_16_5():
    url = 'https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.16.5 Server.jar")
    runserver('1.16.5 Server.jar')


def button_1_16_4():
    url = 'https://launcher.mojang.com/v1/objects/35139deedbd5182953cf1caa23835da59ca3d7cd/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.16.4 Server.jar")
    runserver('1.16.4 Server.jar')


def button_1_16_3():
    url = 'https://launcher.mojang.com/v1/objects/f02f4473dbf152c23d7d484952121db0b36698cb/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.16.3 Server.jar")
    runserver('1.16.3 Server.jar')


def button_1_16_2():
    url = 'https://launcher.mojang.com/v1/objects/c5f6fb23c3876461d46ec380421e42b289789530/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.16.2 Server.jar")
    runserver('1.16.2 Server.jar')


def button_1_16_1():
    url = 'https://launcher.mojang.com/v1/objects/a412fd69db1f81db3f511c1463fd304675244077/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.16.1 Server.jar")
    runserver('1.16.1 Server.jar')


def button_1_16():
    url = 'https://launcher.mojang.com/v1/objects/a0d03225615ba897619220e256a266cb33a44b6b/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.16 Server.jar")
    runserver('1.16 Server.jar')


def button_1_15_2():
    url = 'https://launcher.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.15.2 Server.jar")
    runserver('1.15.2 Server.jar')


def button_1_15_1():
    url = 'https://launcher.mojang.com/v1/objects/4d1826eebac84847c71a77f9349cc22afd0cf0a1/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.15.1 Server.jar")
    runserver('1.15.1 Server.jar')


ofs1_19_rc1 = tk.Button(text="【最新测试版本！】下载1.19_rc1服务端", padx=5, pady=2, command=button_1_19_rc1).pack()
ofs1_18_2 = tk.Button(text="【最新!】下载1.18.2服务端", padx=5, pady=2, command=button_1_18_2).pack()
ofs1_18_1 = tk.Button(text="下载1.18.1服务端", padx=5, pady=2, command=button_1_18_1).pack()
ofs1_18 = tk.Button(text="下载1.18服务端", padx=5, pady=2, command=button_1_18).pack()
ofs1_17_1 = tk.Button(text="下载1.17.1服务端", padx=5, pady=2, command=button_1_17_1).pack()
ofs1_17 = tk.Button(text="下载1.17服务端", padx=5, pady=2, command=button_1_17).pack()
ofs1_16_5 = tk.Button(text="下载1.16.5服务端", padx=5, pady=2, command=button_1_16_5).pack()
ofs1_16_4 = tk.Button(text="下载1.16.4服务端", padx=5, pady=2, command=button_1_16_4).pack()
ofs1_16_3 = tk.Button(text="下载1.16.3服务端", padx=5, pady=2, command=button_1_16_3).pack()
ofs1_16_2 = tk.Button(text="下载1.16.2服务端", padx=5, pady=2, command=button_1_16_2).pack()
ofs1_16_1 = tk.Button(text="下载1.16.1服务端", padx=5, pady=2, command=button_1_16_1).pack()
ofs1_16 = tk.Button(text="下载1.16服务端", padx=5, pady=2, command=button_1_16).pack()
ofs1_15_2 = tk.Button(text="下载1.15.2服务端", padx=5, pady=2, command=button_1_15_2).pack()
ofs1_15_1 = tk.Button(text="下载1.15.1服务端", padx=5, pady=2, command=button_1_15_1).pack()

root.mainloop()
