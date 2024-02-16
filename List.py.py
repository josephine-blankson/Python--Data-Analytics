age = [12, 34, 56, 67]
print("initial list:", age)


# INDEXING wwhich means positioning. And to index an element , you must use a square bracket [],
age= [4, 6, 7, 8, 9, 0]
print("accessing the fourth number", age[3], age[1])

#  SLICING:  Picking or selecting some elements. it is also used to reduce some number of elements. Use a colon(:) to slice  
age = [1, 3, 5, 67, 67,78]
print(age[5])

# Modifying means changing. 
age[3]= 21
print(age)


# Appending means addition. Adding elements to a loop.
for q in range(14,34):
    age.append(q)
print(age)
    
# Removing elements in a while loop
a = 5
while a in age:
    age.remove(a)







# LEN (length). features of len ; (len(age))
a = "josephineabenablankson"
print(len(a))

# INSERT
u= [6, 8, 3, 7]
u.insert(0,"7")
print(u)
