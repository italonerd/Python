
long_string = "    hello my name is Italo Mendes    "

print long_string[0:4]
print long_string[-5:]
print long_string[:-5]
print long_string[:4] + " sub String"
print ("%c is my %s letter and my number %d is %.3f" % ('X',"Favorite",1,.14))
print long_string.capitalize()
print long_string.find("name")
print long_string.isalpha()
print long_string.isalnum()
print len(long_string)
print long_string.replace("name","real name")
print long_string.strip()
quote_list = long_string.split()
print quote_list