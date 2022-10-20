# #List Methods
# 1. len
# 2. .sort()
# 3. .reverse()
# 4. min()
# 5. max()
# 6. .append()
# 7. .remove()
# 8. .insert()  


fruits = ["Blog1", "Blog2", "Blog3", "Blog4"]

print(fruits)

#1. to get length of the List
print("Length of the list is:",len(fruits))


#2. Reverse the list
fruits.reverse()
print(fruits)

#3. Sort
tech = ["Python", "Java", "Html", "Css"]

#sorting a to z
tech.sort()

print(tech)

markList=[50,40,70]

#sorting low to hight
markList.sort()
print(markList)

#reversing to get highest to lowest
markList.reverse()
print(markList)

#4 Min
minMarks = min(markList)
print(minMarks)


#5 Max
print(max(markList))


#6 append (add item to the array)
markList.append(65)

print(markList)

#7. remove  (delete)
markList.remove(40)
print(markList)
 
#8 insert
markList.insert(1, 100)
print(markList)
