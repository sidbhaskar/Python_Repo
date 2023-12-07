#WAP using classes and bjects for online flight booking application

class Flight:
    def __init__(self, flight_number, origin, destination, seats_available):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.seats_available = seats_available

    def book_seat(self):
        if self.seats_available > 0:
            self.seats_available -= 1
            print(f"Seat booked! {self.seats_available} seats remaining.")
        else:
            print("Sorry, this flight is fully booked.")

class BookingSystem:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight):
        self.flights[flight.flight_number] = flight

    def book_seat(self, flight_number):
        if flight_number in self.flights:
            self.flights[flight_number].book_seat()
        else:
            print("Flight not found.")

# Create a flight
flight1 = Flight("AA123", "New York", "Los Angeles", 5)

# Create a booking system and add the flight
booking_system = BookingSystem()
booking_system.add_flight(flight1)

# Book a seat on the flight
booking_system.book_seat("AA123")
