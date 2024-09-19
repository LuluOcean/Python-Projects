#!/usr/bin/python3
import os
import sys
from datetime import datetime
import stat as stat_module

# This script prints out basic stats about file.
# To run the file, specify the file path, if in different directory, or name of the file as an argument

# Specify the file path
file_path = sys.argv[1]

# Get file stats
file_stat = os.stat(file_path)

# File size in bytes
file_size = file_stat.st_size

# File creation time (epoch time in seconds)
creation_time = file_stat.st_ctime
creation_date = datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M:%S")

# Last modification time
modification_time = file_stat.st_mtime
modification_date = datetime.fromtimestamp(modification_time).strftime("%Y-%m-%d %H:%M:%S")

# Last access time
access_time = file_stat.st_atime
access_date = datetime.fromtimestamp(access_time).strftime("%Y-%m-%d %H:%M:%S")

# File permissions
permissions = stat_module.filemode(file_stat.st_mode)

# Check if the file is a directory, symbolic link, or regular file
is_directory = stat_module.S_ISDIR(file_stat.st_mode)
is_symlink = stat_module.S_ISLNK(file_stat.st_mode)
is_regular_file = stat_module.S_ISREG(file_stat.st_mode)

# Output file information
print(f"File: {file_path}")
print(f"Size: {file_size} bytes")
print(f"Creation Date: {creation_date}")
print(f"Last Modification Date: {modification_date}")
print(f"Last Access Date: {access_date}")
print(f"Permissions: {permissions}")

# File type
if is_directory:
    print("Type: Directory")
elif is_symlink:
    print("Type: Symbolic Link")
elif is_regular_file:
    print("Type: Regular File")
else:
    print("Type: Other")

