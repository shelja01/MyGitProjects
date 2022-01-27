hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
if h > 40:
   x = h - 40
   gross_pay = 40 * r
   overtime = x * r * 1.5
   total_pay = gross_pay + overtime
else:
   total_pay = h * r
print(total_pay)
