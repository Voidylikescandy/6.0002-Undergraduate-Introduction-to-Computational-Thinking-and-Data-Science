###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cows = {}
    file = open(filename, "r")
    for line in file:
        contents = line.split(",")
        contents[1] = contents[1].strip()
        cows[contents[0]] = int(contents[1])
    file.close()
    return cows

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    transportOrder = []
    cowsSorted = dict(sorted(cows.items(), key=lambda cow:cow[1], reverse=True))
    
    while 1:
        capacity = limit
        cowTrip = []
        cowAdded = False
        for cow in cowsSorted:
            if cowsSorted[cow] == -1:
                continue
            if cowsSorted[cow] <= capacity:
                cowTrip.append(cow)
                capacity -= cowsSorted[cow]
                cowsSorted[cow] = -1
                cowAdded = True
        if not cowAdded:
            break
        transportOrder.append(cowTrip)
    return transportOrder



# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cowsNames = []
    for cow in cows:
        cowsNames.append(cow)
    transportOrder = []
    bestTrip = 100100
    for partition in get_partitions(cowsNames):
        validTrip = True
        for trip in partition:
            weight = 0
            for cow in trip:
                weight += cows[cow]
            if weight > limit:
                validTrip = False
                break
        if validTrip:
            if len(partition) < bestTrip:
                bestTrip = len(partition)
                transportOrder = partition
    return transportOrder

        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    start = time.time()
    transportOrder = greedy_cow_transport(cows)
    end = time.time()
    print("Greedy - ", len(transportOrder))
    print(end - start)
    start = time.time()
    transportOrder = brute_force_cow_transport(cows)
    end = time.time()
    print("Brute Force - ", len(transportOrder))
    print(end - start)

compare_cow_transport_algorithms()