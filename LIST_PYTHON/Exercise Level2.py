# The following is a list of 10 students ages:

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)
print("Min age:",ages[0])
print("Max age:",ages[-1])

# Add the min age and the max age again to the list
ages.extend([ages[0],ages[-1]])

# Find the median age (one middle item or two middle items divided by two)
middleindex=len(ages) //2
median_age=(ages[middleindex]) //2 
print("\nMedain age:",median_age)   

# Find the average age (sum of all items divided by their number )
print("\nAverage sum:",sum(ages)/len(ages))

# Find the range of the ages (max minus min)
print("\nRange of ages:",max(ages)-min(ages))

# Compare the value of (min - average) and (max - average), use abs() method
min_average=abs(ages[0]-(sum(ages)/len(ages)))
print("\nMin_average:",min_average)
max_average=abs(ages[-1]-(sum(ages)/len(ages)))
print("Max_average:",max_average)

# Find the middle country(ies) in the [countries list]
countries=['India','Canada','Dubai','Russia','Germany']
middle=len(countries)//2
print("\nMiddle country(ies):",countries[middle])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
country=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid=len(country)//2
firsthalf=country[:mid]
secondhalf=country[mid:]
if len(country)%2 !=0:
    firsthalf.append(secondhalf.pop(0))
print("\nFirst half:",firsthalf)
print("Second half:",secondhalf)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
first_three,scandic_countries=country[:3],country[3:]
print("\nFirst Three countries:",first_three)
print("Scandic countries:",scandic_countries)