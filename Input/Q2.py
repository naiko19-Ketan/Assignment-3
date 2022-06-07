print("The program exits when an incorrect expression is entered or user enters quit")
while True :
    i=input("Enter the expression :")
    if i.lower() == 'quit' or i=='':
        break
    print("Output is:", eval(i))
