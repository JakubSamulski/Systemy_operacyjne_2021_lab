class Page:
    def __init__(self, nr, refCount, process_number):
        self.id = nr
        self.processID = process_number
        self.lastUsed = refCount

    def __str__(self): # do debugowania
        return "[Nr:" + str(self.id) + " | proces: " + str(self.processID) + " | ref: " + str(self.lastUsed) + " ]"