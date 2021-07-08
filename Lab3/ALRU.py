from Page import Page
from queue import Queue



def run(numberOfPages,numberOfFrames,requests):
    errors = 0
    time = 0

    pages = []  # tablica ramek
    frames = [-1] * numberOfFrames  # -1 oznacza ze ramka jest pusta tablica int
    queue = Queue()

    # req tablica intow
    for i in range(numberOfPages):
        pages.append(Page(i))

    for req in requests:
        done = False
        for i in range(numberOfFrames):
            if (frames[i] == req):  # brak bledu
                done = True
                pages[req].bit = 1
                break

        if not done:
            for i in range(numberOfFrames):
                if (frames[i] == -1):  # wolna ramka
                    frames[i] = req
                    pages[req].bit=1
                    queue.put(pages[req])
                    errors += 1
                    done = True
                    break
        if not done:
            #gdy pierwsza ma bit=0
            first=queue.get()
            if first.bit==0:
                for i in range(numberOfFrames):
                    if(frames[i]==first.id):
                        frames[i]=req
                        pages[req].bit=1
                        queue.put(pages[req])
                        break
            else:

                while(True):
                    todelete = first
                    if(todelete.bit==0):
                        break
                    else:
                        todelete.bit =0
                        queue.put(todelete)
                        first = queue.get()
                for i in range(numberOfFrames):
                    if (frames[i] == todelete.id):
                        frames[i] = req
                        pages[req].bit = 1
                        queue.put(pages[req])
                        break
            errors+=1
        time+=1

    print(errors)