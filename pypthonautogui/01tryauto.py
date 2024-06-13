import pyautogui as pa
import time as t
# t.sleep(2)
# pa.scroll(100)
print(pa.position())
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
# str pattern(int n):
def sendcont(n):
        for i in range(n):
            # pa.click(1696,967)
            code1 = '38PWRV'
            CODE2 = '4B4'
            r =['3','5','S','6']
            S=['3','9']
            T = ['T','J']
            test = []
            for i in r:
                for j in S:
                    for k in T:
                        test.append(code1+i+j+k+CODE2)
            for li in test:
                pa.click(1722,972)
                pa.typewrite(li)
                pa.click(1863,973)
                t.sleep(.5)
sendcont(1)
# pa.hotkey("ctrlleft", "a","c")