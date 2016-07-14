super_heroes = {"Iron Man" : "Tony Start", "Superman" : "Clark Kent", "Captain America" : "Steeve Rogers", "Batman" : "Bruce Wayne"}

print super_heroes

print super_heroes['Captain America']

del super_heroes["Batman"]
super_heroes["Iron Man"] = "Tony Stank"

print "len %s max %s min %s" % (len(super_heroes),max(super_heroes),min(super_heroes))

print super_heroes.get('Superman')

print super_heroes.keys()

print super_heroes.values()

print super_heroes