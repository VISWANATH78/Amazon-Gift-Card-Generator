import random
import time
def g(choice):
    Data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    result = ""
    while choice >= 1:
        c = random.choice(Data)
        result = result + c
        choice=choice-1
    return result
print("How many codes to be genrated ?")
number = 10
print("")
n = int(number)
n = int(number)
text = input("Type Amazon to get codes -")
t = text.lower()
if text == "Amazon":
    for i in range(n):
        print(g(4)+"-"+g(6)+"-"+g(5))

else:
    print("u have typed wrong type like this Amazon")


time.sleep(2);



