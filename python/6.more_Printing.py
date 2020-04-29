# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:25:21 2020

@author: Sansrit Paudel

    EXTRA KNOWLEDGE ON PRINTING
    
"""

print("Ram had little goat.")
print("Its fur was white as %s." %'snow')

print("And everywhere that Ram went.")

#PRINTS THE DOT 10 TIMES

print("."*10)           

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"

end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"


print(end1+end2+end3+end4+end5+end6,end7+end8+end9+end10+end11+end12)



formatter = "%r %r %r %r"

print(formatter%(1,2,3,4))


print(formatter%("one", "two", "three", "four"))

print(formatter%(formatter,formatter,formatter,formatter))

print(formatter%(True,False,True,False))

print(formatter%(
        "Nepal",
        "China",
        "USA",
        "France"
    ))


days = "Mon Tue Wed Thu Fri Sat Sun"

#THE \n backshlsh n represents start string on next line

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print ("Here are the days: ", days)

print ("Here are the months: ", months)




