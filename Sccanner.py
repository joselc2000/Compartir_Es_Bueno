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

if repos:
    print("Found the following Github repository in C:\Users\CC6\Desktop\practica_git")
    for idx, repo in enumerate(repos, 1):
        print(f"{idx}. {repo}")
else:
    print("No Github repositories foun in C:\Users\CC6\Desktop\practica_git")
    print("Please provide a GitHUb repositry") 