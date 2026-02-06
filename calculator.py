print("Simple calculator")
N1=int(input("Enter a number:"))
N2=int(input("Enter a number:"))
print("1.Find Sum , 2.Find Difference , 3.Find Product , 4.Find quotient")
choice=int(input("Enter the choices(1-4):"))
if choice==1:
  print("The sum of ",N1,"and",N2,"is", N1+N2)
elif choice==2:
  print("The difference of" , N1,"and",N2,"is",abs(N1-N2))
elif choice==3:
  print("The product of",N1,"and",N2,"is", N1*N2)
elif choice==4:
  if N2!=0:
    print("The quotient of" , N1,"and",N2,"is" , N1//N2)
  else:
    print("Error: Division by zero")
else:
  print("Invalid Choice!")
  
  
