name = "Italo"
number = 1

print(number+1)

print "What is your name?"
name = sys.stdin.readline()
print "Hello ",name

#Numbers Strings Lists Tuples Dictionaries

# + - * / % ** // 
#order of operation matters
print("5 + 2 =",5 + 2)
print("5 - 2 =",5 - 2)
print("5 * 2 =",5 * 2)
print("5 / 2 =",5 / 2)
print("5 % 2 =",5 % 2)
print("5 ** 2 =",5 ** 2)
print("5 // 2 =",2 // 5)

quote = "\"purpose that drivers\""

multi_line_string =  ''' This is a multi line 
yeah, multi line string

seriously it is multi line
'''

print quote + multi_line_string
print ("%s %s  %s" % (quote, "this 'is' a sring", multi_line_string))
print ("Testing the send")
count = 0
print ('new line \n' * 5)