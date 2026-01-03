import shutil
from pathlib import Path

def organize_folder(target_dir):
    # Define categories and their associated extensions
    FILE_TYPES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Audio": [".mp3", ".wav", ".flac", ".aac"],
        "Archives": [".zip", ".tar", ".rar", ".7z", ".gz"],
    }

    # Convert string path to a Path object
    base_path = Path(target_dir)

    # 1. Error Handling: Check if folder exists
    if not base_path.exists() or not base_path.is_dir():
        print(f"Error: The directory '{target_dir}' does not exist.")
        return

    print(f"Organizing files in: {base_path.absolute()}...")

    # 2. Iterate through files in the directory
    for item in base_path.iterdir():
        # Skip directories (we only want to move files)
        if item.is_dir():
            continue

        # Get the file extension (lowercase to ensure matches)
        file_ext = item.suffix.lower()
        
        # 3. Determine the destination folder
        dest_folder_name = "Others"
        for category, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                dest_folder_name = category
                break

        dest_folder_path = base_path / dest_folder_name

        try:
            # 4. Create the subfolder if it doesn't exist
            dest_folder_path.mkdir(exist_ok=True)

            # 5. Handle duplicate file names
            destination_file = dest_folder_path / item.name
            if destination_file.exists():
                # Append a suffix if file already exists in destination
                new_name = f"{item.stem}_copy{item.suffix}"
                destination_file = dest_folder_path / new_name

            # 6. Move the file
            shutil.move(str(item), str(destination_file))
            print(f"Moved: {item.name} -> {dest_folder_name}/")

        except PermissionError:
            print(f"Permission Denied: Could not move {item.name}")
        except Exception as e:
            print(f"An error occurred with {item.name}: {e}")

if __name__ == "__main__":
    # Replace 'test_folder' with your specific path
    # Use r'C:\Path\To\Folder' on Windows
    target = input("Enter the path of the folder to organize: ").strip()
    organize_folder(target)
    print("Organization complete!")