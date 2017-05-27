# Describe the sketch comedy group
name = 'Monty Python'
description = 'sketch comedy group'
year = 1969

# Introduce them
sentence = name + ' is a ' + description + ' formed in ' + str(year)

# python
print(sentence)
# python3
print(name, 'is a', description, 'formed in', year)

# Describe Monty Python's work
famous_sketches = "Hell's Grannies"
print(famous_sketches)

famous_sketch1 = "\n\tHell's Grannies"
famous_sketch2 = '\n\tThe Dead Parrot'

# python
print('Famous Work:' + famous_sketch1 + famous_sketch2)
# python3
print('Famous Work:', famous_sketch1, famous_sketch2)

# 2.2 Print Output
greeting = "G'day"
print(greeting)

# 2.3 String Concatenation
greeting = "G'day" + " mate"
print(greeting)

# 2.4 Cast Number to String
number = 2
print(str(number))
# 2.5 Getting Started with Python Strings
name = "Key & Peele"
description = "The Key & Peele comedy show"
year = 1995
sentence = name + description + str(year)
print(sentence)
print(name, description, str(year))

# 2.6 String Formatting
movie1 = '\n\tIron Man'
movie2 = "\n\tMarvel's Avengers"
# python
print("My Favorite Movies:" + movie1 + movie2)
# python3
print("My Favorite Movies:", movie1, movie2)

# 2.7 Strings and Slices
# A string is a list of characters, and each character in this list has a position or an index.
greeting = 'HELLO WORLD!'
print greeting[0]
print greeting[11]

# len() returns the length of a string
# print the length of greeting
print(len(greeting))

# The man who only says ends of words
word1 = 'Good'
end1 = word1[2] + word1[3]
print(end1)

# Using slices to access parts of a string
# slice formula: variable[start:end]
word = 'Python'
# Print charactesr at index 2, 3, and 4
print(word[2:5])
print(word1[0:2])

end2 = word[2:4]
print(end2)

word2 = 'Evening'

end1 = word1[2:]
end2 = word2[3:]

# python
print(end1)
print(end2)
# python3
print(end1, end2)

# Calculate the halfway index of our word
# Integer division // rounds down to the nearest integer
word1 = 'Good'
half1 = len(word1)//2
print(half1)
print(word1[half1:])

word2 = 'Evening'
half2 = len(word2)//2
print(half2)
print(word2[half2:])

# 2.8 Slicing to Create a Substring
word = "scallywag"
sub_word = word[2:6]
print(sub_word)

# 2.9 Pythonese
word = 'Python'
first = word[0]
rest = word[1:]
print(rest)
result = rest + '-' + first + 'y'
print(result)
