class Process:
    def __init__(self,cpuID,arriveTime,phaseLenght,load):
        self.arriveTime = arriveTime
        self.phaseLenght = phaseLenght
        self.cpuID = cpuID
        self.load = load
