hours = input("Enter hours: ")
rate = input("Enter rate: ")
h=float(hours)
r=float(rate)
if(h<40):
   x=h*r
else:
   x=40*r+1.5*(h-40)*r
print(x)
