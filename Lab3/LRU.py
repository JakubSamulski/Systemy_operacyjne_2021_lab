from Page import Page
from Generator import generate
r = generate(5,100,3,0.25,10)

def run(numberOfPages,numberOfFrames,requests):
    errors = 0
    time = 0

    pages = []  # tablica ramek
    frames = [-1] * numberOfFrames  # -1 oznacza ze ramka jest pusta tablica int
    # req tablica intow
    for i in range(numberOfPages):
        pages.append(Page(i))

    for req in requests:
        done = False
        for i in range(numberOfFrames):
            if (frames[i] == req):  # brak bledu
                pages[req].lastUsed = time
                done = True
                break

        if not done:
            for i in range(numberOfFrames):
                if (frames[i] == -1):  # wolna ramka
                    frames[i] = req
                    pages[req].arriveTime = time
                    pages[req].lastUsed = time
                    errors += 1
                    done = True
                    break
        if not done:
            max = 0
            toDel=-1
            for i in range(numberOfFrames):
                if(time-pages[frames[i]].lastUsed>max):
                    toDel = i
                    max = time-pages[frames[i]].lastUsed
            frames[toDel] = req
            pages[req].arriveTime = time
            pages[req].lastUsed = time
            errors += 1
        time+=1
    print(errors)
