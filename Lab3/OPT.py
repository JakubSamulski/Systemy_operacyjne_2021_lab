from Page import Page


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
                done = True
                break

        if not done:
            for i in range(numberOfFrames):
                if (frames[i] == -1):  # wolna ramka
                    frames[i] = req
                    pages[req].arriveTime = time
                    errors += 1
                    done = True
                    break
        if not done:
            max = 0
            todel = -1
            for i in range(numberOfFrames):
                for j in range(time, len(requests)):
                    if (frames[i] == requests[j]):
                        if max < j - time:
                            max = j - time
                            todel = i
                        break
            frames[todel] = req
            pages[req].arriveTime = time
            errors += 1
        time+=1
    print(errors)