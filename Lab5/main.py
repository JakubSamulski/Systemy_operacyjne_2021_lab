from CPU import CPU
from Proces import Process
from Algorithms import *
import random
import copy


def processesGenerator(processesAmount, cpusAmount, maxPhase, maxLoad):
    proc = []
    for i in range(processesAmount):
        cpu = random.randint(0, cpusAmount - 1)
        arriveTime = random.randint(0, processesAmount)
        phaseLenght = random.randint(0, maxPhase)
        load = random.randint(0, maxLoad)
        proc.append(Process(cpu, arriveTime, phaseLenght, load))

    proc.sort(key=lambda p: p.arriveTime)
    return proc


def cpusGenerator(cpusAmount):
    c = []
    for i in range(cpusAmount):
        c.append(CPU())
    return c


p = 70
z = 4
r = 30

PROCESS_AMOUNT = 100000
CPUS_AMOUNT = 50
MAX_PHASE = 200
MAX_LOAD = 80
cpus = cpusGenerator(CPUS_AMOUNT)
processes = processesGenerator(PROCESS_AMOUNT, CPUS_AMOUNT, MAX_PHASE, MAX_LOAD)

p1 = copy.deepcopy(processes)
p2 = copy.deepcopy(processes)
p3 = copy.deepcopy(processes)

cpu1 = copy.deepcopy(cpus)
cpu2 = copy.deepcopy(cpus)
cpu3 = copy.deepcopy(cpus)
alg1(cpu1, p1, p, z)
alg2(cpu2, p2, p)
alg3(cpu3, p3, p, r)
