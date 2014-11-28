def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def reader(filename):
    try:
        with open(filename) as rf:
            data = rf.readline()
            s_data = data.strip().split(',')
            return s_data
    except IOError as err:
        print("File IOError: " + str(err))
        return(None)

james_t = reader('james.txt')


    
james = sorted([sanitize(each_item) for each_item in james_t])
julie = sorted([sanitize(each_item) for each_item in julie_t])
mikey = sorted([sanitize(each_item) for each_item in mikey_t])
sarah = sorted([sanitize(each_item) for each_item in sarah_t])

unique_james = set(james)
unique_julie = set(julie)
unique_mikey = set(mikey)
unique_sarah = set(sarah)


for item in julie:
    if item not in unique_julie:
        unique_julie.append(item)

for item in mikey:
    if item not in unique_mikey:
        unique_mikey.append(item)

for item in sarah:
    if item not in unique_sarah:
        unique_sarah.append(item)

print james
print sorted(unique_james)[0:3]
