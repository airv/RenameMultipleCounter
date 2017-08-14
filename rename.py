import os
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit()
    

    DIRECTORY_TO_LIST = sys.argv[1]
    print "rename the files in the directory : " + DIRECTORY_TO_LIST + "..."

    counter = 0
    Counter_file = 0
    for root, directories, files in os.walk(DIRECTORY_TO_LIST):
        for filename in files:
            filepath = os.path.join(root, filename)
            name, extension = os.path.splitext(filename)
            new_file = os.path.join(root, str(counter) + extension)
            # try to find a counter does not exist
            while os.path.exists(new_file) is True:
                new_file = os.path.join(root, str(counter) + extension)
                counter += 1
            os.rename(filepath, new_file)
            print ("old file : " + filepath + "--- new file : " +
                   os.path.join(root, str(counter) + extension))

            Counter_file += 1
            counter += 1

    print "rename " + str(Counter_file) + " files ! "
