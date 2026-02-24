# encapsulation
# 1)data hiding
# 2)wrap code and data together into a single unit  

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self._balance=balance #protected variable
#     def deposit(self,amount):
#         self._balance+=amount
#         print("Deposit successful. Current balance:",self._balance)
#     def withdraw(self,amount):
#         if amount<=self._balance:
#             self._balance-=amount
#             print("Withdrawal successful. Current balance:",self._balance)
#         else:
#             print("Insufficient balance.")

#     def show_balance(self):
#         print("Current balance:",self._balance)

# pin=5845
# name=input("enter the name:")
# balance=int(input("enter the balance"))
# pin=int(input("enter the pin:"))

# s=BankAccount(name,balance)
# if pin==5845:
#     while True:
#         print("\n1.deposit 2.withdraw 3.check balance 4.exit")
#         choice=int(input("Enter your choice:"))
#         if choice==1:
#             amount=int(input("Enter the amount to deposit:"))
#             s.deposit(amount)
#         elif choice==2:
#             amount=int(input("Enter the amount to withdraw:"))
#             s.withdraw(amount)
#         elif choice==3:
#             s.show_balance()
#         elif choice==4:
#             print("Thank you for using our service.")
#             break
#         else:
#             print("Invalid choice. Please try again.")
# else:
#     print("enter the valid pin")

# polymorphism
# built in function
# len()


# class animal:
#     def sound(self):
#         print("Animal makes a sound")

# class dog(animal):
#     def sound(self): 
#         print("Dog barks")  

# class cat(animal):
#     def sound(self):
#         print("Cat meows")

# d=dog()
# c=cat()

# d.sound() 
# c.sound() 


# encapsulation
# polymorphism
# inheritance
# abstraction

# from abc import ABC,abstractmethod
# class BankAccount(ABC):
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance #protected variable
#     def deposit(self,amount):
#         self.__balance+=amount
#         print("Deposit successful. Current balance:",self.__balance)


#     @abstractmethod
#     def withdraw(self,amount):
#         pass
        

#     def show_balance(self):
#         print("Current balance:",self.__balance)

# class SavingsAcc(BankAccount):
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#             print("Withdrawal from savings account:",self.__balance)
#         else:
#             print("Insufficient balance.")

# class CurrentAcc(BankAccount):
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#             print("Withdrawal from current account:",self.__balance)
#         else:
#             print("Insufficient balance.")



# name=input("enter the name:")
# balance=int(input("enter the balance"))
# print("1.savings account 2.current account")
# account_type=int(input("enter the account type:"))
# if account_type==1:
#     s=SavingsAcc(name,balance)
# elif account_type==2:
#     s=CurrentAcc(name,balance)


# while True:
#     print("\n1.deposit 2.withdraw 3.check balance 4.exit")
#     choice=int(input("Enter your choice:"))
#     if choice==1:
#         amount=int(input("Enter the amount to deposit:"))
#         s.deposit(amount)
#     elif choice==2:
#         amount=int(input("Enter the amount to withdraw:"))
#         s.withdraw(amount)
#     elif choice==3:
#         s.show_balance()
#     elif choice==4:
#         print("Thank you for using our service.")
#         break
#     else:
#         print("Invalid choice. Please try again.")


# abstraction
# hide details

# abstract class-->cant create the object
# abstract method
# from sklearn.naive_bayes import abstractmethod
# from abc import ABC

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class square(shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         self.side*self.side
        
# class circle(shape):
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         3.14*self.radius*self.radius

# square=square(2)
# circle=circle(3)
# print("area of square:",square.area())
# print("area of circle:",circle.area())


from abc import ABC,abstractmethod

class vehicle(ABC):
    def __init__(self,number,total_seats):
        self.number=number
        self.total_seats=total_seats


    @abstractmethod
    def calculated_fare(self):
        pass

    def show_details(self):
        print("bus number",self.number)
        print("total seats",self.total)

class luxurybus(vehicle):
     def calculate_fare(self):
        return 500
     
class ordinarybus(vehicle):
     def calculate_fare(self):
        return 200
     
class seatmanager:
    def __init__(self, total_seats):
        self.__total_seats = total_seats
        self.__booked = []

    def book_seat(self):
        if len(self.__booked) < self.__total_seats:
            seat_no = len(self.__booked) + 1
            self.__booked.append(seat_no)
            return seat_no
        else:
            return None

    def cancel_seat(self, seat_no):
        if seat_no in self.__booked:
            self.__booked.remove(seat_no)
            print("Seat", seat_no, "cancelled successfully.")
        else:
            print("Invalid seat number!")

    def available_seats(self):
        return self.__total_seats - len(self.__booked)


class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Passenger Name:", self.name)
        print("Age:", self.age)


class Ticket:
    def __init__(self, passenger, bus, seat, fare):
        self.passenger = passenger
        self.bus = bus
        self.seat = seat
        self.fare = fare

    def show_ticket(self):
        print("\n------ TICKET ------")
        self.passenger.show()
        print("Bus Number:", self.bus.number)
        print("Seat Number:", self.seat)
        print("Fare:", self.fare)
print("1. Luxury Bus")
print("2. Ordinary Bus")
choice=int(input("Enter the bus type:"))

if choice==1:
    bus=luxurybus("KA-01-AB-1234",5)
else:
    bus=ordinarybus("KA-01-AB-5678",5)




