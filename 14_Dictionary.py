# Dictionary
# key ,value Pair
# no duplicate key allowed
# value duplicate allowed
"""
timeTable={'Tamil':'10:00am','English':'12:00am','Maths':'10:00am'}
d={}
print(type(d))
for key in timeTable.keys():
    print(key)
    for value in timeTable.values():
        print(value)
d[1]='siva'
d[2]='shankar'
print(d)
print(d[1])
d[100]='balaji'
print(d)
# print(d[123]) Key Error
print(d.keys())
print(d.values())
del d[100]
print(d)
d.clear()
print(d)
del d
print(d)
------------------------------------"""
