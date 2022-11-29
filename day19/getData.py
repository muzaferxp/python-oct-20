
def getDataByChar(char):
    f = open("data/data.csv")
    
    data = []
    for line in f:
        if line[0].lower() == char:
            data.append(line)
            
    return data

def getOptions():
    option = []
    f = open("data/data.csv")
    for line in f:
        option.append(line[0])
    option = list(set(option))
    
    option.sort()
    
    return option      
    

def getCounts():
    
    count  = {}
    
    f = open("data/data.csv")
    for line in f:
        if line[0] not in count:
            count[line[0]] = 1
        else:
            count[line[0]] += 1
            
    print(count)
    
getCounts()
        
        
    
    
    
    