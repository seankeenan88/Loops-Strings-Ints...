import itertools


#Irish lotto has 47 numbers 1 - 47
# total combinations = 10,737,573
# Cost of entry €4


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
for L in range(6,len(numbers)):
    for subset in itertools.combinations(numbers, L):
        print(subset)