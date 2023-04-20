import pexpect
import sys
import time
import os
import pyttsx3

"""
mkdir chat
git init
git config core.sparsecheckout true
echo "a.txt" >> .git/info/sparse-checkout
git remote add origin git@github.com:rainy2k/chatroom.git
"""
pre = ""
while True:
    with open('output.log', 'wb') as f:
        # 执行ssh命令，并将输出保存到文件中
        os.system("git pull origin main")
    os.system("echo \"$(cat ./a.txt)\"")
    with open('a.txt', 'r') as file:
        msg = file.read()
        if len(pre)!=0 and pre[0] == msg[0]:
            time.sleep(10)
            pre = msg
            continue
        engine = pyttsx3.init()
        engine.say(msg)
        engine.runAndWait()
        pre = msg
    time.sleep(10)