import os
import shutil

DIRECTORY_MAP = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Video": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh"]
}

def determine_destination_folder(file_extension):
    """
    Maps a specific file extension to its corresponding category folder.

    Parameters:
    file_extension (str): The lowercase file extension string including the leading dot.

    Returns:
    str: The target category folder name, or 'Others' if the extension is unrecognized.
    """
    for folder_name, extensions in DIRECTORY_MAP.items():
        if file_extension in extensions:
            return folder_name
    return "Others"

def organize_folder(target_directory):
    """
    Scans a targeted directory path and segregates files into structured folders.

    Parameters:
    target_directory (str): The absolute file path of the directory to be organized.

    Returns:
    int: The total count of files successfully transferred during execution.
    """
    if not os.path.exists(target_directory):
        return 0

    files_moved_count = 0

    for item_name in os.listdir(target_directory):
        item_path = os.path.join(target_directory, item_name)

        if os.path.isdir(item_path):
            continue

        _, file_extension = os.path.splitext(item_name).lower()
        if file_extension == "":
            continue

        destination_category = determine_destination_folder(file_extension)
        destination_folder_path = os.path.join(target_directory, destination_category)
        
        if not os.path.exists(destination_folder_path):
            os.makedirs(destination_folder_path)
        
        shutil.move(item_path, os.path.join(destination_folder_path, item_name))
        files_moved_count += 1

    return files_moved_count

def main():
    """
    Provides the command-line interface logic for collecting directory paths 
    and executing the organizing routines safely.
    """
    print("=== Automated File Organizer ===")
    path_to_sort = input("Enter the absolute path of the folder to organize: ").strip()
    
    confirm = input(f"Are you sure you want to organize '{path_to_sort}'? (y/n): ").lower()
    if confirm == 'y':
        total_moved = organize_folder(path_to_sort)
        print(f"Organization complete. Total files moved: {total_moved}")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()