# External Classes
# from classes.linkedlist import linkedlist
from classes.skytrain import skytrain

# Data
from data.stations import stations

def main():
    print("Starting Skytrain simulation")

    newSkytrain = skytrain(stations[:])
    # newSkytrain.start()

    # Visualization
    # print(newSkytrain.route.data)
    # print(newSkytrain.route.next.data)
    # print(newSkytrain.route.next.next.data)
    # print(newSkytrain.route.next.next.next.data)
    # print(newSkytrain.route.next.next.next.next.data)

if __name__ == "__main__":
    main()