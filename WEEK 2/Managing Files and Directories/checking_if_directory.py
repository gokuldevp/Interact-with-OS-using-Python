import os 

dir="website"
for name in os.listdir(dir):
    fullname=os.path.join(dir, name)
	if os.path.isdir(fullname):
	    print("{} is a directory".format(fullname))
	else:
	    print("{} is a file".format(fullname))