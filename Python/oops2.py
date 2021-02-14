from oops1 import Fligt
import random

class Booking:

    def __init__(self):
        self.flight = Fligt(5)

    def seatReservation(self, name):
        if self.flight.book(name):
            print(f"Seat has been successfully reserved for the passenger {name} and the seat number is : {self.flight.seatNumber(name)}")
        else:
            print(f"No seats available for the passenger : {name}")



passengerList = ["Kalidas", "Anoop", "Annie", "Ancil", "Sonia", "Alex", "Jhon"]

random.shuffle(passengerList)

print(f"Flignt booking started for the passengers : {passengerList}")

booking = Booking()

for p in passengerList:
    booking.seatReservation(p)



print(f"Ticket reservation completed")