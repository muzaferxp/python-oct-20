import os, json

folder_path = "evaluation_code/data/logs"


#1. Get list of files in a folder
list_of_files = os.listdir(folder_path)
print(list_of_files)
for file in list_of_files:
    file_path = os.path.join(folder_path, file)
    ext = file_path.split(".")[-1]
    if ext == "txt":
        f = open(file_path, "r")
        for line in f:
            print(line)
        f.close()
        
    elif ext == "json":
        f = open(file_path)
        data = json.load(f)  #parse the json to convert str to dict
        f.close()
        print(data)

    
    

#2. Check if file path exists
file_path = os.path.join(folder_path, "log2.txt")
if os.path.exists(file_path):
    print("File Exists", file_path)
else:
    print("File does not exists", file_path)

#3. Crete a new folder
new_folder_path = os.path.join(folder_path, "new_folder")
if os.path.exists(new_folder_path):
    pass
else:
    os.mkdir(new_folder_path)

#4. Create a zip file (backup)
import shutil
shutil.make_archive("backup", 'zip', new_folder_path)

#5 Delete a file
os.remove("backup.zip.zip")

