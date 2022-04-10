# -*- coding: UTF-8 -*-

from tkinter.messagebox import *
import tkinter as tk
import os
import wget

root = tk.Tk()
root.title("fictional spoon main program")

dir_if = os.path.exists('D:/MineCraftServer')
if dir_if == True:
    tk.messagebox.showwarning('Warning!','The installation location "D:/MineCraftServer" is already occupied, please rename or delete this folder so that fictional spoon will install it for you!')
    exit()
elif dir_if == False:
    pass

os.mkdir("D:/MineCraftServer")

def button_1_18_2():
    url = 'https://launcher.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.18.2 Server.jar")
def button_1_18_1():
    url = 'https://launcher.mojang.com/v1/objects/125e5adf40c659fd3bce3e66e67a16bb49ecc1b9/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.18.1 Server.jar")
def button_1_18():
    url = 'https://launcher.mojang.com/v1/objects/3cf24a8694aca6267883b17d934efacc5e44440d/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.18 Server.jar")
def button_1_17_1():
    url = 'https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.17.1 Server.jar")
def button_1_17():
    url = 'https://launcher.mojang.com/v1/objects/0a269b5f2c5b93b1712d0f5dc43b6182b9ab254e/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.17 Server.jar")
def button_1_16_5():
    url = 'https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.16.5 Server.jar")
def button_1_16_4():
    url = 'https://launcher.mojang.com/v1/objects/35139deedbd5182953cf1caa23835da59ca3d7cd/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.16.4 Server.jar")
def button_1_16_3():
    url = 'https://launcher.mojang.com/v1/objects/f02f4473dbf152c23d7d484952121db0b36698cb/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.16.3 Server.jar")
def button_1_16_2():
    url = 'https://launcher.mojang.com/v1/objects/c5f6fb23c3876461d46ec380421e42b289789530/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.16.2 Server.jar")
def button_1_16_1():
    url = 'https://launcher.mojang.com/v1/objects/a412fd69db1f81db3f511c1463fd304675244077/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.16.1 Server.jar")
def button_1_16():
    url = 'https://launcher.mojang.com/v1/objects/a0d03225615ba897619220e256a266cb33a44b6b/server.jar'
    wget.download(url, out="D:/MineCraftServer/1.16 Server.jar")

download_1_18_2 = tk.Button(text="[up to date!] Download 1.18.2 server",padx=5, pady=2, command=button_1_18_2).grid()
download_1_18_1 = tk.Button(text="Download 1.18.1 server", padx=5, pady=2, command=button_1_18_1).grid()
downlaod_1_18 = tk.Button(text="Download 1.18 server", padx=5, pady=2, command=button_1_18).grid()
download_1_17_1 = tk.Button(text="Download 1.17.1 server", padx=5, pady=2, command=button_1_17_1).grid()
download_1_17 = tk.Button(text="Download 1.17 server", padx=5, pady=2, command=button_1_17).grid()
download_1_16_5 = tk.Button(text="Download 1.16.5 server", padx=5, pady=2, command=button_1_16_5).grid()
download_1_16_4 = tk.Button(text="Download 1.16.4 server", padx=5, pady=2, command=button_1_16_4).grid()
download_1_16_3 = tk.Button(text="Download 1.16.3 server", padx=5, pady=2, command=button_1_16_3).grid()
download_1_16_2 = tk.Button(text="Download 1.16.2 server", padx=5, pady=2, command=button_1_16_2).grid()
download_1_16_1 = tk.Button(text="Download 1.16.1 server", padx=5, pady=2, command=button_1_16_1).grid()
download_1_16 = tk.Button(text="Download 1.16 server", padx=5, pady=2, command=button_1_16).grid()

root.mainloop()
