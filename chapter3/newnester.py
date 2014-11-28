from __future__ import print_function
import pickle
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
        with open('man_data2.txt', 'wb') as manout:
            pickle.dump(man, manout)

        with open('other_data2.txt', 'wb') as otherout:
            pickle.dump(other, otherout)

except IOError as err:
        print("Out file error: ", + str(err))
except PickleError as perr:
    print("Pickle error: ", + str(perr))
