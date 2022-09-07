from random import randrange
from pynput.keyboard import Key, Controller as K
from pynput.mouse import Button, Controller as M
import time

def InitializeMsg():
    f=open("/Users/davidj.desjardins/Desktop/HypeBot.txt", "r")
    global listx
    listx=[]
    for line in f:
        listx.append(line)
    f.close 

def GenerateMsg():
    RandomLine=randrange(214)
    return(listx[RandomLine])

InitializeMsg()
HowMany=int(input("How many messages?"))
M().position = (100,500)
M().click(Button.left, 1)
K().type(GenerateMsg())
time.sleep(randrange(1,3))
K().type('\n')
print(1,"of",HowMany)

for i in range(HowMany):
    K().type('\n')
    time.sleep(34)
    M().position = (100,500)
    M().click(Button.left, 1)
    K().type(GenerateMsg())
    time.sleep(randrange(1,3))
    K().type('\n')
    print(i+2,"of",HowMany)


