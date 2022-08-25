import os

directory = os.path.dirname(os.path.realpath(__file__))
ext = 66600
index = 0
chunk_size = 4 * 1024 * 1024

filesToMerge = [os.path.join(root, os.path.splitext(name)[0])
             for root, dirs, files in os.walk(directory)
             for name in files
             if name.endswith((str(ext)))]

results = len(filesToMerge)
if results > 0:
    print("The Following " + str(results) + " Files Have Been Split:")
    for each in filesToMerge:
        print(each)
    merge = input("\nWould You Like To Merge These Files? Y/N").upper()
    
    if merge == 'Y':
        while index < results:
            with open(filesToMerge[index], 'w') as outfile:
                for subdir, dirs, files in os.walk(directory):
                    for file in files:
                        fullDir = subdir + os.sep + file
                        shortDir = (os.path.splitext(fullDir)[0])
                        if shortDir == (filesToMerge[index]):
                            print("Merging " + fullDir + " Into " + filesToMerge[index])
                            with open(fullDir, 'rb') as infile:
                                for chunk in iter(lambda: infile.read(chunk_size), b''):
                                    outfile.buffer.write(chunk)
            index = index+1
        input("Merging Complete!\nPress ENTER To Close This Window.")
else:
    print("No Split PS3 Game Files Found.")
    input("Press Enter to Close this Window.")