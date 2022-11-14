import os
import sys
import platform
import subprocess

# No extra arguments are good
if len(sys.argv) == 1:
    copy_to_clipboard=False
    file_name = ""
# Checking if there is one extra argument
elif len(sys.argv) == 2:
    if sys.argv[1] == "-c":
        copy_to_clipboard=True
        file_name = ""
    elif os.path.exists(sys.argv[1]):
        file_name = sys.argv[1]
        copy_to_clipboard=False
    else:
        copy_to_clipboard=False
        file_name = ""
# Checking if there are two extra arguments
elif len(sys.argv) == 3:
    # Checking if the non-file value is set correctly
    if sys.argv[1] == "-c" or sys.argv[2] == "-c":
        copy_to_clipboard=True
    else:
        print("Usage: cwd [-c] [file_name]")
        exit(1)
    # Checking if the file exists before
    if os.path.exists(sys.argv[1]):
        file_name = sys.argv[1]
    elif os.path.exists(sys.argv[2]):
        file_name = sys.argv[2]
    else:
        print("Usage: cwd [-c] [file_name]")
        exit(1)
# More than two extra are bad
else:
    print("Usage: cwd [-c] [file_name]")
    exit(1)

# If file_name is setup then get abspath otherwise get cwd
if len(file_name) >= 1:
    full_path = os.path.abspath(file_name)
else:
    full_path = os.getcwd()

# If clipboard is setup add it to clipboard on Windows or Mac
if copy_to_clipboard == True:
    whatos = platform.system()
    if whatos == "Darwin":
        subprocess.run("pbcopy", universal_newlines=True, input=full_path)
        output = full_path + " (copied to clipboard)"
    elif whatos == "Windows":
        subprocess.run("clip", universal_newlines=True, input=full_path)
        output = full_path + " (copied to clipboard)"
    else:
        output = full_path + " (clipboard not supported)"
else:
    output = full_path

# Displaying output
print(output)

# >user@macbook ~ % cwd.py -c cwd.bat
#   /Users/Demo/python-scripts/cwd.bat (copied to clipboard

#Getting the present working directory is easy on Linux and Mac because it’s built into the shell as the pwd command. But pwd is a POSIX environmental variable, which means it won’t work on Windows. As a result, we can use the command called cwd so it will not interfere if you choose to use it on either Mac or Linux, but is primarily aimed at Windows.
#
#Running cwd on its own will display the current working directory. If you pass the -c flag it automatically copies the current working directory to the clipboard on Mac or Windows, which saves a lot of retyping and mouse movements.
#
#In addition, you can pass a filename as an argument and have its full path copied to the clipboard, which is something I need to do often when running test cases.