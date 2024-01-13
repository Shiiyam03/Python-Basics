#List[]
a=[1,2,3,4,5,6,7]

print(type(a))

print(a)

a.append(7)
a.append(11)
print(a)

a.append(True)
a.append("Shiiyam")
print(a)

print(a[10])

a.insert(9,"is-to")
print(a)

a.insert(7,8)
print(a)

a[0]="Data Science"
print(a)

a.pop()
print(a)
a.pop()
print(a)

a.pop(0)
print(a)

#List extend[]
a=[1,2,3,4,5,6,7]
b=[8,9,10]
a.extend(b)
print(a)
print(b)




#Tuple()
a=(1,2,3,4,1)
b=list(a)

print(a)
print(b)




#Set{}
a={1,2,3,4,1}
print(a)

a.add(10)
print(a)

a.add(3)
print(a)

a.remove(10)
print(a)

a.pop()
print(a)

a.pop(2)
print(a)




#Dictionary{}
a={
    "name":"Shiyam R",
    "age":19,
    "location":"coimbatore",
    "hobbies":["music","netflix","sleep"]
    }
print(a)
print(a.keys())
print(a.values())

a["name"]="R Shiyam"
print(a)
a.update({"age":20})

a["color"]="grey"
print(a)

a.pop("age")
print(a)
del a["color"]
print(a)

a.clear()
print(a)

























