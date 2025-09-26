num=input("enter your number:")

if len(num) >= 4:
    mid= len (num)//2
    midOne=int(num[mid])
    midTwo=int(num[mid-1])
    product=midOne*midTwo
    print (product)
else:
    ("its not more than equal or 4  digits")