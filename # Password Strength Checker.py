# Password Strength Checker

print("-----PASSWORD STRENGHT CHECKER-----")

a = str(input("ENTER YOUR PASSWORDF :"))
b  = len(a)

if (b>=8):
    print("STRONG PASSWORD")
else:
    print("WEAK")
