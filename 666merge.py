import os

directory = os.path.dirname(os.path.realpath(__file__))
ext = 66600
found = False

for filename in os.listdir(directory):
    if str(ext) in filename:
        print(filename)
        merged = os.path.splitext(filename)[0]
        found = True

if found == True:
    print('merging '+merged)
    with open(merged, 'w') as outfile:
        for filename in os.listdir(directory):
            if str(ext) in filename:
                ext = ext+1
                with open(filename) as infile:
                    for line in infile:
                        outfile.write(line)
    print(merged+' merged successfully!')
else:
    print('No Split PS3 Files Found.')

input('Press ENTER To Close This Window.')