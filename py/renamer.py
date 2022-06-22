import os
from pathlib import Path


def filter_photos_in_directory(dir_string:'str')->'[str]':

    jpg_types = {'jpg', 'jpeg'}

    filtered = list()

    dir = os.listdir(dir_string)

    for d in dir:
        sp = d.split('.')
        
        if sp[-1].lower() in jpg_types:
            filtered.append('.'.join(sp))

    return filtered


def print_each(lst):
    for i, v in enumerate(lst):
        print('Item #{}: '.format(i+1) + v)


# institute-eventname_IMG#_photographer
# example: CHCMP-HCFC_001_BobPeterson
def rename(institute, event_name, photographer, root, filtered_photos):

    print('\nStarting to rename...')

    renamed_folder_path = os.path.join(root, 'Renamed')

    if not os.path.isdir(renamed_folder_path):
        os.makedirs(renamed_folder_path)

    for i, old_name in enumerate(filtered_photos):

        sequence = i+1
        
        new_name = '{}-{}_#{}_{}.JPG'.format(institute, event_name, sequence, photographer)

        print('Renaming Item #{}: {}'.format(sequence, old_name), 'to', new_name)
        
        os.rename(os.path.join(root, old_name), os.path.join(renamed_folder_path, new_name))
    

def run():
    
    root = os.path.join(Path.home(), 'Downloads')

    filtered_photos = filter_photos_in_directory(root)

    print('Photos Found In Directory {}:'.format(root))

    print_each(filtered_photos)

    rename('CIWM', 'LIFEvest', 'Shengyuan', root, filtered_photos)

    print()
    print('Batch Renaming Finished')