f = open("abc.txt",'r')
#print(f.read(6))
print(f.tell())
#f.seek(0,1)
#f.seek(0)
print(f.read(6))



f = open("abc.txt",'rb')
f.seek(-10,2)
print(f.read(6))

# copy file
with open('file.txt','r') as firstfile, open('second.txt','a') as secondfile:

    # read content from first file
    for line in firstfile:
        # append content to second file
        secondfile.write(line)


import os

#reverse file
filename = input("Enter name of file with extension : ")
if filename not in os.listdir():
    # File with given name does not exist in current directory
    print("Oops! seems like file does not exist.")
else:
    file = open(filename,"r")
    #str = file.readlines()
    str = reversed(file.readlines())
for i in str:
    #print(i[::-1])
    print(i.rstrip()[::-1])
file.close()


#read and append in list
fl = []
f = open("file.txt")
for line in f :
    line=line.rstrip("\n")
    fl.append(line)
print(fl)

