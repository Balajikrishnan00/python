"""
row=5
while row>=1:
    col=1
    while col<=row:
        print(1,end='')
        col+=1
    print()
    row-=1
-----------------------
row=5
while row>=1:
    col=1
    while col<=row:
        print(col,end='')
        col+=1
    print()
    row-=1
---------------------------
row=5
while row>=1:
    col=1
    while col<=row:
        print(row,end='')
        col+=1
    print()
    row-=1
-----------------------------"""
row =5
while row>=1:
    col=1
    while col<=row:
        print(row+col,end='')
        col+=1
    print()
    row-=1
