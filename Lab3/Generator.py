import  random
def generate(numberOfPages, amount, maxLocalSubsetSize, localProb, MaxLocalAmount):
    requests= []
    counter=0
    while(counter!=amount):
        if(random.random()<localProb):
            subset=[]

            for i in range(random.randrange(maxLocalSubsetSize)):
                subset.append(random.randrange(numberOfPages))
            for i in range(random.randrange(MaxLocalAmount)):
                if(counter>=amount):
                    break
                counter+=1
                toadd=subset[random.randrange(maxLocalSubsetSize)]

                requests.append(toadd)

        else:
            toadd = random.randrange(numberOfPages)
            requests.append(toadd)
            counter+=1

    return requests

generate(5,100,3,0.25,10)