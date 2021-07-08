from Generator import generate
import Rand
import OPT
import LRU
import ALRU
import FIFO
numberOfPages=30
numberOfFrames=29
requests = generate(numberOfPages,10000,3,0.2,10)


FIFO.run(numberOfPages,numberOfFrames,requests)
OPT.run(numberOfPages,numberOfFrames,requests)
LRU.run(numberOfPages,numberOfFrames,requests)
ALRU.run(numberOfPages,numberOfFrames,requests)
Rand.run(numberOfPages,numberOfFrames,requests)