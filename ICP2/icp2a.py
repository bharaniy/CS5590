num=int(input("enter number of studnets:"))
lst=[]
for i in range(num):
    val=int(input("enter weights in lbs"))
    lst.append((val/2.2046))
print(lst)

