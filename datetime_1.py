import datetime

x=datetime.datetime.now()  #Display Current date and time
print(x)
print(x.year)  #Display year
print(x.month)   #Display Month
print(x.strftime("%A"))  #Display Day of the week
print(x.strftime("%a"))  #Display Shorter Version of Week
print(x.strftime("%B"))  #Display Month in words 
print(x.strftime("%b"))  #Display Shorter Version of Month
print(x.strftime("%C"))  #Display Century of year
print(x.strftime("%c"))  #Display Local version of date and time
print(x.strftime("%D"))  #Display Date in MM-DD-YY Method
print(x.strftime("%d"))  #Display date only
print(x.strftime("%e"))   #Display date only
print(x.strftime("%F"))   #Display yyyy-mm-dd format
print(x.strftime("%f")) 
print(x.strftime("%G"))  #Display year
print(x.strftime("%g"))  #Display year in yy format
print(x.strftime("%H"))  #Display Hour 
print(x.strftime("%h"))  #Shorter version of month
print(x.strftime("%I"))  #hour in 0-12 range 
print(x.strftime("%j"))  
print(x.strftime("%M"))  #Display Minute
print(x.strftime("%m"))  #Display month in number format
print(x.strftime("%n"))  #Display Space
print(x.strftime("%p"))   #Display PM
print(x.strftime("%R"))  #HH-MM Format
print(x.strftime("%r"))   #HH:MM:SS Format
print(x.strftime("%S"))  #Display Second
print(x.strftime("%T"))   #HH:MM:SS Format
print(x.strftime("%t"))  #Space of One Line
print(x.strftime("%U"))   #Week number of year, Sunday as the first day of week, 00-53	
print(x.strftime("%u"))   #ISO 8601 weekday (1-7)
print(x.strftime("%W"))   #Week number of year, Sunday as the first day of week, 00-53	
print(x.strftime("%w"))   #ISO 8601 weekday (1-7)
print(x.strftime("%X"))   #HH:MM:SS Format
print(x.strftime("%x"))    #MM/DD/YY Format
print(x.strftime("%Y"))    #Display Year
print(x.strftime("%y"))    #Display yy format
print(x.strftime("%Z"))    #Display Space
print(x.strftime("%z"))     #Display Space