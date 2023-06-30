import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
abc = int(time.strftime('%H'))
abc2 = int(time.strftime('%M'))
abc3 = int(time.strftime('%S'))

if(abc>=0 & abc <24 ):
    if(abc2>=0 & abc2<60):
        if(abc3>0 & abc3<60):
            print("Good Morning !")
# print(abc)
