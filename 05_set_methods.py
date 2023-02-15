#creating an empty set
a=set()

#adding the values to an empty set
a.add(4) 
a.add(5)
a.add(5) #Adding a value repeaatedly does not change a set
#a.add([4,5,6])  #can not add list or dictionary
#a.add({4:5})
print(a)

print(len(a)) #prints the length of a set

#Removal of an Item
a.remove(5) #removes 5 from the set a
#a.remove(15) #throws an error while trying to remove 15(Which is not present in th set)
print(a)
a.add(8)
a.add(9)
print(a)

print(a.pop())