import os
from pathlib import Path


def print_welcome_message():
    print("+-------------------------------------------------------------------------------+")
    print('Welcome to Merage Photo Renamer')
    print('A Tool To Batch Rename Photos According to UCI Merage Marketing Team\'s Standards')
    print('\n')
    print('Developed by Shengyuan Lu')
    print("+-------------------------------------------------------------------------------+\n")
    

def is_jpg(file_name: 'str')->bool:
    jpg_types = ('.jpg', '.jpeg')

    if file_name.lower().endswith(jpg_types):
        return True
    else:
        return False

    
def find_photos_in_directory(dir_string: 'str')->'[str]':

    dir = os.listdir(dir_string)

    return [file for file in dir if is_jpg(file)]


def get_new_name_format(institute, event_name, sequence, photographer):
    return '{}-{}_{}_{}.JPG'.format(institute, event_name, sequence, photographer)


def audit_each_photo(root, photos_to_be_renamed, institute, event_name, photographer):
    
    print('{} Photo(s) Found in {}:'.format(len(photos_to_be_renamed), root))

    photo_dict = dict()

    sequence = 0
    
    for index, old_name in enumerate(photos_to_be_renamed):

        if old_name not in photo_dict.keys():
            
            sequence += 1
            new_name = get_new_name_format(institute, event_name, sequence, photographer)

            while new_name in photo_dict.values():
                sequence += 1
                new_name = get_new_name_format(institute, event_name, sequence, photographer)

            photo_dict[old_name] = new_name
            
            print('Item #{}:'.format(index+1), old_name, 'will be renamed to', new_name)

    print('\n')

    return photo_dict


# format : institute-eventname_IMG#_photographer
# example: CHCMP-HCFC_001_BobPeterson


def rename(institute, event_name, photographer, root, photo_dict):

    user_confirm = str(input('Do You Want To Start Renaming (Y/N)? (Default: Y) : ') or 'Y')
    print(user_confirm, '\n')

    if user_confirm.upper() != 'Y':
        print('Batch Renaming Aborted')
        print('PROGRAM EXITED\n')
        return

    print('Batch Renaming Start...')

    # renamed_folder_path = os.path.join(root, 'Renamed Photos')

    # if not os.path.isdir(renamed_folder_path):
        # os.makedirs(renamed_folder_path)

    for index, (old_name, new_name) in enumerate(photo_dict.items()):

        old_name_path = os.path.join(root, old_name)
        new_name_path = os.path.join(root, new_name)

        if not os.path.exists(new_name_path):            
            os.rename(old_name_path, new_name_path)

            print('Renamed {} to {}'.format(old_name, new_name))

    print('Batch Renaming Finished')
    print('PROGRAM EXITED\n')


def ask_for_inp():
    
    institue = str(input('What\'s the name of the institute? (Default: CIWM) : ') or 'CIWM')
    print('Institute Name:', institue, '\n')
    
    event = str(input('What\'s the name of the event? (Default: LIFEvest) : ') or 'LIFEvest')
    print('Event Name:', event, '\n')
    
    photographer = str(input('What\'s the name of the photographer? (Default: Shengyuan) : ') or 'Shengyuan')
    print('Photographer Name:', photographer, '\n')
    
    return (institue, event, photographer)
    

def run():
    print_welcome_message()

    root = os.path.join(Path.home(), 'Downloads','rename')

    photos_to_be_renamed = sorted(find_photos_in_directory(root))

    if len(photos_to_be_renamed) == 0:
        print('No photos detected in the directory {}'.format(root))
        print('PROGRAM EXITED\n')
        
    else:
        institute, event_name, photographer = ask_for_inp()

        photo_dict = audit_each_photo(root, photos_to_be_renamed, institute, event_name, photographer)

        rename(institute, event_name, photographer, root, photo_dict)