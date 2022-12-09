
#D:\PythonOct20\restapi\data\data.csv
#data\data.csv
file_path = "data/data.csv"

def searchProduct(text):
    data = []
    queries = text.split(",")
    f=open(file_path)
    for line in f:
        isRecordFound = True 
        for query in queries:
            if query not in line:
                isRecordFound = False
                
        if isRecordFound == True:      
            data.append(line.split(","))
    f.close()    
    return data
    
