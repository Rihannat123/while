lower=int("Enter your lower case")
upper=int("Enter your upper case")

print("prime number between :", lower , "and" ,upper)

for i in range(lower,upper+1):
   if num>1:
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num)