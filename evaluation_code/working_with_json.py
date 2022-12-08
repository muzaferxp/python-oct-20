import json

file_path = "evaluation_code/data/sample.json"

#Step 1: Read and parse the data
f = open(file_path)
data = json.load(f)  #parse the json to convert str to dict
f.close()

for x in data['students']:
    print(x)
    
#Step 2: Write the data to json file
data['students'].append({'name': 'David Thomas', 'roll_no': '556'})

f = open(file_path, "w")
f.write( json.dumps(data,  indent = 4),  )  #convert dict to str before writing
f.close()