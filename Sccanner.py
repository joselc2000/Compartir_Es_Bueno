import os
import subprocess
import time
import webbrowser
#import requests
import winreg
git_dir= r"C:\Users\CC6\Desktop\practica_git"
repos = [name for name in os.listdir(git_dir)
         if os.path.isdir(os.path.join(git_dir,name))and
         os.path.exists(os.path.join(git_dir,name, ".git"))]