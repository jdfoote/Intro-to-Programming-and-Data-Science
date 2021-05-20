NAMES_LIST = "yob2018.txt"

boys = {}
girls = {}

for line in open(NAMES_LIST, 'r').readlines():
    name, gender, count = line.strip().split(",")
    count = int(count)

    if gender == "F":
        girls[name.lower()] = count
    elif gender == "M":
        boys[name.lower()] = count
