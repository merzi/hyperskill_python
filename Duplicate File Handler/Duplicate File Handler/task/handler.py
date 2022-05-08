# write your code here
import hashlib
import os
import sys
from typing import Optional, Dict


def start(args: list) -> Optional[bool]:
    """
    start the program with some inquires
    :param args: command line arguments. first should be the observed folder
    :return: nothing. on error returns False
    """
    if len(args) < 2:
        print("Directory is not specified")
        return False

    print("Enter file format:")
    file_types = input()
    sorting = get_sorting()
    files = get_files(args[1], file_types)
    print_files_size(files, sorting)
    check_for_duplicates(files, sorting)


def get_files(root_path: str, file_types: str) -> Dict[int, list]:
    """
    determine the files in the given root folder. Search only files with the given files extension.
    :param root_path: root folder, which contains the files
    :param file_types: searched file types
    :return: Dictionary with files sizes and file names
    """
    files = {}
    for file in get_files_recursive(root_path, file_types):
        size = os.path.getsize(file)
        if size not in files:
            files.update({size: [file]})
        else:
            files[size].append(file)
    return files


def print_files_size(files: Dict[int, list], sorting: bool) -> None:
    """
    print the files from the given dictionary
    :param files: dictionary with file sizes and files
    :param sorting: boolean for the sorting. True -> Descending, False -> Ascending
    :return: nothing
    """
    for size, files_list in sorted(files.items(), reverse=sorting):
        print("\n{} bytes".format(size))
        for file in files_list:
            print(file)


def check_for_duplicates(files: dict, sorting: bool) -> None:
    possible_options = ["yes", "no"]
    option = None
    while option is None:
        print("\ncheck for duplicates?")
        option = input()
        if option not in possible_options:
            print("Wrong option")
            option = None

    file_number_buffer = 1
    if option == possible_options[0]:
        for size, file_list in sorted(files.items(), reverse=sorting):
            print("\n{} bytes".format(size))
            for file_hash, fl in calculating_hashes(file_list, file_number_buffer).items():
                print("Hash:", file_hash)
                for file_number, file in fl.items():
                    file_number_buffer = file_number
                    print("{}. {}".format(file_number, file))


def calculating_hashes(files_list: list, count: int) -> Dict[str, Dict[int, str]]:
    files = {}
#    count = 1
    for file in files_list:
        file_hash = md5_file_hash(file)
        if file_hash not in files.keys():
            files.update({file_hash: {count: file}})
        else:
            files[file_hash].update({count: file})
        count += 1

    return files


def md5_file_hash(file_path: str) -> str:
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_sorting() -> bool:
    print("\nSize sorting options:")
    print("1. Descending")
    print("2. Ascending\n")
    print("Enter sorting option:")
    sorting = None
    while sorting is None:
        sorting = int(input())
        if sorting not in [1, 2]:
            print("Wrong option")
            sorting = None
            continue

    return sorting == 1


def get_file_extension(file_path: str) -> str:
    filename, file_extension = os.path.splitext(file_path)
    return file_extension


def is_file_extension(file_path: str, extension: str) -> bool:
    return get_file_extension(file_path) == extension


def get_files_recursive(root_folder: str, file_type: str = "*") -> list:
    """
    get the files recursively in the given root folder
    :param root_folder:
    :param file_type:
    :return:
    """
    files_list = []
    for root, dirs, files in os.walk(root_folder, topdown=False):
        for name in files:
            if file_type in ["*", ""] or is_file_extension(os.path.join(root, name), file_type):
                files_list.append(os.path.join(root, name))

    return files_list


def print_files_recursive(root_folder: str) -> Optional[bool]:
    """
    print the files recursively in the given root folder
    :param root_folder: the root folder which should be observed
    :return: return nothing, except in error case return False
    """
    if len(root_folder.strip()) < 1:
        print("Directory is not specified")
        return False

    for file in get_files_recursive(root_folder):
        print(file)


start(sys.argv)
