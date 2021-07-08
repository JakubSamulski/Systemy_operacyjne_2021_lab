from queue import PriorityQueue


class FCFS:
    def __init__(self, processes):
        self.time = 0
        self.ended = []
        self.queue = PriorityQueue()
        for process in processes:
            t = (process.arrivalTime, process.PID, process)
            self.queue.put(t)

    def execute(self):
        while not self.queue.empty():

            current = self.queue.get()[2]  # tuple(arrivaltime,PID,ProcessObj)
            if (self.time - current.arrivalTime) < 0:
                current.waitingTime = 0
            else:
                current.waitingTime = self.time - current.arrivalTime

            if self.time < current.arrivalTime:
                self.time += (current.arrivalTime - self.time)  # przeskok do czasu w którym przyszedł

            self.time += current.phaseLenght
            current.waitingTime = self.time - current.arrivalTime
            self.ended.append(current)

        # podsumowanie
        processCount = 0
        waitingTime = 0
        for process in self.ended:
            processCount += 1
            waitingTime += process.waitingTime
        return float(waitingTime / processCount)

        # TODO usunac to tez

    # zaawansowana funkcja do debugowania
    def prin(self):
        while not self.queue.empty():
            next_item = self.queue.get()
            print(type(next_item[2]))
