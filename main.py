#Importation of my module
import Calculator as Cal
#Importation of time module for sleep
import time

print("Here are things can do in my module named Calculator")

list=["1. add","2. subtact","3. multiply","4. divide","5. modulus ","6. square_root","7. square","8. average","9. roundoff","10.get random number"]


print("For stopping , type '0'")

while True: 
  time.sleep(3)
  for lists in list:
   print (lists)
  op=int(input("Enter a number"))
  if op==0:
    break
  elif op==1:
    a=int(input("Enter a number"))
    
    b=int(input("Enter the second number"))
    Cal.add(a,b)
  elif op==2:
    a=int(input("Enter a number"))
    
    b=int(input("Enter the second number"))
    Cal.subtract(a,b)
  elif op==3:
    a=int(input("Enter a number"))
    
    b=int(input("Enter the second number"))
    Cal.multiply(a,b)
  elif op==4:
   a=int(input("Enter a number"))
    
   b=int(input("Enter the second number"))
   Cal.divide(a,b)
  elif op==5:
    a=int(input("Enter a number"))
    
    b=int(input("Enter the second number"))
    Cal.modulus(a,b)
#Rest I will finish tomorrow
  elif op==6:
    c=int(input ("Enter the number"))
    print(Cal.squareroot(c))
  elif op==7:
    d=int(input ("Enter the num"))
    print(Cal.square(d))
  elif op==8:
    e=int(input("Enter first number"))
    f=int(input ("Enter second number"))
    print(Cal.average(e,f))
  elif op==9:
    h=int(input ("Enter the number"))
    print (Cal.round_of(h))
  elif op==10:
    i=int(input("Enter the number"))
    print(Cal.get_random_num(i))
  else:
    print("wrong number")
    
