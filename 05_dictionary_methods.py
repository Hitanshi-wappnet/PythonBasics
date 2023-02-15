myDict={
    "fast":"In a quick manner",
    "hitanshi":"A Coder",
    "marks":[1,2,5],
    "anotherdict":{'Shivam':'player'},
    1:2
}
#Dictionary methods
print(myDict.keys())#print the key value of dictionary
print(type(myDict.keys()))
print(list(myDict.keys())) #we can convert keys in to list
print(myDict.values())#print the values of dictionary
print(myDict.items()) #print the (key,value)  for all content in dictionary
print(myDict)
updateDict={
    "Shreya":"friend",
    "Prish":"Brother",
    "hitanshi":"Singer and coder"
}
myDict.update(updateDict)#we can update the content in dictionary by adding key value pairs from updateDict
print(myDict)

print(myDict.get("hitanshi")) #print the value associated with key
print(myDict["hitanshi"]) #print the value associated with key

#-------------------------------Interview Question----------------------------------------------
#difference betwwen the .get and [] syntax in the dictionary
print(myDict.get("hitanshi2")) #returns none when we use get method
print(myDict["hitanshi2"])#throws an error if the key is not present in the dictionary
