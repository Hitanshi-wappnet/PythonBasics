# Create a list using []
a=[1,2,3,4,5]

#print the list using print() statement
print(a)

#change the value of list using
a[0]=98

#Access using index using a a[0],a[1],a[2]
print(a[0])
print(a[2])

#we can crate a list with items of different items
c=[45,"Hitanshi",False,25.23]
print(c)

m1=int(input("Enter Student number1 : "))
m2=int(input("Enter Student number2 : "))
m3=int(input("Enter Student number3 : "))
m4=int(input("Enter Student number4 : "))
m5=int(input("Enter Student number5 : "))
m6=int(input("Enter Student number6 : "))

mylist=[m1,m2,m3,m4,m5,m6]
mylist.sort()
print(mylist)