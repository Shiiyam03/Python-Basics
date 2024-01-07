f=open("text.txt","a")
f.write("\nvimal\n")
f.write("Shiyam\n")
f.close()

f=open("text.txt","r+")
print(f.read())
print(f.readline())
