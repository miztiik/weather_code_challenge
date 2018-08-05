import itertools
import os
f = open("sample.txt", "r")
user=[]
ip=[]

for line in f:
    words = line.split()
    a=words[0]
    b=words[-1]
    user.append(a)
    ip.append(b)

for (m, n) in zip(user, ip):
	os.system('python3 script.py'+" --user "+m+" --host "+n+" --port 22 PushKey") 
