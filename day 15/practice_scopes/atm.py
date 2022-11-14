balance = 100

def withdraw(amount):
    global balance
    balance = balance - amount
    
def deposit(amount):
    global balance
    balance = balance  + amount
    
withdraw(50)

deposit(40)
    
print(balance)