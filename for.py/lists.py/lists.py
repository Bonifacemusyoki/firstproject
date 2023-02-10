#my first python list
names=["tush","marto"]
print(names[0])
print(names[1])
numbers=[2,4,6,8,10,12]
print(len(numbers))
print(sum(numbers))
for i in range(len(numbers)):
    print(numbers[i])

print(numbers.index(4))


# LIST METHODS
#Index-gets the index of an element in a list
#Append-adds an element to the end of a list
# before appending
for i in range(len(numbers)):
    print(numbers[i])
    numbers.append(90)
    
    # after appending
    for i in range(len(numbers)):
        print(numbers[i])

#sort-sorts the numbers from  least to the highest value
numbers.sort()
for i in range(len(numbers)):
    print(numbers[i])


#count-returns the number of times an element occurs in a list
print(numbers.count(90))
#pop-removes an element at a given index and returns that element
print(numbers.pop(2))


#insert-inserts an element x at index y
numbers.insert(2,100)
for i in range(len(numbers)):
    print(numbers[i])
#remove-removes a number the first occurence of a number in a given list

numbers.remove(90)

# creating lists
nums=[] #creating an empty list
for i in range(10):
    nums.append(i)

for i in range(len(nums)):
    print(nums[i])

even_nums=[]
for num in range(20):
 if(num % 2==0):
    even_nums.append(num)

for i in range(len(even_nums)):
    print(even_nums[i])