# Shopping Bill Generator


print("SHOPPING BILL GENETOR")

a = str(input("ENTER 1ST PRODUCT NAME: "))
b = int(input("ENTER VALUE: "))

c = str(input("ENTER 2ND PRODUCT NAME: "))
d = int(input("ENTER VALUE: "))

e = str(input("ENTER 3RD PRODUCT NAME: "))
f = int(input("ENTER VALUE: "))

g = str(input("ENTER 4TH PRODUCT NAME: "))
h = int(input("ENTER VALUE: "))

total_bill = b + d + f + h

print("----BILL-----")


print(a,":",b)
print(c,":",d)
print(e,":",f)
print(g,":",h)
print("---------------")
print("TOTAL BILL =",total_bill)
