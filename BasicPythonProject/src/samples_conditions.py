age = 63

if age > 16 :
    print("You can drive a car")
else :
    print("You should not drive")
    
if age >= 21 :
    print("You can drive a truck")
elif age >= 16 :
    print("You can drive a car")
else :
    print("You should not drive")
    
    
# ando or not

if ((age >= 1) and (age<=18)) :
    print "You have a bDay party"
elif ((age == 21 ) or (age >=65)) :
    print "You have a bDay party too"
elif not(age == 30) :
    print "You DON't have a bDay party"
else :
    print "HAPPY BIRTHDAY!"