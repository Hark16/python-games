car =[]
for a in range(4):
    a=input("enter any car name")
    car.append(a)

print("you wanna drive ", car)

marry =[]
for b in range(4):
    b=input("enter any name of your choicepartner ")
    marry.append(b)

print("you want to live with ", marry)


money =[]
for c in range(4):
    c=input("enter any amount of Rupees ")
    money.append(c)

print("you wanna get ", money)

home =[]
for d in range(4):
    d=input("enter you wanna live in")
    home.append(d)

print("you want to live in ", home)

e=int(input("gasse any number between 1 to 9 " ))

if e==1:
    print("you will drive ", car[2])
    print("you will marry with ", marry[3])
    print("you will have rupees ", money[1])
    print("you will live in ", home[0])
    

elif e==2:
    print("you will drive ", car[0])
    print("you will marry with ", marry[1])
    print("you will have rupees ", money[2])
    print("you will live in ", home[3])
    

elif e==3:
    print("you will drive ", car[1])
    print("you will marry with ", marry[0])
    print("you will have rupees ", money[3])
    print("you will live in ", home[2])
    

elif e==4:
    print("you will drive ", car[1])
    print("you will marry with ", marry[3])
    print("you will have rupees ", money[1])
    print("you will live in ", home[3])
    

elif e==5:
    print("you will drive ", car[3])
    print("you will marry with ", marry[3])
    print("you will have rupees ", money[1])
    print("you will live in ", home[0])
    

elif e==6:
    print("you will drive ", car[2])
    print("you will marry with ", marry[2])
    print("you will have rupees ", money[2])
    print("you will live in ", home[2])

elif e==7:
    print("you will drive ", car[1])
    print("you will marry with ", marry[1])
    print("you will have rupees ", money[1])
    print("you will live in ", home[1])
    

elif e==8:
    print("you will drive ", car[0])
    print("you will marry with ", marry[0])
    print("you will have rupees ", money[0])
    print("you will live in ", home[0])
    

elif e==9:
    print("you will drive ", car[3])
    print("you will marry with ", marry[3])
    print("you will have rupees ", money[3])
    print("you will live in ", home[3])
    
else :
    pass

z=input("enter for quit")