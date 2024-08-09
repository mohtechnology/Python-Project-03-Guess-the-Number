import random

x = random.randint(1,100)
y = ""
attempt = 0
print("Welcome to The Guessing the Number")
print()
try:
  while x != y:
    y = int(input("Enter Your Number Between 1 to 100 : "))
    attempt += 1
    print()
    if x == y:
      print("Congrats, you won")
      print()
      print(f"Number is    : {x}")
      print(f"Attempts are : {attempt}")
    elif x > y:
      print("Too, small")
    elif x < y:
      print("Too, big")
    print()
except:
  print()
  print('INVALID NUMBER FOUND TRY AGAIN')

finally:
  print("Thank You")
