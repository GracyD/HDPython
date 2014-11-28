from __future__ import print_function
from nester import print_lol
man = []
other = []

try:
	data = open('sketch.txt')
	for line in data:
		try:
			(role, line_spoken) = line.split(":", 1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()	
except IOError:
	print('The data file is missing!')
	
try:
        with open('man_data1.txt', 'w') as manout:
                #print(man, file=manout)
                print_lol(man, output=manout)

        with open('other_data1.txt', 'w') as otherout:
                #print(other, file=otherout)
                print_lol(other, output=otherout)
#        manout = open("man_data.txt", "w")
#        otherout = open("other_data.txt", "w")
#        print(man, file=manout)
#        print(other, file=otherout)
except IOError as err:
        print("Out file error: ", + str(err))
#finally:
#       manout.close()
#        otherout.close()
