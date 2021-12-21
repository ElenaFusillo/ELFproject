def full_dest_txt(dest, name_file):
    '''TODO docstring'''
    full_destination_txt = dest + '/' + name_file + '.txt'
    return full_destination_txt

def write_file(full_destination_txt, optarg_output):
    '''TODO docstring
    Append Only (‘a’) : Open the file for writing.
    The file is created if it does not exist. The handle is positioned at the end of the file.
    The data being written will be inserted at the end, after the existing data.'''

    with open(full_destination_txt, "a") as output_file:
        output_file.write(str(optarg_output))
        output_file.write('\n')

def save_output_txt(dest, name_file, optarg_output):
    '''TODO docstring'''
    full_destination = full_dest_txt(dest, name_file)
    write_file(full_destination, optarg_output)


def full_dest_jpg(dest, name_file):
    full_destination_jpg = dest + '/' + name_file + '.jpg'
    return full_destination_jpg

def save_output_jpg(dest, name_file, output_figure):
    '''TODO docstring'''
    full_destination_jpg = full_dest_jpg(dest, name_file)
    output_figure.savefig(full_destination_jpg)

