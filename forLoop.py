# For Loop Every Letter in Given string
"""
name='user1'

for n in name:
    print(n)
-----------------
for x in range(10+1):
    print(x,end=' ')
-----------------
for x in range(100,120+1):
    print(x,end=' ')
    # op 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120
---------------------------------------
for x in range(5,100+1,5):
    print(x,end=' ')

# 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
---------------------------------------
for x in range(30,0-1,-1):
    print(x,end=' ')
# 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
--------------------------------------
name='mom'
for n in range(len(name)):
    print(n,end=' ')
#  0 1 2
----------------------------------
for no in range(51,20,-1):
    print(no,end=' ')
# 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21
---------------------------------
name='bala'
for n in name:
    print(n,end='')
else:
    print('ji')

# balaji
-----------------------------------
for x in range(10,1):
    print(x)
# no output
----------------------------------
for x in range(10,1,-1):
    print(x,end=' ')
# 10 9 8 7 6 5 4 3 2
----------------------------------
for x in [1,2,3,4,5,6]:
    print(x,end=' ')
# 1 2 3 4 5 6
----------------------------------
# sum of 10 numbers
total=0
for n in range(10+1):
    total+=n
print(total)
-------------------------------
# sum of N numbers
n=int(input('Enter range :'))
total=0
for l in range(n+1):
    total+=l
print(total)

------------------------------
# fact
n=int(input('Enter n Factorial Number:'))
total=1
for x in range(1,n+1):
    total*=x
print(total)
-----------------------------
# prime Number
sentance='i am a very bad boy '.strip()
word=0
for x in sentance:
    if x==' ':
        word+=1
word+=1
print(word,end=' ')
----------------------------"""
# Prime Number
n= int(input('Enter a Number:'))
for x in range(2,n):
    if n%x==0:
        print('Not Prime')
        break

else:
    print(n,'Prime')










