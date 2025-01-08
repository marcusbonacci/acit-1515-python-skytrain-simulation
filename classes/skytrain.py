from classes.linkedlist import linkedlist

class skytrain:
    def __init__(self, route):
        self.route = linkedlist(route[0])
        self.currentStation = self.route.data

        for station in reversed(route[1:]):
            self.route.connect(station)

    # def start(self):
    #     newIter = iter(self.route)

    def __str__(self):
        return str(self.route)

# newTrain = skytrain(['A', 'B', 'C', 'D'])
# print(newTrain)