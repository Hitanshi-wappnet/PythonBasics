# creates a tuple using ()
t=(1,2,4,5)
#t1=() #empty tuple
#t1=(1) #wrong way to declare a tuple with single element
t1=(1,) #tuple with single element
print(t1)

#printing the elements of tuple
print(t[0])

#can not update the values of tuple --->This is main dofference between list and tuple in python
#t[0]=34 #throws an error
print(t)
