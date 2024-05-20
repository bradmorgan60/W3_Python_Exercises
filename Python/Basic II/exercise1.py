'''
1. Write a Python function that 
   takes a sequence of numbers and determines whether all 
   the numbers are different from each other.
'''

# to note, sets in Python remove duplicates

def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False
    
print(test_distinct([1,2,3,4]))
print(test_distinct([1,1,2,3,4,4]))


my_set1 = {1,2,3,4,5,5,6}
my_set2 = {10,11,12}
my_set3 = {69, 70}
print(my_set1)
my_set1.update([7,8], my_set3)

print(my_set1)


