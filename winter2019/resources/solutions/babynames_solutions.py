import ssadata

## 1
print("There are {} boys and {} girls with the name 'jeremy'".format(ssadata.boys['jeremy'], ssadata.girls['jeremy']))

## 2

def get_max(d):
    max_name = '' # Intialize the name
    max_count = 0 # Initialize the count
    for name in d.keys(): # Go through each name
        curr_count = d[name]
        # If the count is higher than the current max,
        # then replace it
        if curr_count > max_count:
            max_name = name
            max_count = curr_count
    return (max_name, max_count) # Return the results as a tuple

# Here, we can assign each of the two parts of the result to its own variable
max_boys_name, max_boys_count = get_max(ssadata.boys)
max_girls_name, max_girls_count = get_max(ssadata.girls)

print("The most common girls name is " + max_girls_name)
print("The most common boys name is " + max_boys_name)

## 3

def get_min(d):
    min_name = ''
    min_count = None
    for name in d.keys():
        curr_count = d[name]
        if min_count == None or min_count > curr_count:
            min_count = curr_count
            min_name = name
    return (min_name, min_count)


# Instead of assigning each result to its own variable, we can keep them as a
# tuple (which is like a list), and use indexing to get the one that we want.
print("The least common boys name is " + get_min(ssadata.boys)[0])
print("The least common girls name is " + get_min(ssadata.girls)[0])

## 4

print("The least common boys name appears " + str(get_min(ssadata.boys)[1]) + " times")
print("The least common girls name appears " + str(get_min(ssadata.girls)[1]) + " times")

# You would think it would be one time!

## 5
n_boys = len(ssadata.boys)
n_girls = len(ssadata.girls)

print("There are {} boys names and {} girls names".format(n_boys, n_girls))

# 5 Challenge
n_boys = 0
for name in ssadata.boys.keys():
    n_boys = n_boys +1

def get_num_names(d, letter):
    count = 0
    for name in d.keys():
        if name[0] == letter:
            count = count + 1
    return count


for l in 'abcdefghijklmnopqrstuvwxyz':
    for data in [ssadata.girls, ssadata.boys]:
        num_names = get_num_names(data, l)
        if data == ssadata.girls:
            s = 'girls'
        else:
            s = 'boys'
        print('There are {} {} names that start with {}'.format(num_names, s, l))

## 6

# Combine the names (you can combine lists with '+')
all_names = list(ssadata.boys.keys()) + list(ssadata.girls.keys())

longest_name = ''
for name in all_names:
    if len(name) > len(longest_name):
        longest_name = name

print("The longest name is " + longest_name)

## 7

# Here are 2 different ways to do this
boys_count = sum(ssadata.boys.values())

girls_count = 0
for name in ssadata.girls.keys():
    curr_count = ssadata.girls[name]
    girls_count = girls_count + curr_count

print("There are " + str(boys_count) + " boys and " + str(girls_count) + " girls.")

## Why are there so many more boys than girls?
# Probably because more girls have unique names.

# One simple test of this is to compare how many have the minimum number of people (5)
# with a names

boys_count = 0
for value in ssadata.boys.values():
    if value == 5:
        boys_count = boys_count + value

# This is a more advanced way of doing that, with a "list comprehension"
girls_count = sum([value for value in ssadata.girls.values() if value == 5])

print("There are {} boys with 'unique' names and {} girls with 'unique' names".format(boys_count, girls_count))

## 8

# Boys names that are girls names
boys_count = 0
for name in ssadata.boys.keys():
    if name in ssadata.girls.keys():
        boys_count = boys_count + 1

girls_count = 0
for name in ssadata.girls.keys():
    if name in ssadata.boys.keys():
        girls_count += 1 # This is a shortcut for incrementing a variable

print("There are {} boys names that are also girls names and {} girls names which are also boys names".format(boys_count, girls_count))

# Note that these are the same; if a name is in both lists, it doesn't matter
# which direction you are comparing.

## 9

# I am assuming that this means the most popular among girls,
# not the most popular overall.
most_popular_name = ''
popularity = 0
for name in ssadata.girls.keys():
    if name in ssadata.boys:
        if ssadata.girls[name] > popularity:
            most_popular_name = name
            popularity = ssadata.girls[name]

print("The most popular girls name that is also a boys name "\
    "is {}; {} girls have this name".format(most_popular_name, popularity))

## 10

# I decided to find all of the names that only contain vowels.


for name in all_names: # Reusing all_names from before
    all_vowels = True # Initialize to true
    for letter in name:
        if letter not in 'aeiou':
            all_vowels = False # If a letter isn't a vowel, then set this to False
            break
    if all_vowels == True: # If this is still true, then we know it only has vowels
        print(name + " is composed of only vowels.")
