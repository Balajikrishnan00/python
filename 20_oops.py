"""
import sys
class customer:
    ''' This class is about bank'''
    bank='Indian Overseas Bank'
    def __init__(self,name,acno,blance=500):
        self.name=name
        self.acno=acno
        self.blance=blance
        print('welcome Mr.',self.name,'How can help you')

    def deposit(self,amt):
        self.blance+=amt

    def withdraw(self,amt):
        if self.blance>=500 and self.blance-amt>=500 :
            self.blance -= amt
        else:
            print('sorry you have only minimum balance only')

print('Welcome to',customer.bank)
name=input('whats is your name:')
acno=int(input('Ac number:'))
c1=customer(name,acno,500)
c1.deposit(500)
print(c1.blance)
c1.withdraw(200)
print(c1.blance)
c1.withdraw(300)
print(c1.blance)
c1.withdraw(100)
#print(c1.blance)
----------------------------------
import sys
class bank:
    bankName='Indian Overseas Bank'
    '''this class is about bank'''
    def __init__(self,name,accno,blance=500):
        self.name=name
        self.accno=accno
        self.blance=blance
        print('Welcome to ',bank.bankName,'Mr.',self.name)


    def deposit(self,amount):
        self.blance+=amount
    def blanceEnquiry(self):
        print('Your amount:',self.blance)
    def widthraw(self,amount):
        if self.blance>=500 and self.blance-amount>=500:
            self.blance-=amount
        else:
            print('sorry minimum balance must be maintain is 500.00')
    def exit(self):
        sys.exit()


name=input('acHolder Name:')
accno=int(input('ac Number:'))
c=bank(name, accno)

while True:

    choice =input('D-Deposit\nB-Balance Enquiry\nW-Widthraw\nS-Exit\n')

    if choice=='D' or choice=='d':
        #c=bank(name, accno)
        amt=float(input('Enter your amount:'))
        c.deposit(amt)

    elif choice=='B' or choice=='b':
        c.blanceEnquiry()

    elif choice=='W' or choice=='w':
        amt=float(input('Enter Widthraw amount:'))
        c.widthraw(amt)


    elif choice=='S' or choice=='s':
        sys.exit()
---------------------------------------
# inheritance
# 1. HAS A relationship
# 2. IS A relationship

class Engine:
    '''This class is about Engine'''
    mileage=22

    def __init__(self):
        self.petrol=True
        self.Engine_Running=False
    def EngineStart(self):
        if self.Engine_Running:

            print('Engine Already Running')
        else:
            self.Engine_Running=True
            print('Engine Started...')

    def EngineStop(self):
        if self.Engine_Running:
            self.Engine_Running=False
            print('Engine Stopped..!')
        else:
            print('Engine Already Stopped..!')
class Car:
    '''This class is about Car'''
    def __init__(self):
        self.engine=Engine()
    def drive(self):
        self.engine.EngineStart()
        print('Car in Running')

    def park(self):
        self.engine.EngineStop()
        print('Car stoped')
c1=Car()
c1.drive()
c1.park()
#t1=Engine()
#t1.EngineStart()
#t1.EngineStart()
#t1.EngineStop()
#t1.EngineStop()
------------------------------
# 2 is a relationship

class humanbeing:
    '''this class about is humanbeing'''
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def reading(self):
        print('reading books')
class empolyee(humanbeing):
    '''this class is about employee'''
    def __init__(self,empno,salary,name,age,sex):
        super().__init__(name,age,sex)
        self.empno=empno
        self.salary=salary
    def dowork(self):
        print('Emp working')
emp1=empolyee(101,20000,'balaji',24,'male')

print(emp1.age)
emp1.reading()
emp1.dowork()
-----------------------------------------------
class bank:
    bankname='SBI'
    def __init__(self):
        self.min=2000
    def deposit(self):
        print('Deposit')
    def withdraw(self):
        print('widthraw')
    @staticmethod
    def staticmethod():
        print('staticmethod is running')
    @classmethod
    def classmethod(cls):
        print('classmethod is running',cls.bankname)

user1=bank()
user1.classmethod()
user1.staticmethod()
user1.deposit()
user1.withdraw()
print(user1.min)
----------------------------------
class Signup:
    '''This class is about  Signup your account'''
    def __init__(self,name,accno):
        self.name=name
        self.accno=accno
        self.account=True
class Rbi(Signup):
    '''This class is about Bank'''
    def __init__(self,acname,acno):
        super(Rbi,self).__init__(acname,acno)
    def deposit(self):
        if self.account:
            print('cash Deposited')
        else:
            print('Please Login')
    def withdraw(self):
        if self.account:
            print('cash withdraw success full.')
        else:
            print('Login')
class indianBank(Rbi):
    @staticmethod
    def staticmethod():
        print('staticmethod is running')

#user1=indianBank('balaji',12234)
#user1.deposit()
#user1.withdraw()
#print(user1.account)
#user1.staticmethod()
user2 =indianBank()
user2.deposit()
---------------------------------------"""
