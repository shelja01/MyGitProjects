largest = None
smallest = None
while True:
     #v = 0
     num = input("Enter a number: ")
     if num == "done":
        break
     try:
       num = int(num)
      # print(v)
       if largest is None or num > largest:
          largest = num
       elif smallest is None or num < smallest:
          smallest = num

     except ValueError :
        print("Invalid input")

     continue

print("Maximum is", largest)

print("Minimum is", smallest)
