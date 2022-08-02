print("Welcome to Pizza Street 99!")
size = input("What size pizza do you want? S, M, or L ")
add_prosciutto = input("Do you want prosciutto crudo? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill=0

if size == 'S':
    bill+= 10
elif size == 'M':
    bill+=15
else:
    bill+=20

if add_prosciutto == 'Y':
    if size == 'S':
     bill += 2
    else:
        bill+=4

if extra_cheese =='Y':
    bill +=1


print(f"Your final bill is: ${bill}.")