choice=input("convert to (c)elsius or (f)ahrenheit?").lower()
temp=float(input("enter the temperature value:"))
if choice=='c':
   celsius=(temp-32)*5/9
   print("temperature in celsius:",celsius)
elif choice=='f':
     fahrenheit=(temp*9/5)+32
     print("temperature in farenheit:",fahrenhiet)
else:
    print("invaild")
    
