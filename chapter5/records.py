def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

with open('james.txt') as james, open('julie.txt') as julie, open('mikey.txt') as mikey, open('sarah.txt') as sarah:
    for line in james:
        james_t = line.strip().split(',')

    for line in julie:
        julie_t = line.strip().split(',')

    for line in mikey:
        mikey_t = line.strip().split(',')

    for line in sarah:
        sarah_t = line.strip().split(',')

james_ft = []
julie_ft = []
mikey_ft = []
sarah_ft = []

for i in james_t:
    james_ft.append(sanitize(i))

for i in julie_t:
    julie_ft.append(sanitize(i))

for i in mikey_t:
    mikey_ft.append(sanitize(i))

for i in sarah_t:
    sarah_ft.append(sanitize(i))
    
print("Formatted time data for James, Julie, Mikey and Sarah: ")
print(sorted(james_ft))
print(sorted(julie_ft))
print(sorted(mikey_ft))
print(sorted(sarah_ft))
