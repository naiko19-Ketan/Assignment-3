number=int(input())
temp=number
place_value=0
binary=0
while(temp > 0):
    binary = ((temp%2)*(10**place_value)) + binary
    temp = int(temp/2)
    place_value += 1
print("Binary of {x} is: {y}".format(x=number,y=binary))
