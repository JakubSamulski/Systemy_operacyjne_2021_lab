from Page import Page


class Proces:

    def __init__(self, proces, PFrame):
        self.processFrame = PFrame #INTEGER
        self.requests = proces #ArrayList
        self.errorsCoef = 0
        self.framesCount = 0
        self.errors = 0
        self.frames = []



    def LRU(self, PageReferences):
        errors = 0
        req2 = PageReferences.copy()
        temp = req2[0]
        Done = False

        if len(self.frames) < self.framesCount:  #gdy sa wolne ramki
            for frame in self.frames:
                if frame.id == temp.id: #strona w ramce -> brak bledu
                    frame.lastUsed += 1
                    Done = True
                    break
            if not Done:        #brak strony w ramkach -> wrzucenie do wolnej
                errors += 1
                self.frames.append(temp)
        else:   # brak wolnych ramek
            for frame in self.frames:   #strona w ramce -> brak bledu
                if frame.id == temp.id:
                    frame.lastUsed += 1
                    # p.setRef(p.ref + 1)
                    Done = True
                    break

            if not Done: # podmiana strony
                self.frames.sort(key=lambda x: x.lastUsed, reverse=False)
                self.frames.pop(0)
                self.frames.append(temp)
                errors += 1
        self.errorsCoef = self.errorsCoef + errors
        return errors