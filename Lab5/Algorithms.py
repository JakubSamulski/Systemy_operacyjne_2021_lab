import Proces
from Proces import Process
from CPU import CPU
import random
from statistics import mean, stdev


def alg1(CPUs, processes, p, z):
    print("Algorytm1")
    above100Counter = 0
    averageLoads = []
    asksForLoad = 0
    time = 0
    migrations = 0

    while processes:
        if processes[0].arriveTime <= time:
            currentProcess = processes[0]
            currentCpu = CPUs[currentProcess.cpuID]
            for i in range(z):
                rand = random.randint(0, len(CPUs) - 1)
                asksForLoad += 1
                if CPUs[rand].getLoadSum() < p:
                    currentCpu = CPUs[rand]
                    migrations += 1
                    break

            currentCpu.processes.append(currentProcess)
            processes.remove(currentProcess)

        time += 1
        if time % 10 == 0:
            loads = []
            for cpu in CPUs:
                loads.append(cpu.getLoadSum())
                if (cpu.getLoadSum() > 100):
                    above100Counter += 1
            averageLoads.append(mean(loads))

        # print("Time: "+str(time))
        for cpu in CPUs:
            cpu.updatePhaseLenghts()

    avg  = mean(averageLoads)
    dev = []
    for load in averageLoads:
        dev.append(abs(avg-load))


    print("Srednie obciazenie:", avg)
    print("Odchylenie:", mean(dev))
    print("Zapytania o obciazenie:", asksForLoad)
    print("Migracje:", migrations)
    print("Czas przeciazenia:", above100Counter)
    print()

def alg2(CPUs, processes, p):
    print("Algorytm2")
    migrations = 0
    asksForLoad = 0
    noFreeCpuCounter = 0
    averageLoads = []
    time = 0
    above100Counter = 0

    while processes:
        if processes[0].arriveTime <= time:
            currentProcess = processes[0]
            currentCpu = CPUs[currentProcess.cpuID]
            asksForLoad += 1
            if currentCpu.getLoadSum() > p:
                freeCpus = []
                for cpu in CPUs:
                    asksForLoad += 1
                    if cpu.getLoadSum() < p:
                        freeCpus.append(cpu)
                if freeCpus:
                    rand = random.randint(0, len(freeCpus) - 1)
                    currentCpu = freeCpus[rand]
                    migrations += 1
                else:
                    noFreeCpuCounter += 1

            currentCpu.processes.append(currentProcess)
            processes.remove(currentProcess)

        time += 1
        if time % 10 == 0:
            loads = []
            for cpu in CPUs:
                loads.append(cpu.getLoadSum())
                if (cpu.getLoadSum() > 100):
                    above100Counter += 1
            averageLoads.append(mean(loads))

        for cpu in CPUs:
            cpu.updatePhaseLenghts()
    avg = mean(averageLoads)
    dev = []
    for load in averageLoads:
        dev.append(abs(avg - load))
    print("Srednie obciazenie:", avg)
    print("Odchylenie:", mean(dev))
    print("Zapytania o obciazenie:", asksForLoad)
    print("Migracje:",migrations)
    print("Czas przeciazenia:",above100Counter)
    print("Sytuacje gdy nie bylo procesora ponizej progu p:",noFreeCpuCounter)
    print()


def alg3(CPUs, processes, p, r):
    print("Algorytm3")
    migrations = 0
    asksForLoad = 0
    noFreeCpuCounter = 0
    averageLoads = []
    time = 0
    above100Counter = 0

    while processes:
        belowR = []
        aboveP = []
        for cpu in CPUs:
            asksForLoad += 1
            if cpu.getLoadSum() < r:
                belowR.append(cpu)
            if cpu.getLoadSum() > p:
                aboveP.append(cpu)
        if aboveP and belowR:
            for cpu in belowR:
                temp = random.choice(aboveP)
                if temp.processes:
                    proces = random.choice(temp.processes)
                    temp.processes.remove(proces)
                    cpu.processes.append(proces)
                    migrations += 1

        if processes[0].arriveTime <= time:
            currentProcess = processes[0]
            currentCpu = CPUs[currentProcess.cpuID]
            asksForLoad += 1
            if currentCpu.getLoadSum() > p:
                freeCpus = []
                for cpu in CPUs:
                    if cpu.getLoadSum() < p:
                        freeCpus.append(cpu)
                if freeCpus:
                    rand = random.randint(0, len(freeCpus) - 1)
                    currentCpu = freeCpus[rand]
                    migrations += 1
                else:
                    noFreeCpuCounter += 1
            currentCpu.processes.append(currentProcess)
            processes.remove(currentProcess)

        time += 1
        if time % 10 == 0:
            loads = []
            for cpu in CPUs:
                loads.append(cpu.getLoadSum())
                if (cpu.getLoadSum() > 100):

                    above100Counter += 1
            averageLoads.append(mean(loads))

        for cpu in CPUs:
            cpu.updatePhaseLenghts()

    avg = mean(averageLoads)
    dev = []
    for load in averageLoads:
        dev.append(abs(avg - load))
    print("Srednie obciazenie:", avg)
    print("Odchylenie:", mean(dev))
    print("Zapytania o obciazenie:", asksForLoad)
    print("Migracje:", migrations)
    print("Czas przeciazenia:", above100Counter)
    print("Sytuacje gdy nie bylo procesora ponizej progu p:", noFreeCpuCounter)
    print()
