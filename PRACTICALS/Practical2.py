# Practical 2

# (A)Create a list and apply methods(append, extend, remove, reverse), arrange created list into the ascending and descending order

friends = ['Kunj', 'Krish', 'Utsav', 'Kalpan']
friends.append('Dhrudeep')
print(friends)
friends.reverse()
print(friends)
friends.remove('Kalpan')
print(friends)
friends.extend(['Kirtan'])
print(friends)
print(sorted(friends))
print(friends)
friends.sort()
print(friends)
friends.sort(reverse = True)
print(friends)

# (B)
List1 = [1, 2, 3, 4, ['Pyton', 'Java', 'C++',[10, 20, 30]], 5, 6, 7, ['WaterMelon', 'GrapeFruit', 'PassionFruit']]

values = List1[4][0:1] + List1[8][2:3]
five_values = [values] * 5
print(five_values)

# (C)
cars = ['Mustang', 'Porsche', 'BMW', 'Supra', 'Mercedes']
duplicate_cars = cars[:]
print(duplicate_cars)

# (D)
numbers = (3, 7, 1, 50, 20)
print(max(numbers))
print(min(numbers))
print(sum(numbers))