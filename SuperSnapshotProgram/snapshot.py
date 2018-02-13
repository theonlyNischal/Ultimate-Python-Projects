"""
This is the main module,
It will display menu to the user and make descision based on
what the user has selected.
"""
import os, pickle



def create_snapshot(directory, filename):
    cumulative_directories = []
    cumulative_files = []
    for root, dirs, files in os.walk(directory):
        cumulative_directories = cumulative_directories + dirs
        cumulative_files = cumulative_files + files
    print(cumulative_directories, cumulative_files)
    try:
        output = open(filename, 'wb')
        pickle.dump(cumulative_directories, output, -1)
        pickle.dump(cumulative_files, output, -1)
        output.close()
    except:
        print("Problems Encountered")
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
        print("No Snapshot Availaible.")




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
        print("Pressed 3")
    elif choice == '4':
        print('Pressed 4.')
    else:
        print("Pressed 5.")




