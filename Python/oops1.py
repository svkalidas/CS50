class Fligt:

    def __init__(self, capacity):
        self.capacity = capacity
        self.pasangers = []

    def book(self, name):
        if self.isSeatsAvailable():
            self.pasangers.append(name)
            self.capacity = self.capacity - 1
            return True
        return False


    def isSeatsAvailable(self):
        return self.capacity > 0

    def seatNumber(self, name):
        return self.pasangers.index(name)