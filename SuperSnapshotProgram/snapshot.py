"""
This is the main module,
It will display menu to the user and make descision based on
what the user has selected.
"""
import os, pickle, difflib



def create_snapshot(directory, filename):
    cumulative_directories = []
    cumulative_files = []
    for root, dirs, files in os.walk(directory):
        cumulative_directories = cumulative_directories + dirs
        cumulative_files = cumulative_files + files
    try:
        output = open(filename, 'wb')
        pickle.dump(cumulative_directories, output, -1)
        pickle.dump(cumulative_files, output, -1)
        output.close()
        print("Snapshot Created.\n")
    except:
        print("Problems Encountered.\n")
        input("Press Enter To Continue...")
        return
    input("Press Enter To Continue...")
    return

def snapshot_list(extension):
    snaplist = []
    allfiles = os.listdir(os.curdir)

    for file in allfiles:
        if file.find(extension) != -1:
            snaplist.append(file)

    print("""
                SNAPSHOT List
                =============

                """)

    if len(snaplist) > 0:

        for file in snaplist:
            print(file)
    else:
        print("No Snapshot Availaible.\n")

    input("Press Enter To Continue...")

def compare_snapshot(snapfile1, snapfile2):

    try:

        pkl_file1 = open(snapfile1, 'rb')
        dirs_1 = pickle.load(pkl_file1)
        files_1 = pickle.load(pkl_file1)
        pkl_file1.close()

        pkl_file2 = open(snapfile2, 'rb')
        dirs_2 = pickle.load(pkl_file2)
        files_2 = pickle.load(pkl_file2)
        pkl_file2.close()
    except:
        print("Problems Encountered")
        input("Press Enter To Continue....")
        return


  

    result_dirs = list(difflib.unified_diff(dirs_1, dirs_2))
    result_files = list(difflib.unified_diff(files_1, files_2))


    added_dirs = []
    added_files = []
    removed_dirs = []
    removed_files = []

    for result in result_files:
        if result.find("\n") == -1:
            if result.startswith("+"):
                resultadd = result.strip('+')
                added_files.append(resultadd)
            elif result.startswith('-'):
                resultsubtract = result.strip('-')
                removed_files.append(resultsubtract)

    for result in result_dirs:
        if result.find("\n") == -1:
            if result.startswith("+"):
                resultadd = result.strip('+')
                added_dirs.append(resultadd)
            elif result.startswith('-'):
                resultsubtract = result.strip('-')
                removed_dirs.append(resultsubtract)





    print("\n\nAdded Directories:\n")
    print(added_dirs)
    print ("\n\nAdded Files:\n")
    print(added_files)
    print ("\n\nRemoved Directories:\n")
    print(removed_dirs)
    print ("\n\nRemoved Files:\n")
    print(removed_files)
    input("Enter to continue..")


def show_help():
    clear_screen()
    print("""


            DIRECTORY/FILE COMPARISON TOOL
            ==============================

            Welcome to the DIRECTORY/FILE COMPARISON TOOL help.
            This tool allows you to create snapshot of a directory/file tree,
            list the snapshots you created in the current directory, and compare
            any two snapshots.



            You can select any 5 options from menu by pressing the number: 

            1. Create a snapshot
            2. List snapshot files
            3. Comapre Snapshots
            4. Help
            5. Exit



            1. Create a snapshot
                This will create a snapshot of the directory/file tree.
                Enter the name of directory to create snapshot of and enter
                the name of snapshot file to store snapshot according to input
                of the string.

                E.G: To create snapshot of folder name 'TestFolder'
                 located on my desktop and 
                 save the snapshot in a file name 'snapshot1.snp'

                Enter the directory name to creat snapshot of: 
                ---> /home/nischal/Desktop/TestFolder/
                Enter a file name to save the snapshot: 
                ---> snapshot1.snp

                You can use whatever extenion you like instead of '.snp'.



            2. List snapshot files
                This will list all the snapshots you created in current
                directory. It will ask for the extension to list.

                Enter the file extension of your snapshot files: 
                ---> snp

                It will list all the snapshot with '.snp' extensions.




            3. Comapre Snapshots
                This will compare any two snapshots and list out the changes
                occured after you take snapshot.

                Example Use:
                First Take a snapshot using Menu 1 and save it in a file called
                snapshot1.snp,  Delete/Create folder/files. Then, take another
                snapshot using Menu 1 and save it as snapshot2.snp

                Now go to Menu 3:
                It will ask for the snapshots name. Enter the name and see the 
                change.
                
                Enter name of first snapshot file:
                ---> snapshot1.snp
                Enter name of first snapshot file:
                ---> snapshot2.snp

                It will show:
                Added Directories:

                ['the', 'names', 'of', 'directory', 'added']


                Added Files:

                ['the', 'names', 'of', 'files', 'added']


                Removed Directories:

                []

                # Empty, if no change occured.


                Removed Files:

                ['the', 'names', 'of', 'files', 'removed']

            4. Help
                This will display this help menu

            5. Exit
                End the program.

        """)

    input("Press Enter To Continue...")






def clear_screen():
    os.system('clear')


def menu():
    clear_screen()
    print("""

        DIRECTORY/FILE COMPARISON TOOL
        ==============================

        
        1. Create a snapshot
        2. List snapshot files
        3. Comapre Snapshots
        4. Help
        5. Exit

        Please type a number and press enter:

        """)

    choice = input()
    return choice

choice = ""

while choice != '5':
    

    choice = menu()

    if choice == '1':
        clear_screen()
        print("CREATE SNAPSHOT\n================")
        directory = input("Enter the directory name to creat snapshot of: ")
        filename = input("Enter a file name to save the snapshot: ")
        create_snapshot(directory, filename)

    elif choice == '2':
        clear_screen()
        extension = input("Enter the file extension of your snapshot files: ")
        snapshot_list(extension)

    elif choice == '3':
        clear_screen()
        print("""
            Compare SNAPSHOT
            ================
            """)

        snapfile1 = input("Enter name of first snapshot file: ")
        snapfile2 = input("Enter name of second snapshot file: ")
        compare_snapshot(snapfile1, snapfile2)

    elif choice == '4':
        show_help()
    else:
        print("Bye Bye...")