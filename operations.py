def factors (numbers):
    factor=[]
    for i in range(1,number+1):
        if number%i==0:
            factor.append(i)
    print("Factor of ",number ," are : ",factor)

def multiples(number):
    multiple=[]
    for i in range(1,11):
        multiple.append(number*i)
    print("Multiples of ",number,"are : ",multiple)

def lcm(x,y):
    if x>y:
        num=x
    else:
        num=y
    while(1):
        if((num%x==0) and (num%y==0)):
            lcm=num
            break
        num=num+1;
    print("LCM of (",x,",",y,") is :",lcm)
    return lcm

def hcf(x, y):
    if x < y:
        num = x
    else:
        num = y
    for i in range(1,num+1):
        if ((x%i == 0) and (y%i== 0)):
            hcf= i
            break
    print("HCF of (", x,",", y,") is :", hcf)
    return hcf


loop=True
print("Enter following choice code for respective operations: \n1) For finding factors \n 2) For finding multiple \n 3) For finding lcm \n 4) For finding hcf. \n 5) To exit")

while(loop):
    choice = int(input("Enter choice : "))
    if(choice==1):
        number=int(input("Enter number whose factors are to be found: "))
        factors(number)
    elif(choice==2):
        number = int(input("Enter number whose multiples are to be found: "))
        multiples(number)
    elif(choice==3):
        x=int(input("Enter 1st number : "))
        y=int(input("Enter 2nd number : "))
        lcm(x,y)
    elif (choice == 4):
        x = int(input("Enter 1st number : "))
        y = int(input("Enter 2nd number : "))
        hcf(x, y)
    elif(choice==5):
        loop=False