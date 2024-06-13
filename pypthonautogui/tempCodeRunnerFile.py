import pyautogui as pa
import time as t
# t.sleep(2)
# pa.scrioll(100)
# print(pa.position())
# print(pa.size())
#(pa.click(53,146))
# #will click on given position
# pa.click(1531,956)
# pa.typewrite("hi i am writing from python automation")
# text = [i for i in ("hi i am writing from python automation").split(' ')]
# print(text)
# pa.typewrite(text)

# for i in range(1,5):

#     pa.moveTo(100*i,234,duration=2)
# hihi
# pa.alert("alok")
# pa.confirm("should i proceed")
def sendcont(n):
    while(n):
        n-=1
        for i in "hi rahul":
            pa.click(1531,956)
            if(i!=" "):
                pa.typewrite(i)
                pa.click(1876,967)
# sendcont(5)
pa.hotkey("ctrlleft", "a")