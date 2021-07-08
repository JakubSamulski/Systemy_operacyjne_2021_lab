from queue import PriorityQueue


class SJF:

    def __init__(self, add):
        self.toAdd = add
        self.ended = []
        self.queue = PriorityQueue()
        self.time = 0

    def exectue(self):
        while self.toAdd or (not self.queue.empty()):
            self.addToQueue()
            if not self.queue.empty():
                current = self.queue.get()[2]  # tuple(phaselenght,PID,ProcessObj)
                current.waitingTime = self.time - current.arrivalTime
                self.time += current.phaseLenght
                self.ended.append(current)
            else:
                self.time += 1

        processCount = 0
        waitingTime = 0
        avgWaiting = 0
        for process in self.ended:
            processCount += 1
            waitingTime += process.waitingTime
            avgWaiting = float(waitingTime / processCount)
            if process.waitingTime > 4 * avgWaiting:
                print("Proces Zagłodzony " + str(process))

        return avgWaiting

    def addToQueue(self):
        for process in self.toAdd:
            if process.arrivalTime <= self.time:
                t = (process.phaseLenght, process.PID, process)
                self.queue.put(t)
                self.toAdd.remove(process)
