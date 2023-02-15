story = "I do this python course with the help of tutorial--15 hours vedio and learn python"

#string Functions
""" print(len(story))
print(story.endswith("python"))
print(story.count("a"))
print(story.count("python"))
print(story.capitalize())  #make the first letter capital  """
print(story.find("tutorial"))
print(story.replace("I","Hitanshi"))

letter='''Dear <|NAME|>,
You are selected in amazon!
Date:<|DATE|>'''
name=input("Enter your name\n")
date=input("enter Date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)