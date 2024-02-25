from enum import Enum


class Passenger():
    """ A class that represents a passenger

        Attributes:
        firstName - The first name of the passenger as shown on their passport.
        lastName - The last name of the passenger as shown on their passport.
        passportID - The passport ID as shown on their passport.

        """
    def __init__(self, firstName, lastName, passportID):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__passportID = passportID

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getPassportID(self):
        return self.__passportID

    def displayPassenger(self):
        """ This method, when called, displays all of the relevant information of a passenger """
        print("Passenger Information:")
        print(f"Name: {self.getFirstName()} {self.getLastName()}")
        print(f"Passport Number: {self.getPassportID()}")
        print("")


class Flight():
    """ A class that represents a flight

    Attributes:
    flightNum - The number that is assigned to a National Airlines flight.
    dateofDep - The scheduled date of the departing flight
    depOrigin - The airport where the flight will originate from.
    depTime - The scheduled time of the flight's departure (shown as integer e.g. 1130 or 1745)
    depGate - The gate that was assigned to the flight.
    flightDest - The planned destiantion of the flight.
    arrTime - The scheduled arrival time of the flight.
    arrTerminal - The terminal that the flight will arrive at.


    """
    def __init__(self, flightNum, dateofDep, depOrigin, depTime, depGate, flightDest, arrTime, arrTerminal):
        self.__flightNum = flightNum
        self.__dateOfDep = dateofDep
        self.__depOrigin = depOrigin
        self.__depTime = depTime
        self.__depGate = depGate
        self.__flightDest = flightDest
        self.__arrTime = arrTime
        self.__arrTerminal = arrTerminal

    def getFlightNum(self):
        return self.__flightNum

    def getDateOfDep(self):
        return self.__dateOfDep

    def getDepOrigin(self):
        return self.__depOrigin

    def getDepTime(self):
        return self.__depTime

    def getDepGate(self):
        return self.__depGate

    def getFlightDest(self):
        return self.__flightDest

    def getArrTime(self):
        return self.__arrTime

    def getArrTerminal(self):
        return self.__arrTerminal

    def displayFlight(self):
        """ This method, when called, displays all of the relevant information of an existing flight """
        print("Flight Information:")
        print(f"Flight Number: NA{self.getFlightNum()}")
        print(f"Date of Departure: {self.getDateOfDep()}")
        print(f"Departure Origin: {self.getDepOrigin()}")
        print(f"Departure Time: {self.getDepTime()}")
        print(f"Boarding Until: {self.getDepTime() - 20}")
        print(f"Departure Gate: {self.getDepGate()}")
        print(f"Flight Destination: {self.getFlightDest()}")
        print(f"Arrival Time: {self.getArrTime()}")
        print(f"Arrival Terminal: {self.getArrTerminal()}")
        print("")


class CabinClass(Enum):
    """ This enum class represents the values that a Cabin class attribute can have"""
    Economy = "Economy Class"
    Business = "Business Class"
    First = "First Class"


class PassengerReservation(Passenger, Flight):
    """ A class that represents a passenger reservation

        Attributes:
            reservationID - the value that was assigned to a reservation.
            seatRow - The row of a seat that was assigned to a passenger (as an integer e.g. 12345).
            seatPos - The position of the that was assigned to a passenger (as a string e.g. ABCDEF).
            cabinClass - The cabin that has been assigned to a passenger once a reservation is made. It is only limited
            to the values found in CabinClass class above.

            This class inherits some attributes from Passenger and Flight class. These attributes are: firstName, lastName, and
            flightNum. These attributes are inherited to be used when a passenger reservation is displayed.

        """
    def __init__(self, firstName, lastName, flightNum, reservationID, seatRow, seatPos, cabinClass):
        Passenger.__init__(self, firstName, lastName, None)
        Flight.__init__(self, flightNum, None, None, None, None, None, None, None)
        self.__reservationID = reservationID
        self.__seatRow = seatRow
        self.__seatPos = seatPos
        self.__cabinClass = cabinClass


    def setReservationID(self, reservationID):
        self.__reservationID = reservationID
    def getReservationID(self):
        return self.__reservationID

    def setSeatRow(self, seatRow):
        self.__seatRow = seatRow
    def getSeatRow(self):
        return self.__seatRow

    def setSeatPos(self, seatPos):
        self.__seatPos = seatPos
    def getSeatPos(self):
        return self.__seatPos

    def setCabinClass(self, cabinClass):
        self.__cabinClass = cabinClass
    def getCabinClass(self):
        return self.__cabinClass

    def displayReservation(self):
        """ This method, when called, displays all of the relevant information of the reservation """
        print(f"Reservation ID: {self.getReservationID()}")
        print(f"Name: {self.getFirstName()} {self.getLastName()}")
        print(f"Flight Number: NA{self.getFlightNum()}")
        print(f"Seat: {self.getSeatRow()}{self.getSeatPos()}")
        print(f"Cabin Class: {self.getCabinClass()}")
        print("")


class BoardingPass():
    """ A class that represents a boarding pass

    Attributes:
        electicketNum - the value that was assigned to a boarding pass.
        isIssused - determines if the boarding pass has been issued.

        This class will also inherit all attributes in Passenger, Flight, and Reservation classes to be able to create
        a boarding pass with all of the neccessary attributes.

    """
    def __init__(self, passenger, flight, reservation, electicketNum, isIssued):
        self.__passenger = passenger
        self.__flight = flight
        self.__reservation = reservation
        self.__electicketNum = electicketNum
        self.__isIssued = isIssued


    def setElecticketNum(self, electicketNum):
        self.__electicketNum = electicketNum

    def getElecticketNum(self):
        return self.__electicketNum


    def issueBoardingPass(self):
        """ This method, when called, will issue the passenger's boarding pass with all of the attributes from an existing
        passenger, flight, and reservation object. This method also depends on the status of the isIssued attribute where
        a boarding pass can be only issued if it hasn't been issued already. If the value was False, it indicates that
        it has not been issued yet so it can be issued. Once it has been issued, the value changes to True. This means
        that it cant be reissued. It can only be reissued if the boarding pass has been changed in the ChangeBoardingPass
        method. Once a boarding pass is issued, the program will print a digital boarding pass that can be used.
        """
        if self.__isIssued == False:
            print("Your boarding pass has been issued.")
            print("-------------------------------------")
            print("|            Boarding Pass          |")
            print(f"|           {self.__reservation.getCabinClass()}           |")
            print("|                                   |")
            print(f"| Passenger: {self.__passenger.getFirstName()} {self.__passenger.getLastName()}            |")
            print(f"| Flight Number: NA{self.__flight.getFlightNum()}             |")
            print(f"| Date: {self.__flight.getDateOfDep()}                   |")
            print(f"| Seat: {self.__reservation.getSeatRow()}{self.__reservation.getSeatPos()}                          |")
            print(f"| From: {self.__flight.getDepOrigin()}   Time: {self.__flight.getDepTime()}   |")
            print(f"| Gate: {self.__flight.getDepGate()}  Boarding Till: {self.__flight.getDepTime() - 20}      |")
            print(f"| To: {self.__flight.getFlightDest()}   Time: {self.__flight.getArrTime()}      |")
            print(f"| Arrival Terminal: {self.__flight.getArrTerminal()}               |")
            print("|                                   |")
            print(f"|               {self.__electicketNum}                 |")
            print("-------------------------------------")
            print("")
            print("PLEASE DONT SHARE THIS BOARDING PASS. \n")
            self.__isIssued = True

        else:
            print("The boarding pass has already been issued.")
            print("")

    def ChangeBoardingPass(self):
        """ This method, when called, will initiate the change boarding pass process where the
            user will choose their new seat. This can only occur when a boarding pass has been
            issued already. The method will use a new attribute called isChanged, which will
            show if a boarding pass has been changed. On default, it will be set to False but
            it will become True once this method is called.

            This method will ask the passenger to input their new seat position and row. The
            user is asked if they have upgraded their cabin class, if yes, it will ask for the
            new cabin class. All new inputted values will replace the old ones and the isIssued
            attribute will be set to False so that it can be reissued for use.
        """
        pass

    def VerifyBoardingPass(self):
        """ This method, when called, will attempt to verify the information of the passenger in the boarding pass with
        the person. This is done by checking if the name and the passport ID in the boarding pass object matches with the
        information shown on the person object. If the information matches, the boarding pass is verified, which will return
        true. Otherwise, it will return false.

        """
        pass


# Test Case
passenger1 = Passenger("James", "Smith", "AF324T4A3")
flight1 = Flight(4321, "6/12/2020", "NEW YORK JFK", 1140, 3, "CHICAGO ORD", 1330, 2)
reservation1 = PassengerReservation("James", "Smith", 4321, 54241, 9, "A", "Economy Class")
boardingpass1 = BoardingPass(passenger1, flight1, reservation1, 629, False)


#Display information of passenger 1
passenger1.displayPassenger()

#Displays information of flight 1
flight1.displayFlight()

#Displays information of reservation 1
reservation1.displayReservation()

#Issues a boarding pass using a boarding pass object
boardingpass1.issueBoardingPass()

#Checks if it can be reissued after the above.
boardingpass1.issueBoardingPass()