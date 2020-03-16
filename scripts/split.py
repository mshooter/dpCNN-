import random 
import os
import sys

default_path = "../birds"

ALLFILE     = os.path.join(default_path,"allimages.txt")
TRAINFILE   = os.path.join(default_path,"train.txt")
VALIDFILE   = os.path.join(default_path,"val.txt")
TESTFILE    = os.path.join(default_path,"test.txt")

TRAINPERC = float("%.2f" % float(sys.argv[1])) 
VALIDPERC = float("%.2f" % float(sys.argv[2]))
# test percentage is implied

# change this from 1.0 to some lower fraction to subsample the data
# e.g 0.05 will use 5 percent of all the data 
SUBSAMP = 1.0 

def main(): 

    with open(ALLFILE, 'r') as source:

        data    = [ (random.random(), line) for line in source]
        data.sort() 
        train   = open(TRAINFILE, "w")
        valid   = open(VALIDFILE, "w")
        test    = open(TESTFILE, "w")

        count       = len(data)
        cumlvalid   = int(TRAINPERC*count) 
        cumltest    = cumlvalid+int(VALIDPERC*count)

        print("Total records = %d" % count)
        print("Train %d%% = %d" % (round(TRAINPERC*100), cumlvalid))
        print("Valid %d%% = %d" % (round(VALIDPERC*100), cumltest-cumlvalid))
        print("Test  %d%% = %d" % (round((1-TRAINPERC-VALIDPERC)*100), count-cumltest))
        
        didwrite    = 0 
        ctr         = 0
        for _, line in data: 
            if(ctr>=cumltest):
                if(random.uniform(0,1) < SUBSAMP):
                    test.write(line) 
            elif(ctr>=cumlvalid):
                if(random.uniform(0,1) < SUBSAMP): 
                    valid.write(line) 
            else:
                if(random.uniform(0,1) < SUBSAMP): 
                    train.write(line)
                    didwrite=didwrite+1
            ctr=ctr+1

        train.close()
        valid.close()
        test.close()

        print("Wrote training data %d" % didwrite)

if __name__ == "__main__":

    main()
