*********************
SuperSnapshot Program
*********************


This is simple introduction to SuperSnapshot Program which I created
following tutorials from the book. 






       
DIRECTORY/FILE COMPARISON TOOL
-------------------------------

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