road = ["Start", "Signal", "Turn", "Destination"]

for place in road:
    if place == "Signal":
        print(place, "- Stop and Go")
    elif place == "Turn":
        print(place, "- Turn Left")
    elif place == "Destination":
        print(place, "- Reached")
    else:
        print(place, "- Move Forward")
