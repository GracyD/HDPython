from __future__ import print_function
import sys
def print_lol(a_list, indent=False, level=0, output=sys.stdout):
    for each_item in a_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, output)
        else:
			if indent == True:
				for i in range(level):
					print("\t", end='', file=output)
			print(each_item, file=output)     
