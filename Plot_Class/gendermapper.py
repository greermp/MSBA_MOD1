import gender_guesser.detector as ggd

d = ggd.Detector(case_sensitive=False)

def guessGender(fName, lName="") :
    if (len(lName) > 1):
        print ("Two names provided")
        return d.get_gender(fName)
    else   :
        return d.get_gender(fName)


print(guessGender("Tom"))
print(guessGender("Seth"))
print(guessGender("Tom", "Jones"))
