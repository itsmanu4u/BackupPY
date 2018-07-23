import os
import time

# 1. The files and directories to be backed up are:
# specified in a list.
# Example in Winodws: 
# source = ['"C:\\My Documents'"]
# Example of Mac OS X and  Linux:
source = ['/root/Desktop/MyDailyWork'] 

# Note: for names with space in it. We have to use double quote or raw string can also be used.
# i.e ['"C:\\My Documents'"]    <== Double quotes inside a string.
# i.e [r'C:\\My Documents']     <== Raw string as: r


# 2. The backup must be stored in a main backup directory.
# Example in Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = '/root/Documents/' # We set the backup destination to Document folder.
# remember to change this folder to your preffered.

# 3. The files are backed up into a ZIP file.
# 4. The name of the ZIP archive is the current date a time
target = target_dir + os.sep + \
        time.strftime('%y%m%d%H%M%S') + '.zip'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)    # make directory

# 5. We use the ZIP command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target,''.join(source))

# 6. Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Sucessful backup to', target)
else:
    print('Backup FAILED')

