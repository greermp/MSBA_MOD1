import gender_guesser.detector as ggd
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np


d = ggd.Detector(case_sensitive=False)

def guessGender(fName, lName="") :
    if (len(lName) > 1):
        return d.get_gender(fName)
    else   :
        return d.get_gender(fName)


print(guessGender("Tom"))
print(guessGender("Seth"))
print(guessGender("Tom", "Jones"))

df = pd.read_csv("MSBA class.csv", engine='python')  


#x = df.first

print(df.head())

x = np.random.randint(0, 50, 25)
y = x^2
#np.corrcoef(x,y)
#plt.plot(x,y,'o')
#plt.scatter(x,y)
#plt.show()

#m, b = np.polyfit(x, y, 1)
#plt.plot(x, m*x + b)
#plt.show()
numMen = 0
numWomen = 0
notSure=0
#print(df.get('First'))
for name in df.First :
    if (isinstance(name, str)):
        if (guessGender(name) == 'male') :
            numMen += 1
        elif (guessGender(name) == 'female') :
            numWomen+=1
        else :
            notSure +=1
print ("Num men: {}, Num women: {}, Not Sure: {}".format(numMen,numWomen,notSure))
plt.bar(numMen, numWomen, notSure)
plt.show()