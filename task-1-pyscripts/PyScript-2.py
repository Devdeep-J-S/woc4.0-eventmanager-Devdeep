import re
# using re library to regular expressions to find integers in a file and output total of ut 

#reading file using hadle 
fhand = open ("pyscript-2-data.txt")
Sum=0
for lines in fhand:
    line = lines.rstrip()
    #using regular expression to find integers in file 
    temp_list = re.findall('[0-9]+',line)
    for i in temp_list:
      Sum +=int(i)
print(Sum)    
