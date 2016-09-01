import sys
import string

# list of alphabets
mappingList = (string.ascii_uppercase)

def mapToAplhabets(x):
    return mappingList[x]

def mapToIndex(c):
    return mappingList.index(c)

#find nearest empty seat
def findEmpty():
    for j in range(length):
        for i in range(width):
            if plane[j][i] == 0:
                return j,i

print 'Argument count : ', len(sys.argv)
# exit if file name is not provided as command line argument
if len(sys.argv) != 2:
    print 'Please input file name as command line argument'
    exit(0)

fileName = sys.argv[1]
print 'File name : ', sys.argv[1]

# read all lines of file
fileHandler = open(fileName,"r")
lines = fileHandler.readlines()
fileHandler.close()

width = int(lines[0])
length = int(lines[1])

#print width, length
#print seatingList

#2D list representing seats in a plane
plane = [[0 for x in range(width)] for y in range(length)]

#List of passengers
seatingList = lines[2].split(',')

#dictionary to maintain paths of each lazy passenger
lazyList = {}

for item in seatingList:
    if '*' not in item:
        alpha = item[0]
        #if normal passenger, fill up that seat
        if plane[int(item[1:]) - 1][mapToIndex(alpha)] == 0:
            plane[int(item[1:]) - 1][mapToIndex(alpha)] = 1
        else:
            #move lazy passenger first
            lazyItem = plane[int(item[1:])-1][mapToIndex(alpha)]
            plane[int(item[1:]) - 1][mapToIndex(alpha)] = 1

            j, i = findEmpty()
            nextLoc = mapToAplhabets(i) + str(j + 1)
            plane[j][i] = lazyItem
            lazyList[lazyItem].append(nextLoc)
    else:
        #if lazy passenger, find nearest empty seat and fill up temporarily
        lazyList[item] = []
        j,i = findEmpty()
        nextLoc = mapToAplhabets(i) + str(j + 1)
        plane[j][i] = item
        lazyList[item].append(nextLoc)

#print plane

#print paths of all lazy passengers
for key in lazyList.keys():
    path = lazyList[key]
    for item in path[:-1]:
        print item+',',
    print path[-1],
    print

#print lazyList


