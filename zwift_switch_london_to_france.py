import os, sys, shutil
from pathlib import Path
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR

# Set this variable to your Zwift directory if it doesn't work correctly,
# the script should detect your home folder automatically though.
# Use forward slashes '/' instead of backward slashes '\'
# Do not forget to put a trailing '/' at the end
zwift_directory = Path.home() / Path('Documents/Zwift')

if not os.path.exists(zwift_directory):
    sys.exit("Zwift directory not found, please assign the correct directory to the 'zwift_directory' variable above.")
    
mapschedule_file_prev = Path(zwift_directory) / Path('MapSchedule_prev.xml')
if not os.path.exists(mapschedule_file_prev):
    sys.exit(mapschedule_file_prev + " not found, please start Zwift and login first, then run this script again.")

def modify_file(filename):
  with open(filename, 'r') as file :
    filedata = file.read()

  # Replace LONDON with FRANCE
  filedata = filedata.replace('LONDON', 'FRANCE')

  # Make sure the file is writeable and write the changes to the file
  os.chmod(filename, S_IWUSR|S_IREAD)
  with open(filename, 'w') as file:
    file.write(filedata)

  # Set the file to read-only
  os.chmod(filename, S_IREAD|S_IRGRP|S_IROTH)

#mapschedule_file_backup = Path(zwift_directory) / Path('MapSchedule_prev.xml.BACKUP')
# Create a backup from the original 'MapSchedule_prev.xml' file
#if not os.path.exists(mapschedule_file_backup):
#  shutil.copy(mapschedule_file, mapschedule_file_backup)        

modify_file(mapschedule_file_prev)

mapschedule_file = Path(zwift_directory) / Path('MapSchedule.xml')
if not os.path.exists(mapschedule_file):
    # If the 'MapSchedule.xml' file doesn't exist, create it
    shutil.copy(mapschedule_file_prev, mapschedule_file)

mapschedule_file_v2 = Path(zwift_directory) / Path('MapSchedule_v2.xml')
if not os.path.exists(mapschedule_file_v2):
    # If the 'MapSchedule_v2.xml' file doesn't exist, create it
    shutil.copy(mapschedule_file_prev, mapschedule_file_v2)     
modify_file(mapschedule_file_v2)

sys.exit('DONE')