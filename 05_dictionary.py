myDict={
    "fast":"In a quick manner",
    "hitanshi":"A Coder",
    "marks":[1,2,5],
    "anotherdict":{'Shivam':'player'}
}
print(myDict)
print(myDict["fast"])
myDict["marks"]=[45,78] #posiible to change the element of dictinory
print(myDict['marks'])
print(myDict["anotherdict"]["Shivam"])

myhindi={
    "Pankha":"Fan",
    "Dabba":"Box",
    "Vastu":"Item"
}
print("Options are: ",myhindi.keys())
a=input("Enter the Hindi word\n")
#---print("The meaning of your word is: ",myhindi[a])
#----To avoid error we use .get() method
print("The meaning of your word is: ",myhindi.get(a))
