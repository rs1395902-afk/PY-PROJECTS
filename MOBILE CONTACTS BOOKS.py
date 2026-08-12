#MOBILE CONTACTS BOOKS
contacts = {}

name1 = str(input("ENTER FIRST CONTACT NAME :"))
number1 = int(input("ENTER FIRST CONTACT NUMBER :"))
contacts[name1] = number1

name2 = str(input("ENTER SECOND CONTACT NAME :"))
number2 = int(input("ENTER SECOND CONTACT NUMBER"))
contacts[name2] = number2

name3 = str(input("ENTER THIRD CONTACT NAME :"))
number3 = int(input("ENTER THIRD CONTACT NUMBER"))
contacts[name3] = number3

print("NUMBER SAVED")
print(contacts)

search_name = str(input("SEARCH NAME :"))

if search_name in contacts:
    print("PHONE NUMBER :",contacts[search_name])
else:
    print("CONTACT NOT FOUND :")