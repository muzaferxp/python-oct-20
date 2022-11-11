data = {
    "hyd_branch" : {
        "cse" : {
            "sec-a" : ["a", "b", "c"],
            "sec-b" : ["x", "y", "z"]
        },
        "civil" : {
            "sec-a" : ["d", "e", "f"],
            "sec-b" : ["g", "h", "i"]
        }
    }
}

print(data['hyd_branch']['civil']['sec-a'][1])