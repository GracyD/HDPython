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
            result_data = {'Name': s_data.pop(0), 'DOB': s_data.pop(0), 'Records': sorted(set([sanitize(t) for t in s_data]))[0:3]}
            return result_data
    except IOError as err:
        print("File IOError: " + str(err))
        return(None)

james = reader('james2.txt')
sarah = reader('sarah2.txt')1
mikey = reader('mikey2.txt')
julie = reader('julie2.txt')

print(james['Name'] + "'s fastest times are: " + str(james['Records']))
print(sarah['Name'] + "'s fastest times are: " + str(sarah['Records']))
print(mikey['Name'] + "'s fastest times are: " + str(mikey['Records']))
print(julie['Name'] + "'s fastest times are: " + str(julie['Records']))
