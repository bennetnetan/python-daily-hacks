import datetime
import os

root = os.path.join('..', 'food')
for directory, subdir_list, file_list in os.walk(root):
    for name in file_list:
        source_name = os.path.join(directory, name)
        timestamp = os.path.getmtime(source_name)
        modified_date = str(datetime.datetime.fromtimestamp(timestamp)).replace(':', '.')
        target_name = os.path.join(directory, f'{modified_date}_{name}')

        print(f'Renaming: {source_name} to: {target_name}')

        os.rename(source_name, target_name)

# Test your update-filenames.py script by running it
# python3 update-filenames.py

# and then running your list-directory-contents.py script again
# python3 list-directory-contents.py

# Use Python to print the new file system directory names with the last-modified timestamp prepended to it's own text file by entering this command directly in your PowerShell termina

# python3 list-directory-contents.py > food-directory-last-modified.txt