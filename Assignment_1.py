'''import sys
print(sys.version)

#printing id 
a=23
b=23
print(id(a))
print(id(b)) 

#printing keywords list
import keyword
print(keyword.kwlist)

#date and time of today
from datetime import datetime
dt = datetime.today()
print(dt)

# Changing the format of date and time

from datetime import datetime
dl=dt.strftime("%d-%m-%Y and   %I : %M %p") # for full year "Y" annd for only 24 "y"  and I for 12 hr format and H for 24 hr format we use p as pm and am
print(dl) 


#year formatting
from datetime import datetime
dt = datetime.today()
from datetime import datetime
dl=dt.strftime("%B %d %Y") # far name of full month
print(dl)
dc=dt.strftime("%b/%d/%Y")# for name of short month
print(dc)

# printing unicode
print(ord("m"))

#printng char from unincpde

print(chr(100))   '''