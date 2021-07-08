from Algorithms import Algorithms

#
FRAME_COUNT = 200
REQUESTS_AMOUNT = 10000







PAGESAMOUNT = 250
PROCESSES_COUNT = 10
PPF_COEF = 0.7
ZONE_COEF=40
LOCAL_PROB = 0.01
MAX_LOCAL_COUNT = 100
MAX_LOCAL_SUBSET_SIZE = 10


a = Algorithms(FRAME_COUNT, REQUESTS_AMOUNT, PAGESAMOUNT, PROCESSES_COUNT, PPF_COEF, ZONE_COEF
               , LOCAL_PROB, MAX_LOCAL_COUNT, MAX_LOCAL_SUBSET_SIZE)

print("Equal: " + str(a.equal()))
print("Proportional: " + str(a.proportional()))
print("Steering Page Fault Frequency: " + str(a.steering_fault_frequency()))
print("Zone Model Algorithm: " + str(a.zone()))