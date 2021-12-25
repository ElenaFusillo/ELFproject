from .calculations import main_print # main_print_point, main_print_bidim, main_print_dpa


def full_dest_txt(dest, name_file):
    '''TODO docstring'''
    full_destination_txt = dest + '/' + name_file + '.txt'
    return full_destination_txt


def write_file(full_destination_txt, current_s, xp, yp, diam_cables, cables_array, subparser_type, dpa_value, dictionary):
    '''TODO docstring'''
    with open(full_destination_txt, "a", encoding="utf-8") as output_file:
        main_print(current_s, xp, yp, diam_cables, cables_array, subparser_type, dpa_value, dictionary, output_file)

def save_output_txt(dest, name_file, current_s, xp, yp, diam_cables, cables_array, subparser_type, dpa_value, dictionary):
    '''TODO docstring'''
    full_destination = full_dest_txt(dest, name_file)
    write_file(full_destination, current_s, xp, yp, diam_cables, cables_array, subparser_type, dpa_value, dictionary)


# def write_file_point(full_destination_txt, current_s, xp, yp, diam_cables, cables_array, subparser_type):
#     '''TODO docstring'''
#     with open(full_destination_txt, "a", encoding="utf-8") as output_file:
#         main_print_point(current_s, xp, yp, diam_cables, cables_array, subparser_type, file=output_file)

# def save_output_point_txt(dest, name_file, current_s, xp, yp, diam_cables, cables_array, subparser_type):
#     '''TODO docstring'''
#     full_destination = full_dest_txt(dest, name_file)
#     write_file_point(full_destination, current_s, xp, yp, diam_cables, cables_array, subparser_type)


# def write_file_bidim(full_destination_txt, current_s, xp, yp, diam_cables, cables_array, subparser_type):
#     with open(full_destination_txt, "a", encoding="utf-8") as output_file:
#         main_print_bidim(current_s, xp, yp, diam_cables, cables_array, subparser_type, file=output_file)

# def save_output_bidim_txt(dest, name_file, current_s, xp, yp, diam_cables, cables_array, subparser_type):
#     '''TODO docstring'''
#     full_destination = full_dest_txt(dest, name_file)
#     write_file_bidim(full_destination, current_s, xp, yp, diam_cables, cables_array, subparser_type)


# def write_file_dpa(full_destination_txt, current_s, diam_cables, cables_array, subparser_type, dpa_value):
#     with open(full_destination_txt, "a", encoding="utf-8") as output_file:
#         main_print_dpa(current_s, diam_cables, cables_array, subparser_type, dpa_value, file=output_file)

# def save_output_dpa_txt(dest, name_file, current_s, diam_cables, cables_array, subparser_type, dpa_value):
#     '''TODO docstring'''
#     full_destination = full_dest_txt(dest, name_file)
#     write_file_dpa(full_destination, current_s, diam_cables, cables_array, subparser_type, dpa_value)


def full_dest_jpg(dest, name_file):
    full_destination_jpg = dest + '/' + name_file + '.jpg'
    return full_destination_jpg

def save_output_jpg(dest, name_file, output_figure):
    '''TODO docstring'''
    full_destination_jpg = full_dest_jpg(dest, name_file)
    output_figure.savefig(full_destination_jpg)
