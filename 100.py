

class ATM(object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber
    
    def checkBalance(self):
        print("balance is 50000")

    def withDrawel(self,amount):
        newAmount=50000-amount
        print("New balance: ",newAmount)

def main():
    cardnumber=input("ENTER THE CARD NUMBER: ")
    pinnumber=input("ENTER THE PINNUMBER: ")
    user=ATM(cardnumber,pinnumber)
    print("CHOOSE YOUR ACTIVITY")
    print("1.BALANCECHECK 2.WITHDRAWELCASH")
    activity=int(input("ENTER THE ACTIVITY NUMBER: "))
    if(activity==1):
        user.checkBalance()
    elif(activity==2):
        amount=int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAWEL: "))
        user.withDrawel(amount)
    else:
        print("enter a vailed number")

main()
