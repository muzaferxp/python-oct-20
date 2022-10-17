vahicles = [{"type" : "Car","name" : "Car 1"},
    {
        "type" : "Car",
        "name" : "Car 2"
    },
    {
        "type" : "Bike",
        "name" : "Bike 1"
    },
     {
        "type" : "Bike",
        "name" : "Bike 2"
    }
]

def getCars():
    print("======GETTING CARS==========")
    for v in vahicles:
        if v['type'] == "Car":
            print(v)
        else:
            print("Not a car")
        
    
def getBikes():
    print("======GETTING BIKES")
    for v in vahicles:
        if v['type'] == "Bike":
            print(v)
        else:
            print("Not a Bike")
    
getBikes()
