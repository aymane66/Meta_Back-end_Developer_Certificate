# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):

    ### YOUR CODE HERE
    def basicinfo():
        print("This is a generic bank")
        return str("Generic bank: 0")

    @abstractmethod
    def withdraw():
        pass
 
# Class Swiss
class Swiss(Bank):

    ### YOUR CODE HERE
    def __init__ (self):
        self.bal = 1000

    def basicinfo(self):
        print("This is the Swiss Bank")
        return (f"Swiss Bank: {self.bal}")

    def withdraw(self, amount):
        self.amount = amount
        
        if self.amount > self.bal:
            print("Insufficient funds! ")
            return self.bal

        else:
            self.bal -= self.amount
            print(f"Withdrawn amount: {self.amount}")
            print(f"New Balance: {self.bal}")
            return self.bal
  
# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    #s.withdraw(1000)

if __name__ == "__main__":
    main()