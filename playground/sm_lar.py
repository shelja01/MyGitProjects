largest = None
smallest = None
while True:
     v=0
     num = input("Enter a number: ")
     if num == "done":
        break
     try:
       v= int(num)

     except:
        print("Invalid Input")
     continue


if num == None:
   largest = num
elif num > largest:
   largest = num
else:
   largest = largest


if num == None:
   smallest = num
elif num > smallest:
   smallest = smallest
else:
   smallest = num

print("Maximum", largest)
print("Minimum", smallest)
