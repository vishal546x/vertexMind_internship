import os
import shutil

# Configuration: Mapping extensions to destination folders
DIRECTORY_MAP = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Video": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh"]
}

def organize_folder(target_dir):
    if not os.path.exists(target_dir):
        print(f"Error: The directory '{target_dir}' does not exist.")
        return

    print(f"Scanning: {target_dir}...\n")
    files_moved = 0

    # Iterate through all files in the target directory
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)

        # Skip directories, only process files
        if os.path.isdir(item_path):
            continue

        # Get file extension in lowercase
        _, extension = os.path.splitext(item).lower()

        # Find the correct category folder
        moved = False
        for folder_name, extensions in DIRECTORY_MAP.items():
            if extension in extensions:
                dest_folder = os.path.join(target_dir, folder_name)
                
                # Create the destination folder if it doesn't exist
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                
                # Move the file gracefully
                shutil.move(item_path, os.path.join(dest_folder, item))
                print(f"Moved: {item} -> {folder_name}/")
                files_moved += 1
                moved = True
                break
        
        # Optional: Handle miscellaneous/unknown files
        if not moved and extension != "":
            misc_folder = os.path.join(target_dir, "Others")
            if not os.path.exists(misc_folder):
                os.makedirs(misc_folder)
            shutil.move(item_path, os.path.join(misc_folder, item))
            print(f"Moved: {item} -> Others/")
            files_moved += 1

    print(f"\n✨ Organization complete! Total files moved: {files_moved}")

def main():
    print("=== Automated File Organizer ===")
    path_to_sort = input("Enter the absolute path of the folder to organize: ").strip()
    
    # Simple verification step
    confirm = input(f"Are you sure you want to organize '{path_to_sort}'? (y/n): ").lower()
    if confirm == 'y':
        organize_folder(path_to_sort)
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()