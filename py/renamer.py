import os
from pathlib import Path

def filter_photos_in_directory(dir_string:'str')->'[str]':

    dir = os.listdir(dir_string)

    return [file for file in dir if is_jpg(file)]


def is_jpg(file_name: 'str')->bool:
    jpg_types = ('.jpg', '.jpeg')

    if file_name.lower().endswith(jpg_types):
        return True
    else:
        return False


def print_each(lst):
    for i, v in enumerate(lst):
        print('Item #{}: '.format(i+1) + v)


# format : institute-eventname_IMG#_photographer
# example: CHCMP-HCFC_001_BobPeterson

def rename(institute, event_name, photographer, root, filtered_photos):

    print('Starting to rename photos...')

    renamed_folder_path = os.path.join(root, 'Renamed Photos')

    if not os.path.isdir(renamed_folder_path):
        os.makedirs(renamed_folder_path)

    for index, old_name in enumerate(filtered_photos):

        sequence = index + 1
        
        new_name = '{}-{}_{}_{}.JPG'.format(institute, event_name, sequence, photographer)

        new_name_path = os.path.join(renamed_folder_path, new_name)

        if not os.path.exists(new_name_path):
            print('Renaming Item #{}: {}'.format(sequence, old_name), 'to', new_name)
            
            os.rename(os.path.join(root, old_name), new_name_path)

    print('\nBatch Renaming Finished')
    print('PROGRAM EXITED')


def print_welcome_message():
    print("---------------------------------------------------------------------------------")
    print('Welcome to Renamer by Shengyuan Lu')
    print('A Tool To Batch Rename Photos According to UCI Merage Marketing Team\'s Standards')
    print("---------------------------------------------------------------------------------\n")


def ask_for_inp():

    print()
    
    institue = str(input('What\'s the name of the institute? (Default: CIWM) : ') or 'CIWM')
    print('Institute Name:', institue, '\n')
    
    event = str(input('What\'s the name of the event? (Default: LIFEvest) : ') or 'LIFEvest')
    print('Event Name:', event, '\n')
    
    photographer = str(input('What\'s the name of the photographer? (Default: Shengyuan) : ') or 'Shengyuan')
    print('Photographer Name:', photographer, '\n')
    
    return (institue, event, photographer)
    

def run():
    print_welcome_message()

    root = os.path.join(Path.home(), 'Downloads')

    filtered_photos = filter_photos_in_directory(root)

    if len(filtered_photos) == 0:
        print('No photos detected in the directory {}'.format(root))
        print('PROGRAM EXITED')
        return

    print('Photos Found In Directory {}:'.format(root))

    print_each(filtered_photos)

    institute, event, photographer = ask_for_inp()

    rename(institute, event, photographer, root, filtered_photos)