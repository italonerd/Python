#You can't change a tuple after its creation
#To change a tuple one must change to a list then again to a new tuple

pi_tuple = (2,5,0,6,1,99,0)

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

print pi_tuple
print "len %s max %s min %s" % (len(pi_tuple),max(pi_tuple),min(pi_tuple))