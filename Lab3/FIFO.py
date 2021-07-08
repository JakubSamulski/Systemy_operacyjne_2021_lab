from Page import Page



def run(numberOfPages,numberOfFrames,requests):
    errors=0
    time=0

    pages = []  #tablica ramek
    frames = [-1]*numberOfFrames    #-1 oznacza ze ramka jest pusta tablica int
                                            # req tablica intow
    for i in range(numberOfPages):
        pages.append(Page(i))

    for req in requests:
        done = False
        for i in range(numberOfFrames):
            if(frames[i]== req):    #brak bledu
                done = True
                break

        if not done:
            for i in range(numberOfFrames):
                if(frames[i]==-1):      #wolna ramka
                    frames[i] = req
                    pages[req].arriveTime = time
                    errors += 1
                    done =True
                    break
        #czesc fifo
        if not done:
            max = time -pages[frames[0]].arriveTime
            toDelete = 0
            for i in range(numberOfFrames):
                if(time -pages[frames[i]].arriveTime>max): #szukanie tej strony ktora jest najdluzej w pamieci
                    max = time -pages[frames[i]].arriveTime
                    toDelete = i
            frames[toDelete] = req
            pages[req].arriveTime = time
            errors += 1
        time+=1
    print(errors)
