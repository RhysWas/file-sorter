import shutil
import os

# Extension types accepted, everything else falls in misc
images = ['png', 'jpg', 'jpeg']
audio = ['mp3', 'ogg']
docs = ['txt', 'html', 'pdf', 'docx']

# Folder being sorted
input_folder = 'input'

def sort_files():
    """ Sorts files based on file type to prenamed folders"""
    files_to_sort = os.listdir(input_folder)
    for file in files_to_sort:
        src = os.path.join(input_folder, file)
        file_ending = file.split('.')[1]
        if file_ending in images:
            shutil.move(src, 'images')
        elif file_ending in audio:
            shutil.move(src, 'audio')
        elif file_ending in docs:
            shutil.move(src, 'docs')
        else:
            shutil.move(src, 'misc')

sort_files()