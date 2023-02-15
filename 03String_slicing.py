# name="Hitanshi"
# greetings=" Good morning"
# print(type(name))
# #concatenating two strings
# c=name + greetings
# print(c)

name="Hitanshi"
print(name[0])
print(name[2])
#name[3]="d"---> is not possible in python

""" print(name[0:3])#3 is not included
print(name[1:5])
print(name[:5]) # is same as name[0:4]
print(name[0:]) # is same as name[0:7]--end of string index
print(name[-4:-1]) # is same as name[1:4] """

name="HarryIsGood"
d=name[1:7:2]# from [1:7] every one character is skip
e=name[0::2]#every one character skip
f=name[0::3]#every two character skip
print(d)
print(e)
print(f)