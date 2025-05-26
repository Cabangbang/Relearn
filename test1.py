name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 18:
  print(name + ", is a minor.")
else:
  print(name + ", is an adult.")

#check if age is odd or even
if age % 2 == 0:
  print(name + ", your age is even.")
elif age % 2 != 0:
  print(name + ", your age is odd.")
else:
  print(  "Invalid age")
  
