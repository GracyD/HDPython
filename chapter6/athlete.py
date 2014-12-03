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
            return Athlete(s_data.pop(0), s_data.pop(0), s_data)
    except IOError as err:
        print("File IOError: " + str(err))
        return(None)

class Athlete:
    def __init__(self, a_name, a_dob=None, a_data=[]):
        self.name = a_name
        self.dob = a_dob
        self.records = a_data

    def top3(self):
        return sorted(set(sanitize(t) for t in self.records))[0:3]

    def add_time(self, n_record=0):
        return self.records.append(n_record)

    def add_times(self, n_records=[]):
        return self.records.extend(n_records)


james = reader('james2.txt')

print(james.name + "'s fastest times are: " + str(james.top3()))

james.add_time('1:26')
print james.records
print james.top3()
james.add_times(['1:27', '2:08'])
print james.records
print james.top3()
