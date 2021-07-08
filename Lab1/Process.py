class Process:
    remaningTime = 0

    def __init__(self, PID, arrivalTime, phaseLenght):
        self.PID = PID
        self.arrivalTime = arrivalTime
        self.phaseLenght = phaseLenght
        self.setRemaningTime(phaseLenght)
        self.waitingTime = 0


    def __repr__(self):
        return "PID: " + str(self.PID) + " Moment zgloszenia: " + str(self.arrivalTime) + \
               " Dlugosc pracy: " + str(self.phaseLenght) + " Czas pozostały: " + \
               str(self.remaningTime) + " Czas oczekiwania: " + str(self.waitingTime)

    def setRemaningTime(self, remaningTime):
        self.remaningTime = remaningTime

    def getRemaningTime(self):
        return self.remaningTime
