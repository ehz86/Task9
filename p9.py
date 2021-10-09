def Check(a):
    if  (a>9999) and (a<100000):
        if(a // 10000 == a % 10)and((a // 1000) % 10 == (a % 100) // 10):
            print("Yes")
        else:
            print("No") 
    else:
        print ("Invalid data")
flag = True
while flag:
    try:
        a = int(input ("Введите 5 значное число: "))
    except Exception:
        print ("Invalid data")
    else:
        flag = False
Check(a)
