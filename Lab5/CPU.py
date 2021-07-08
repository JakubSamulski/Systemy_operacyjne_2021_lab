class CPU:
    def __init__(self):
        self.processes = []
        self.ended = []


    def getLoadSum(self):
        loadSum = 0
        for process in self.processes:
            loadSum+= process.load

        return loadSum

    def updatePhaseLenghts(self):
        for process in self.processes:
            process.phaseLenght-=1
           # print("ArriveTime: " + str(process.arriveTime) + " load: " + str(process.load) + " phase: " + str(process.phaseLenght))
            if(process.phaseLenght<=0):
                self.ended.append(process)
                self.processes.remove(process)


