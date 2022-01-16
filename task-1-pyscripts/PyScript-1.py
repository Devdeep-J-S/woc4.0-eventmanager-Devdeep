
import matplotlib.pyplot as plt
import numpy as np
#finding frequency of elements in this paragraph
# note : here for example  I have taken this line , we can use file handling to open a file and count frequency of words
paragraph = "the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car."
di = dict()
string=paragraph.rstrip()
words=paragraph.split()
for word in words:
  di[word]=di.get(word,0)+1

  #finding element with maximum frequency    
w=None      
count=-1
for k,v in di.items():
     if v > count:
          w=k
          count=v

print(di)  

print ("Element with highest frequency is  \"" + w + "\" with frequency "+ str(count))


x = di.keys()
y = di.values()

fig, ax = plt.subplots()
ax.plot(x, y,'ro-', label='line 1', linewidth=0)
plt.show()