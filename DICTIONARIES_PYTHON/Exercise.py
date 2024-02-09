# Create an empty dictionary called dog
dog={}

# Add name, color, breed, legs, age to the dog dictionary
dog={
    'name':'Bolt',
    'color':'white',
    'breed':'golden',
    'legs':'4',
    'age':'2'
    }
for Tittle,Details in dog.items():
    print(f"{Tittle.title()}:{Details}")

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={
    'first name':'Dhrudeep',
    'last name':'Vaghasiya',
    'gender':'male',
    'age':'19',
    'marital status':'Single',
    'skills':['Volleyball','JS','E-Gaming'],
    'country':'India',
    'city':'Junagadh',
    'address':'Junagadh'
}
# Get the length of the student dictionary
print('\nLength:',len(student))

# Get the value of skills and check the data type, it should be a list
print('\nValue & data type:',type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills'].append('machine learning')
for key, value in student.items():
    if key == 'skills':
        print(f"{key}: {', '.join(value)}")
    else:
        print(f"{key}: {value}")


# Get the dictionary keys as a list
print("\n",student.keys())

# Get the dictionary values as a list
print("\n",student.values())

# Change the dictionary to a list of tuples using items() method
stu_tuple=student.items()
print("\n",stu_tuple)

# Delete one of the items in the dictionary
student.pop('martial status')
for key, value in student.items():
    if key == 'skills':
        print(f"{key}: {', '.join(value)}")
    else:
        print(f"{key}: {value}")

# Delete one of the dictionaries
del student
