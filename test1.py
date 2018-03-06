# Test your code for the graded functions name_generator() & directory_creator()
import os
import shutil
import datetime
import math
import random

def directory_count():
    """
    Calculate the number of directories to be generated.
    
    I) Get the current minute using appropriate functionality from `datetime`
    II) Take the square root of ..the current minute + 15
    III) Round the square root to an integer
    VI) return the rounded number as the number of directories to be created
    
    args: 
          NONE
    
    returns: 
         `dir_count`: number of directories to be created 
    """
    #TODO

    now = datetime.datetime.now()
    minute = now.minute
    minute_fifteen = minute + 15
    minute_square = math.sqrt(minute_fifteen)
    dir_count = int(round(minute_square))

    print dir_count

    return dir_count 
    

def name_generator():
    """
    Generate a single directory name using the pattern (MM_DD_YY_randnum).
    
    args:
         NONE
    
    returns:
         `dir_name`: string containing a valid directory name
    """
    #TODO

    oggi = datetime.datetime.today()
    oggi_formattato = oggi.strftime("%m_%d_%Y")
    random_number = random.randint(10000,50000)
    dir_name = oggi_formattato + "_" + str(random_number)

    return dir_name


def directory_creator(name):
    """
    Create a single directory called `name` in the current working directory.
    
    args:
         name: directory to be created
    
    returns:
         NONE
    """
    #TODO

    os.mkdir(name)

def create():
    """
    Generate the necessary directories.
    
    Use `directory_count` to calculate the number of directories, then use `directory_creator` and `name_generator`.

    args:
         NONE
    
    returns:
         NONE
    """
    #TODO

    quante_directory = directory_count()

    for n in range(quante_directory):
    	nome_directory = name_generator()
    	directory_creator(nome_directory)
 



# make sure directory structure is in place
os.chdir("/Users/depo/Desktop/LEARNING")

if os.path.exists(os.getcwd() + "/parent_dir") != True:
    os.mkdir("parent_dir")
os.chdir("parent_dir")
    
    
if os.path.exists(os.getcwd() + "/randoms_directory") != True:
    os.mkdir("randoms_directory")
os.chdir("randoms_directory")
    
if os.path.exists(os.getcwd() + "/test_required") == True:
    # delete the test_required directory
    shutil.rmtree("/Users/depo/Desktop/LEARNING/parent_dir/randoms_directory/test_required")
# create and move to Test_required
os.mkdir("test_required")
os.chdir("test_required")

# print the current working directory (should be "parent_dir")
print("The current working directory is:", os.getcwd())
print("\nThe created directories should be named MM_DD_YY_randnum - such as '03_22_19_17040'")

# TEST*** test name_generator & directory_creator() by creating 3 directories ***TEST
for i in range(3):
    dir_name = name_generator()
    print("creating directory", dir_name)
    directory_creator(dir_name)


# list the content of the current directory
print("Current directory content:", os.listdir(os.getcwd()))

# Check if TEST created 3 directories
num_dir = len(os.listdir(os.getcwd()))

if num_dir == 3:
    print("\nPASS: Contains 3 directories as expected. Be sure name_generator() & directory_creator() contain required keywords and functions.")  
    print("Copy code cell above into edX required code submission.")
else:
    print("\nFAIL: Should contain 3 directories, contains", num_dir )
