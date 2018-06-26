class Account:

    def __init__(self,filepath):
        self.filepath=filepath
        with open(self.filepath,'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance-=amount

    def deposit(self,amount):
        self.balance+=amount

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write('{}'.format(self.balance))

class Checking(Account):

    acc_type='checking'

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee

    def transfer(self,amount,acc):
        self.balance-=amount+self.fee
        acc.balance+=amount

chk=Checking('balance.txt',1)
chk2=Checking('bal2.txt',1)
chk2.transfer(100,chk)
chk.commit()
chk2.commit()
print(chk.balance,chk2.balance)
