

def getDuplicates(myList):
    duplicateItems = []
    occuredItem = []
    for item in myList:
        if item in occuredItem:
            duplicateItems.append(item)
        else:
            occuredItem.append(item)
        
    print("myList:", myList)
    print("duplicates:", duplicateItems)

l = [0,1,3,1,5,3]
getDuplicates(l) #[1,3]