from classes.skytrain import skytrain
from classes.linkedlist import linkedlist

# Variables / Data
stations = [
    "king george",
    "surrey central",
    "gateway",
    "scott road",
    "columbia",
    "new westminster",
    "22nd street",
    "edmonds",
    "royal oak",
    "metrotown",
    "patterson",
    "joyce-collingwood",
    "29th avenue",
    "nanaimo",
    "commercial-broadway",
    "main street-science world",
    "stadium-chinatown",
    "granville",
    "burrard",
    "waterfront"
]

def main():
    print("Starting Skytrain simulation")

    newSkytrain = skytrain(stations[:])
    newSkytrain.start()

    # Visualization
    # print(newSkytrain.route.data)
    # print(newSkytrain.route.next.data)
    # print(newSkytrain.route.next.next.data)
    # print(newSkytrain.route.next.next.next.data)
    # print(newSkytrain.route.next.next.next.next.data)



if __name__ == "__main__":
    main()