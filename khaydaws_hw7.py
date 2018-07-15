#####8.20
####
####
####class BankAccount():
####    bank_balance = 0
####
####    def __init__(self, bank_balance):
####        self.bank_balance = bank_balance
####
####    def withdraw(self, amount):
####        if self.bank_balance >= amount:
####            self.bank_balance = self.bank_balance - amount
####
####    def deposit(self, amount):
####        self.bank_balance += amount
####
####    def balance(self):
####        return self.bank_balance
##
##
##8.40
##
##class BankAccount2():
##    
##    def __init__(self, bank_balance2):
##        self.bank_balance2 = bank_balance2
##
##        if self.bank_balance2 < 0:
##           print("Illegal Balance")
##        else:
##           self.bank_balance2 = 0
##       
##    
##
##    def withdraw (self, amount):
##        if self.bank_balance2 - amount < 0:
##            print("Overdraft")
##        else:
##            self.bank_balance2 = self.bank_balance2 - amount
##            
##
##    def deposit(self, amount):
##        if amount < 0:
##            print("Negative Deposit")
##        else:
##            self.bank_balance2 += amount
##
##    def balance(self):
##
##        return self.bank_balance2
##            
##    
##        
##            
#####8.22
####
####class Worker():
####    name = ""
####    pay_rate = 0
####
####    def __init__(self, name, pay_rate):
####        self.name = name
####        self.pay_rate = pay_rate
####
####    def changeRate(self, new_pay_rate):
####        self.pay_rate = new_pay_rate
####
####    def pay(self, hours):
####        print("Not Implemented")
####
####class HourlyWorker(Worker):
####    name = ""
####    pay_rate = 0
####    def __init__(self, name, pay_rate):
####        self.name = name
####        self.pay_rate = pay_rate
####
####    def pay(self, hours):
####        if hours >= 40:
####            hours = hours * 2
####        print(self.pay_rate * hours )
####
####class SalariedWorker(Worker):
####    name = ""
####    pay_rate = 0
####
####    def __init__(self, name, pay_rate):
####        self.name = name
####        self.pay_rate = pay_rate
####
####    def pay(self,hours = 40):
####        print(self.pay_rate * 40)
##
###8.35
##
####class Stack(object):
####    stack = []
####
####    def __init__(self):
####        self.stack = []        
####
####    def push(self, item):
####        self.stack.append(item)
####
####    def pop(self):
####        return (self.stack.pop())
####
####    def isEmpty(self):
####        if (len(self.stack)) == 0:
####            return True
####        else:
####            return False
####    def __len__(self):
####        return len(self.stack)
####        
####    def __repr__(self):
####        return str(self.stack)
##        
##
##
##
##
##        
