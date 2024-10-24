fp = open('newfile.txt', 'w')
#fp is file handle
#'w' means write file

list = ['red\n', 'green\n', 'blue\n']
#write in file
fp.writelines(list)
fp.write("This is a test file\n")

#close file
fp.close()

#read file
fp = open('newfile.txt', 'r')
view = fp.read()
print(view)
fp.close()

#append in file
fp = open('newfile.txt', 'a')
fp.writelines(list)

#Context Managers
with open('newfile.txt', 'r') as fp: #dont need to close
   #readlines shows as list // ['red\n', 'green\n', 'blue\n', 'This is a test file\n', 'red\n', 'green\n', 'blue\n']
    view = fp.readlines()
    print(view)
