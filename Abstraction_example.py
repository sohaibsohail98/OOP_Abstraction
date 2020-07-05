from abc import ABC, abstractmethod
class Payment(ABC):
    def reciept(self, amount):
        print('Purchase of amount- ', amount)
    # This is an abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(Payment): #This is a child class using the abstract method
    def payment(self, amount):
        print('Credit card payment of- ', amount)

class NFCPhonePayment(Payment): #This is the second child class using the abstract method
    def payment(self, amount):
        print('Mobile wallet payment of- ', amount)

obj = DebitCardPayment()
obj.payment(100)
obj.reciept(100)
print(isinstance(obj, Payment))
obj = NFCPhonePayment()
obj.payment(200)
obj.reciept(200)
print(isinstance(obj, Payment))