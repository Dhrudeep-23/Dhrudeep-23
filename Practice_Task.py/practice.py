# String
# 1. Reverse the given string (You can take any string)
d="I am  Dhrudeep"
print("Reverse:",d[::-1])

# 2. Replace some character of the string with another character without using a loop.
d="I am  Dhrudeep"
print("\nReplace:",d.replace("I am", "Myself"))

# 3. Find whether the character in the given string or not.
d="This is Buggati"
if "B" in d:
    print("\nThe character 'B' is present.")
else:
    print("\nThe character 'B' is not present.")

# 4. Create tuple, list and set and convert them into the different strings.
x_tuple=("Dhrudeep",23,"Vaghasiya")   
y_list=["Dhrudeep",23,"Vaghasiya"]  
z_set={"Dhrudeep",23,"Vaghasiya"} 
print("\n",str(x_tuple))
print(str(y_list))
print(str(z_set))

# 5. Convert all the string characters to the upper and the lower case and split it with the        different methods.
q="Hello Moto"
print("\nUpper Case:",q.upper())
print("Lower Case:",q.lower())
print("Split:",q.split(' '))
print("Split:",list(q))


# 6. Perform the following operations to the tuple and the list 
# 	Find max, min, len, sum
tup=(9,8,7,5)
lis=[99,8,7,1]
print("\nMAX:",max(tup),"MIN:",min(tup),"LEN:",len(tup),"SUM:",sum(tup))
print("MAX:",max(lis),"MIN:",min(lis),"LEN:",len(lis),"SUM:",sum(lis))

# 7. Copy one list to the another list without using the copy command.
lis=["BMW","Ferrari","Thar"]
coopy=lis[:]
print(coopy)

# 8. Perform below task as instructed
# 	-> Create a dictionary named student with keys: 'name', 'age', and 'grade'. Assign 	values accordingly.
# 	Access Dictionary Values:
# 	-> Print the 'age' of the student from the dictionary created in Exercise 1.
# 	Modify Dictionary Values:
# 	-> Update the 'grade' of the student to a new value.
# 	-> Check if the key 'gender' is present in the student dictionary. Print a message 	based on the result.
student={'Name':'Dhrudeep','Age':19,'Grade':'A'}
print("\nAge:",student['Age'])
student['Grade']='AA'
print("Grade:",student['Grade'])
if 'Gender' in student:
    print("Present")
else:
    print("Not Present")


# 9. Perform below task as instructed
# 	-> Create two sets: set1 with elements (1, 2, 3) and set2 with elements (3, 4, 5).
# 	Union of Sets:
# 	-> Find the union of set1 and set2 and print the result.
# 	Intersection of Sets:
# 	-> Find the intersection of set1 and set2 and print the result.
# 	Difference of Sets:
# 	-> Find the elements that are in set1 but not in set2 and print the result.
# 	Check Subset:
# 	-> Check if set1 is a subset of set2. Print a message based on the result.
set1={1,2,3}
set2={3,4,5}
print("\nUnion:",set1|set2)
print("Intersection:",set1&set2)
print("Difference:",set1-set2)
print("Subset",set1.issubset(set2))


# 10. Perform below task as instructed
# 	Create a dictionary where keys are subjects ('math', 'science') and values are sets 	of students who take those subjects.
# 	Update Set Values:
# 	Add a new student to the 'math' subject in the dictionary from Exercise 11.
# 	Remove Set Values:
# 	Remove a student from the 'science' subject in the dictionary from Exercise 11.
# 	Check Common Students:
# 	Find and print the students who take both 'math' and 'science'.
# 	Nested Dictionary:
# 	Create a nested dictionary where each key represents a country, and the value is 	another dictionary containing cities and their populations.
subjects={'math':{'Dhrudeep','kunj','krish'},'science':{'kalapn','utsav','om','kunj'}}
subjects['math'].add('Ram')
print("\nUpdate:",subjects)

subjects['science'].remove('om')
print("Remove:",subjects)

print("Common Student:",subjects['math'] & subjects['science'])

countries = {
    'India': {
        'Junagadh': 362001 ,
        'Delhi': 1122,
        'Bangalore': 123456
    },
    'USA': {
        'New York': 11,
        'Los Angeles': 22,
        'Chicago': 33
    },
    'China': {
        'Shanghai': 44,
        'Beijing': 55,
        'Guangzhou': 66
    }
}
print(countries)


# 11. Create two lists, one containing elements at even indices and the other containing elements at odd indices from the original list.
student = {'name': 'Roy', 'age': 21, 'grade': 'A', 'science': {'Jon': {'age': 23, 'grade': 'A'}, 'Bob': {'age': 21, 'grade': 'B'}}}
if 'science' in student:
    if 'Alice' in student['science']:
        removed_student = student['science'].pop('Alice')
        print("Removed student from 'science' subject:", removed_student)
    else:
        print("Student 'Alice' not found in 'science' subject.")
else:
    print("No 'science' subject found in the dictionary.")

print("\nUpdated dictionary:", student)

# 12. Use tuple packing and unpacking to swap the values of two variables without using a temporary variable.
a = 5
b = 10
a, b = b, a

print("\na after swapping:", a)
print("b after swapping:", b)

# 13. Check if a given list is a palindrome using slicing.
def is_palindrome(lst):
    return lst == lst[::-1]

test_list1 = [1, 2, 3, 4, 5]
test_list2 = [1, 2, 3, 2, 1]

print("\n",is_palindrome(test_list1))
print(is_palindrome(test_list2))

# 14. oncatenate two tuples without using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concated_tuple = *tuple1,*tuple2
print("\n",concated_tuple)