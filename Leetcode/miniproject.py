from abc import ABC, abstractmethod

# STEP 1 & 2: Abstract Class
class Vehicle(ABC):
    def __init__(self, number, total_seats):
        self.number = number
        self.total_seats = total_seats

    @abstractmethod
    def calculate_fare(self):
        pass

    def show_details(self):
        print("Bus Number:", self.number)
        print("Total Seats:", self.total_seats)


# STEP 5: LuxuryBus
class LuxuryBus(Vehicle):
    def calculate_fare(self):
        return 500


# STEP 7: OrdinaryBus
class OrdinaryBus(Vehicle):
    def calculate_fare(self):
        return 200


# STEP 9: Seat Manager (Encapsulation)
class SeatManager:
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


# STEP 13: Passenger Class
class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Passenger Name:", self.name)
        print("Age:", self.age)


# STEP 14: Ticket Class
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
        print("--------------------")


# MAIN PROGRAM
print("Select Bus Type")
print("1. Luxury Bus")
print("2. Ordinary Bus")

choice = int(input("Enter choice: "))

if choice == 1:
    bus = LuxuryBus("TN01LB1234", 5)
else:
    bus = OrdinaryBus("TN01OB5678", 5)

seat_manager = SeatManager(bus.total_seats)
tickets = []

while True:
    print("\n1. Available Seats")
    print("2. Book Seat")
    print("3. Cancel Seat")
    print("4. Show Tickets")
    print("5. Exit")

    option = int(input("Enter option: "))

    if option == 1:
        print("Available Seats:", seat_manager.available_seats())

    elif option == 2:
        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))

        seat = seat_manager.book_seat()

        if seat is None:
            print("Bus Full!")
        else:
            passenger = Passenger(name, age)
            fare = bus.calculate_fare()
            ticket = Ticket(passenger, bus, seat, fare)
            tickets.append(ticket)
            ticket.show_ticket()

    elif option == 3:
        seat_no = int(input("Enter seat number to cancel: "))
        seat_manager.cancel_seat(seat_no)

    elif option == 4:
        if not tickets:
            print("No tickets booked yet.")
        else:
            for t in tickets:
                t.show_ticket()

    elif option == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")