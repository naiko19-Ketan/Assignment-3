import math 
print('a.Value of (3+4)(5):',((3+4)*5))
n=int(input("Enter value of n: "))
print("b.Value of n(n-1)/2:",(n*(n-1))/2)
r=int(input("Enter the value of r: ",))
print("c.Value of 4πr²:",(4*(math.pi)*(r**2)))
r=int(input("Value of r: ",))
a=float(input("Value of Alpha in radians: "))
b=float(input("Value of Beta in radians: "))
print("d. Value of √(r(cos(α))²+r(sin(β))²)",math.sqrt(((r)*(math.cos(math.radians(a)))**2)+((r)*(math.sin(math.radians(b)))**2)))
x1=float(input("Value of x1:"))
x2=float(input("Value of x2:"))
y1=float(input("Value of y1:"))
y2=float(input("Value of y2:"))
print("e.Value of (y2-y1)/(x2-x1):",(y2-y1)/(x2-x1))
