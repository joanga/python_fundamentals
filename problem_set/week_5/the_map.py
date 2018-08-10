#1.Find a path to get from node 0 to node 499
#investigate 100 paths and pick the best (fewer miles)
    #what is the different between best and worst
#Of all paths how do we find the very best

#Use classes

#make a useful print() statement that tell us something worth knowing

#Use len().

import pickle
import random
# QUESTION: 
with open ('map.pkl', 'rb') as f:
    map = pickle.load(f)

class Car():
    def __init__(self, origin = 0 , destination = 499):
        self.milage = 0
        self.origin = 0
        self.destination = destination
        self.path = [origin] #needs to be ordered because its the path traveled

    def current_location(self):
        return self.path[-1]

    def arrrived(self):
        return self.current_location() == self.destination

    def find_path(self):
        possible_paths = []
        for key,value in map.items():
            if self.origin in key:
                possible_paths.append(list(key)[1])

        #print (possible_paths)
        next = random.choice(possible_paths)
        print(next)



if __name__ == '__main__':
    subaru = Car()
    subaru.find_path()
