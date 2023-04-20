import pexpect
import sys
import time
import os
import pyttsx3

username = "SA22011105"
password = "Zxy314159"
pre = ""

while True:
    with open('output.log', 'wb') as f:
        # 执行ssh命令，并将输出保存到文件中
        ssh_command = f'scp {source_file} .'
        ssh_process = pexpect.spawn(ssh_command, logfile=sys.stdout.buffer)
        ssh_process.expect('(Student ID)')
        ssh_process.sendline(username)
        ssh_process.expect('Vlab password:')
        ssh_process.sendline(password)
        ssh_process.expect(pexpect.EOF)
        ssh_process.close()

    os.system("echo \"$(cat ./b.txt)\"")
    with open('b.txt', 'r') as file:
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