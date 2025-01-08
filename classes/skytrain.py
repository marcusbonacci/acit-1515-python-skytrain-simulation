from classes.linkedlist import linkedlist

class skytrain:
    def __init__(self, route):
        self.route = linkedlist(route[0])
        for station in reversed(route[1:]):
            self.route.connect(station)

    def start(self):
        while True:
            self.route.__iter__()
            print(self.route.__next__())

    def __str__(self):
        return str(self.route)

# newTrain = skytrain(['A', 'B', 'C', 'D'])
# print(newTrain)