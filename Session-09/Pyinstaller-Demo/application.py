import os
import sys


def my_read_file(filename):
    file_handle = open(filename)
    file_content = file_handle.readlines()
    return file_content


def main():
    filename = "dummy.txt"
    # Check if MEIPASS attribute is available in sys else return current file path
    bundle_dir = getattr(sys, '_MEIPASS',
                         os.path.abspath(os.path.dirname(__file__)))
    path_to_data = os.path.abspath(os.path.join(bundle_dir, filename))
    contents = my_read_file(path_to_data)
    for line in contents:
        print(f"{line}")


if __name__ == '__main__':
    main()
