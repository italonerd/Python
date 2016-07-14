test_file = open("test.txt","wb")

print(test_file.mode)
print(test_file.name)

test_file.write( "Write e to the file")
test_file.close()
test_file = open("test.txt","r+")
text_in_file = test_file.read()
print text_in_file
test_file.close()
os.remove("test.txt")