mol=input("Molecular formula of compound :")
c=int(input("Enter the number of Carbon atoms :"))
h=int(input("Enter the number of Hydrogen atoms :"))
o=int(input("Enter the number of Oxygen atoms :"))
print("Weight of 1 Hydrogen atom is 1.00794")
print("Weight of 1 Oxygen atom is 15.9994")
print("Weight of 1 Carbon atom is 12.0107")
w_h=(1.00794)*h
w_o=15.9994*o
w_c=12.0107*c
net_weight=(w_h)+(w_o)+(w_c)
print("The molecular weight of {} is: {} + {} + {}= {} ".format(mol,w_h,w_o,w_c,net_weight))
