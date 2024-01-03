# Declare an empty list
list_empty=[]

# Declare a list with more than 5 items
car=['BMW','Buggati','Thar','Ferrari','Lamborgini'] 

# Find the length of your list
print("\nLength of the list:",len(car))

# Get the first item, the middle item and the last item of the list
print("\nFirst item:",car[0])
print("Middle item:",car[2])
print("Last item:",car[4])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Dhrudeep','19','5.5','Single','Junagadh']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

# Print the list using print()
print('\n',it_companies)

# Print the number of companies in the list
print("\nNumber of companies in the list:",len(it_companies))

# Print the first, middle and last company
print("\nFirst:",it_companies[0])
print("Middle:",it_companies[3])
print("Last:",it_companies[6])

# Print the list after modifying one of the companies
it_companies[0]='JAVA'
print("\nModified List:",it_companies)

# Add an IT company to it_companies
it_companies.append("TCS")
print("\nAdd IT_company:",it_companies)

# Insert an IT company in the middle of the companies list
middle=len(it_companies)//2
it_companies.insert(middle,'Tech Manhindra')
print("\nInsert in the middle:",it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies=it_companies[4].upper()
print("\nUpper case:",it_companies)

# Join the it_companies with a string '#;  '
print("\nJoined:",'#; '.join(it_companies))

# Check if a certain company exists in the it_companies list.
if 'Samsung' in it_companies:
    print("\nSamsung is in the list of IT companies.")
else:
    print("\nSamsung is not in the list of IT companies.")

# Sort the list using sort() method
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.sort()
print("\nSorted:",it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print("\nReverse:",it_companies)

# Slice out the first 3 companies from the list
print("\nSlice:",it_companies[0:3])

# Slice out the last 3 companies from the list
print("\nSlice from last:",it_companies[-3::])

# Slice out the middle IT company or companies from the list
if len(it_companies)%2!=0:
    print("\nSlice from middle:",it_companies[len(it_companies)//2])

# Remove the first IT company from the list
print("\nPOP:",it_companies.pop(0))

# Remove the middle IT company or companies from the list
print("\nPOP from middle:",it_companies.pop(len(it_companies)//2))

# Remove the last IT company from the list
print("\nPOP from last:",it_companies.pop(-1))

# Remove all IT companies from the list
print("\n",it_companies.clear())

# Destroy the IT companies list
del it_companies

# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
back_end = ['Node','Express', 'MongoDB']
fullstack=front_end+back_end
print("\n",fullstack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
fullstack.insert(fullstack.index('Redux') + 1, "Python")
fullstack.insert(fullstack.index('Redux') + 2, "SQL")
print("\n",fullstack)

 




