import os
import shutil
import argparse

# Define the file types and their corresponding extensions
FILE_TYPES = {
    'PDFs': ['.pdf'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    'Music': ['.mp3', '.wav', '.flac', '.aac'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.csv'],
    'Archives': ['.zip', '.rar', '.tar.gz', '.7z'],
    'Executables': ['.exe', '.msi'],
    'Other': []
}

def organize_directory(directory):
    """
    Organizes files in a directory by moving them into subdirectories based on their file type.

    :param directory: The path to the directory to organize.
    """
    # Create directories for each file type if they don't exist
    for file_type in FILE_TYPES:
        folder_path = os.path.join(directory, file_type)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their respective folders
    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            # Skip directories
            continue

        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()
            moved = False
            for file_type, extensions in FILE_TYPES.items():
                if extension in extensions:
                    destination_folder = os.path.join(directory, file_type)
                    shutil.move(file_path, os.path.join(destination_folder, filename))
                    moved = True
                    break
            if not moved:
                destination_folder = os.path.join(directory, 'Other')
                shutil.move(file_path, os.path.join(destination_folder, filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files in a directory based on their extension.")
    parser.add_argument("directory", help="The directory to organize.")
    args = parser.parse_args()

    if os.path.isdir(.directory):
        organize_directory(args.directory)
        print("Files organized successfully!")
    else:
        print("Error: The specified directory does not exist.")