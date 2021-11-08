import datetime


class Cars:

    def __init__(self, phone, car_type, plate):
        self.__phone = phone
        self.__car_type = car_type
        self.__plate = plate

    def __str__(self):
        return f"Plate: {self.__plate}, Phone: {self.__phone}, Car Type: {self.__car_type}."


class ParkingLot:

    def __init__(self, name, capacity=1):
        ''' return a ParkingLot object with name "name" '''

        self.name = name
        self.capacity = capacity
        self.earnings = 0
        self.rate = 15
        self.carsAndEnterTime = {}

    def SetCapacity(self, newCap):
        ''' change the capacity from the default 1 '''
        if newCap < 1:
            raise RuntimeError("Error: parking lot size cannot be less than 1")

        self.capacity = newCap

    def GetCapacity(self):
        ''' return parking lot capacity '''
        return self.capacity

    def GetEarnings(self):
        ''' return how much much parking has made '''
        return self.earnings

    def VehicleEnters(self, vehicle):
        ''' vehicle enters parking lot'''

        # put car and its enter time in a dictionary
        self.carsAndEnterTime[vehicle] = datetime.datetime.now()

        if self.capacity == 0:
            raise RuntimeError("Error: Parking lot full!")

        self.capacity -= 1

    def VehicleLeaves(self, vehicle):
        ''' vehicle leaves parking lot. when it leaves, charges money '''

        secondsDiff = datetime.datetime.now() - self.carsAndEnterTime[vehicle]
        self.earnings += self.rate * secondsDiff.seconds
        # after earned money, delete vehicle from dictionary
        del self.carsAndEnterTime[vehicle]
        self.capacity += 1

    def __str__(self):
        ''' prints basic information of parking lot '''
        return f"Parking lot: {self.name} \nSpots open: {self.capacity} \nHourly rate:{self.rate}\n {self.carsAndEnterTime}\nEarnings: $ {self.earnings} "