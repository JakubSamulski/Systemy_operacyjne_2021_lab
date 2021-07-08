from random import gauss

from FCFS import FCFS
from Process import Process
from Rot import Rot
from SJF import SJF


def generate():
    amount = 1000
    median = 50
    std = 15
    p = []

    for i in range(amount):
        pid = i
        at = int(abs(gauss(median+1000, std)))
        ph = int(abs(gauss(median, std)) + 1)
        p.append(Process(pid, at, ph))
    return p





sFCFS=0
sSJF = 0
sRot = 0

testruns=10

for i in range(testruns):
    procesy = generate()
    p1 = procesy.copy()
    p2 = procesy.copy()
    p3 = procesy.copy()

    fcfs = FCFS(p1)
    sFCFS+=fcfs.execute()
    sjf = SJF(p2)
    sSJF+= sjf.exectue()
    rot = Rot(p3, 100)
    sRot+=rot.execute()

sFCFS = sFCFS/testruns
sSJF = sSJF/testruns
sRot = sRot/testruns

print("FCFS "+str(sFCFS),"SJF "+str(sSJF),"Rot "+str(sRot))



