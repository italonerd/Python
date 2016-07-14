s = ""

# FOR LOOPS
for x in range(0,10) :
    s = s + str(x)+ " "
 
print s
s = ""

grocery_lists = ['Juice', 'Tomatoes','Bananas']
for x in grocery_lists :
    s = s + str(x)+ " "
print s
s = ""

for x in [2,4,6,8,10] :
    s = s + str(x)+ " "
print s
s = ""

num_list = [[1,2,3],[4,5,6],[7,8,9]]
for x in num_list :
    print x
    for y in x :
        print y

# WHILE LOOPS

random_number = random.randrange(0,100)

while(random_number != 15):
    print random_number
    random_number = random.randrange(0,100)

i = 0
while(i <= 20):
    if(i % 2 == 0):
        print("Is even ", i)
    elif (i == 9):
        break
    else :
        i+=1
        continue
    
    i+=1

