# a = int(input("Enter a Number"))

# print("positive") if a>0 else print("Non Positive")

#Match

x=int(input("Enter a Number: "))

match x:
  case 1:
    print("One")
  case 23:
    print("Two")
  case _:
    print("lol")