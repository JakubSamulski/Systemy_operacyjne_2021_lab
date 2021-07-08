from Page import Page
import random

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
                    errors += 1
                    done =True
                    break
        if not  done:
            todelete = random.randrange(numberOfFrames)
            frames[todelete] = req
            errors += 1
        time+=1

    print(errors)
