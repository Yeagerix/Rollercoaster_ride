print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age? "))
  if age >= 45 and (age <= 55):
    bill = 0
    print("You go on for free Old Bugger!")
  elif age >= 18:
    bill = 18
    print("Please pay full price: $18 ")
  elif age <= 12:
    bill = 12 
    print("Please pay: $12 Please") 
  else:
    bill = 7
    print("Please pay: $7 Please")

  wants_photo = input("Do you want your photo taken Y or N ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your bill is ${bill}")

else:
  print(f"Sorry mate you can't ride the rollercoaster, you're less than 120 cm") 

#odd_even = (height % 2)


#if odd_even == 0:
 # print("It's Even")
#else:
 # print("It's odd")

