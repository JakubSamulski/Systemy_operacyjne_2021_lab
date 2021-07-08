import random
import copy
from Page import Page
from Proces import Proces




class Algorithms:
    def __init__(self, framesCount, requestCount, maxID, Processes_count,ppfPercentage,zoneCoef,localProb,localCount,localSubset):
        self.framesCount = framesCount
        self.requestCount = requestCount
        self.processesCount = Processes_count
        self.maxID = maxID
        self.processes = []  # length == Processes
        self.Pages = []
        self.requests = []
        self.frames = []
        self.errors = 0
        self.ppfPercentage = ppfPercentage
        self.zoneCoef = zoneCoef
        self.localProbability = localProb
        self.localCount = localCount
        self.localSubset = localSubset
        self.generate()


    def generate(self):  # TODO dodac lokalnosci
        # generowanie ciagu
        for i in range(self.requestCount):
            #lokalnosc
            if(random.random()<self.localProbability):
                process = random.randint(0, self.processesCount)
                subsetCount = random.randint(1,self.localSubset)
                subset = []
                for i in range(subsetCount):
                    subset.append(random.randint(0,self.maxID))
                localCount = random.randint(0,self.localCount)
                for i in range(localCount):
                    toAdd = random.choice(subset)
                    if(i== self.requestCount):
                        return
                    self.requests.append(Page(toAdd,0,process))
                    i+=1

            process = random.randint(0, self.processesCount)
            id = random.randint(0, self.maxID)
            self.requests.append(Page(id, 0, process))
        # generowanie procesow
        for i in range(self.processesCount):
            self.processes.append(Proces([], 0))
            for req in self.requests:
                if req.processID == i:
                    a = self.processes[i]
                    a.requests.append(req)

    def equal(self):
        # bez tego referencje sie mieszaja\
        errors = 0
        processesCopy = copy.deepcopy(self.processes)

        framesCount = self.framesCount // len(self.processes)

        for i in range(len(self.processes)):
            p = self.LRUList(processesCopy[i].requests, framesCount)
            errors += p
            
        return errors

    def proportional(self):
        ProcessesCopy = copy.deepcopy(self.processes)
        errors = 0

        for i in range(len(ProcessesCopy)):
            frame_size = len(ProcessesCopy[i].requests) * self.framesCount // self.requestCount

            # zeby jednak proces mial jakies bo inaczej zacznie sypac duzo bledow


            e = self.LRUList(ProcessesCopy[i].requests, frame_size)
            errors += e
        return errors

    def steering_fault_frequency(self):
        # prog % bledow
        errorMax = int(self.ppfPercentage) * self.requestCount

        framesCount = self.framesCount / len(self.processes)

        processesCopy = copy.deepcopy(self.processes)


        for i in processesCopy:
            i.framesCount = framesCount

        freeFrames = 0
        processesCount = self.processesCount
        allErrors = 0

        while processesCount != 0:
            minimum = self.maxID
            maximum = 0
            bestProcessIndex = 0
            worstProcessIndex = 0


            for i in range(len(processesCopy)):
                current = processesCopy[i]
                if current is not None and len(current.requests) != 0:
                    if processesCount == 1:
                        processesCopy[i].framesCount = processesCopy[i].framesCount + freeFrames
                        freeFrames = 0

                    errorsCoef = current.errorsCoef

                    e = current.LRU(current.requests)
                    # update  najlepszego i najgorszego procesu
                    if errorsCoef > maximum:
                        maximum = errorsCoef
                        worstProcessIndex = i

                    if errorsCoef < minimum:
                        minimum = errorsCoef
                        bestProcessIndex = i

                    current.requests.pop(0)
                    allErrors += e

                elif current is not None:
                    # jesli koniec to przekazuje ramki najgorszemu
                    if processesCopy[worstProcessIndex] is not None and worstProcessIndex != i:
                        processesCopy[worstProcessIndex].framesCount += processesCopy[i].framesCount
                    else:
                        # jesli nie ma najgorszego to do puli
                        freeFrames += processesCopy[i].framesCount
                    #koniec
                    processesCopy[i] = None
                    processesCount -= 1

           # gdy przekroczony prog
            if (processesCopy[bestProcessIndex] is not None and processesCopy[worstProcessIndex] is not None and processesCopy[
                bestProcessIndex].processFrame != 1 and maximum > errorMax):

                if processesCopy[bestProcessIndex].framesCount > 3:
                    # zabranie i przydzielenie ramki
                    processesCopy[bestProcessIndex].framesCount -= 1
                    processesCopy[worstProcessIndex].framesCount += (1 + freeFrames)
                    freeFrames = 0

        return allErrors

    def set(self, a, zone):
        h = set()
        if zone > len(a):
            zone = len(a)
        for i in range(zone):
            h.add(a[-i].id)
        return len(h)




    #TODO Nie do konca wiem czy to jest dobra implementacja ale wydaje sie ze dziala
    def zone(self):

        allErrors = 0
        freeFrames = self.framesCount
        finished = -1

        ProcessesTabCopy = copy.deepcopy(self.processes)
        #przydzial proporcjonalny na poczatku
        for i in range(len(ProcessesTabCopy)):
            workingSet = len(ProcessesTabCopy[i].requests) * self.framesCount // self.requestCount
            ProcessesTabCopy[i].framesCount = workingSet

        if finished != self.processesCount - 1:
            for k in range(finished + 1, len(self.processes)):
                # jesli sa wolne
                if freeFrames > ProcessesTabCopy[k].framesCount:
                    finished += 1
                    w = ProcessesTabCopy[k].framesCount
                    freeFrames -= w
                    if ProcessesTabCopy[k].framesCount != 0:
                        h = int(self.LRUList(ProcessesTabCopy[k].requests, ProcessesTabCopy[k].framesCount))
                        allErrors += h
            freeFrames = self.framesCount

        while (finished != self.processesCount - 1):
            for i in ProcessesTabCopy:
                workingSet = self.set(i.requests, self.zoneCoef)# update zbioru roboczego
                i.framesCount = workingSet
            for k in range(finished + 1, len(self.processes)):
                #wolne ramki
                if freeFrames > ProcessesTabCopy[k].framesCount:
                    finished += 1
                    w = ProcessesTabCopy[k].framesCount
                    # odejmowanie zajetych ramek
                    freeFrames -= w
                    # jesli brakuje ramek to nie idziemy dalej czyli usypiamy na iteracje
                    if(freeFrames<0):
                        freeFrames+=w   #dodajemy ramki uspionego
                        continue
                    if ProcessesTabCopy[k].framesCount != 0:
                        h = int(self.LRUList(ProcessesTabCopy[k].requests, ProcessesTabCopy[k].framesCount))
                        allErrors += h
            freeFrames = self.framesCount

        return allErrors

    def LRUList(self, PagesRef, frame_size):
        eroors = 0
        req2 = copy.deepcopy(PagesRef)

        if len(req2) == 0:
            return 0

        for i in req2:
            if_breaker = False
            if len(self.frames) < frame_size:
                for frame in self.frames:
                    if frame.id == i.id:
                        frame.lastUsed += frame.lastUsed + 1
                        if_breaker = True
                if not if_breaker:
                    eroors += 1
                    self.frames.append(i)
            else:
                for frame in self.frames:
                    if frame.id == i.id:
                        frame.lastUsed += frame.lastUsed + 1
                        if_breaker = True
                if not if_breaker:
                    self.frames.sort(key=lambda f: f.lastUsed, reverse=False)

                    del self.frames[0]
                    if(i.lastUsed!=0):
                        print(i)
                    self.frames.append(i)
                    eroors += 1

        self.frames = []
        return eroors