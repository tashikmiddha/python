import os
import shutil


def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            ext = file.split('.')[-1].lower()
            ext_folder = os.path.join(directory, ext)

            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)

            shutil.move(file_path, os.path.join(ext_folder, file))

    print("Files organized successfully!")


if __name__ == "__main__":
    dir_path = input("Enter the directory path to organize: ")
    organize_files(dir_path)
