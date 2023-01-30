import os

root = os.path.join('..', 'food')
for directory, subdir_list, file_list in os.walk(root):
    print('Directory:', directory)
    for name in subdir_list:
        print('Subdirectory:', name)
    for name in file_list:
        print('File:', name)
    print()

# Use Python to print that file system directory output to it's own text file by entering this command directly in your PowerShell terminal
# python3 list-directory-contents.py > food-directory.txt