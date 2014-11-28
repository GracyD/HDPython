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
julie_t = reader('julie.txt')
mikey_t = reader('mikey.txt')
sarah_t = reader('sarah.txt')

james = set(sorted([sanitize(each_item) for each_item in james_t]))
julie = set(sorted([sanitize(each_item) for each_item in julie_t]))
mikey = set(sorted([sanitize(each_item) for each_item in mikey_t]))
sarah = set(sorted([sanitize(each_item) for each_item in sarah_t]))

print sorted(james)[0:3]
print sorted(julie)[0:3]
print sorted(mikey)[0:3]
print sorted(sarah)[0:3]

