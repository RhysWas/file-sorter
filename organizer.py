import shutil
import os
import re
import send2trash

# Extension types accepted, everything else falls in misc
images = ['png', 'jpg', 'jpeg', 'svg', 'heic', '3dm', 'ai', 'psd', '3dmbak']
audio = ['mp3', 'ogg']
docs = ['txt', 'html', 'pdf', 'docx', 'doc']
spreadsheets = ['csv', 'xlsx', 'xls']
presentations = ['pptx', 'ppt']
coding = ['h', 'cpp', 'json', 'gz', 'tar', 'sql']

# Change profile here
base_path = '/mnt/c/users/profile'

# Folder being sorted
input_folder = os.path.join(base_path, 'Downloads')

# Folders to sort files into
docs_folder = os.path.join(base_path, 'Documents')
pics_folder = os.path.join(base_path, 'Pictures')
music_folder = os.path.join(base_path, 'Music')
spreadsheet_folder = os.path.join(base_path, 'Documents/Spreadsheets')
presentation_folder = os.path.join(base_path, 'Documents/Presentations')
coding_folder = os.path.join(base_path, 'Documents/Coding')

# Duplicate Downloads have the pattern (1-9) in the name
# Check for pattern return true if it matches
def check_duplicates(str):
    pattern = r'\([1-9]\)'
    if re.search(pattern, str):
        return True
    else:
        return False
    
def move_to_recycle(path):
    # Put in the recycle bin to allow user to remove before deletion
    try:
        send2trash.send2trash(path)

    except OSError as e:
        print(f"Failed to recycle '{path}' to {e}")

def sort_files():
    """ Sorts files based on file type to prenamed folders"""
    files_to_sort = os.listdir(input_folder)
    for file in files_to_sort:
        src = os.path.join(input_folder, file)
        if check_duplicates(file):
            # If pattern matches move to the recycling bin to allow for more user control
            move_to_recycle(src)
        # elif to stop the sorting of files being deleted
        elif '.' in file:
            file_ending = file[file.rindex('.')+1:].lower()
            if file_ending in images:
                shutil.move(src, pics_folder)
            elif file_ending in audio:
                shutil.move(src, music_folder)
            elif file_ending in docs:
                shutil.move(src, docs_folder)
            elif file_ending in spreadsheets:
                shutil.move(src, spreadsheet_folder)
            elif file_ending in presentations:
                shutil.move(src, presentation_folder)
            elif file_ending in coding:
                shutil.move(src, coding_folder)
    # For now leave misc files in the downloads folder
    

sort_files()