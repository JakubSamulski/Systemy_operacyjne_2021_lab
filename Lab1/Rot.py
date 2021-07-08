class Rot:

    def __init__(self, added, quant):
        self.queue =  added
        self.ended = []
        self.quant = quant
        self.time = 0

    def execute(self):
        while self.queue:
            for proces in self.queue:
                if proces.arrivalTime <= self.time:
                    self.time += 5
                    self.queue.remove(proces)
                    self.queue.append(proces)
                    quantOfTime = self.quant

                    if proces.getRemaningTime() > quantOfTime:
                        proces.setRemaningTime(proces.getRemaningTime() - quantOfTime)
                        self.time += quantOfTime

                    elif proces.getRemaningTime() <= quantOfTime:
                        self.time += proces.getRemaningTime()
                        proces.setRemaningTime(0)
                        proces.waitingTime = self.time - proces.arrivalTime - proces.phaseLenght
                        self.ended.append(proces)
                        self.queue.remove(proces)
            self.time += 1

        processCount = 0
        waitingtime = 0
        for process in self.ended:
            processCount += 1
            waitingtime += process.waitingTime
        return float(waitingtime / processCount)
