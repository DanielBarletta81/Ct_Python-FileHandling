
#Task 1: Directory Inspector:

# Your script should prompt the user for the directory path and then display the contents.

#Code Example:
 #   import os

   # def list_directory_contents(path):


        # List and print all files and subdirectories in the given path


#Expected Outcome: The script should correctly list all files and subdirectories in the specified directory.
#Handle exceptions for invalid paths or inaccessible directories.

import os

path = input("Enter the directory path. ")
  
def directory_contents(path):

    try:

        list_files = os.listdir(path)
        print(list_files)

# output: Enter the directory path. /Users/dbarletta_mb_pro/Desktop/Eastern Oyster

#['Restoration', 'Oysters in New England.pdf', 'Ermgassen_13_Filtration_Loss_Service.pdf', 
# 'Waldbrusser _11-Bicalcification_pH.pdf', 'Physicochemical', 'Rosa13_FeedingSelectivity_Oys_BM.pdf']



    except FileNotFoundError:
        print(FileNotFoundError)

    except PermissionError:
        print(PermissionError)

    except OSError as e:
        print(f'An OS Error occurred: {e}')

directory_contents(path)
