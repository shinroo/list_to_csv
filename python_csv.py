#    Python script to convert list of strings in text file to comma seperated
#    with either 2 or 4 columns
#    Copyright (C) 2016  Robert Focke
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os.path
import sys

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

filename = sys.argv[1]
if RepresentsInt(sys.argv[2]):
	mode = int(sys.argv[2])
else:
	sys.exit('the output mode must be an integer')

if os.path.isfile(filename):
	file = open(filename,'r')
else:
	sys.exit('file does not exist')

data = file.readlines()

if len(data) % mode == 0:
	outputfile = open('output.txt','w')
	length = len(data)
	file.close()
	file = open(filename,'r')
	if mode == 2:
		for x in range(0, int(len(data)/2)):
			outputfile.write(file.readline().rstrip() + ',' + file.readline().rstrip() + '\n')
	elif mode == 4:
		for x in range(0, int(len(data)/4)):
			outputfile.write(file.readline().rstrip() + ',' + file.readline().rstrip() + ',' + file.readline().rstrip() + ',' + file.readline().rstrip() + '\n')
	else:
		sys.exit('the given output mode is not supported, please enter 2 or 4')
else:
	sys.exit('file is not formatted correctly for given output mode, number of lines is incorrect')
