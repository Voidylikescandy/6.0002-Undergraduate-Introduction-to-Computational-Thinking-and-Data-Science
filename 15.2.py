import random

def flip(numFlips):
    """Assumes numFlips a positive int"""
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
    """Assumes numFlipsPerTrial and numTrials positive ints"""
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    return mean

print("Mean = ", flipSim(10, 100))
print("Mean = ", flipSim(10, 1000))
print("Mean = ", flipSim(10, 10000))
print("Mean = ", flipSim(10, 100000))
print("Mean = ", flipSim(10, 1000000))
print("Mean = ", flipSim(10, 1))
print("Mean = ", flipSim(10, 1))
print("Mean = ", flipSim(10, 1))