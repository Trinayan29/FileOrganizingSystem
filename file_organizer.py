import os
import shutil
import platform


# ---- OS Validation ----
os_name = platform.system()

if os_name == "Windows":
    print("Operating System Detected: Windows")
elif os_name == "Darwin":
    print("Operating System Detected: macOS")
elif os_name == "Linux":
    # Android runs on Linux kernel
    if "ANDROID_ROOT" in os.environ:
        print("Operating System Detected: Android")
    else:
        print("Operating System Detected: Linux (Desktop)")
else:
    print("Operating System Detected: Unknown")


path = input("Enter the path of the directory to organize: ")

try:
    
    list_of_files = os.listdir(path)

    
    for file in list_of_files:
       
        name, ext = os.path.splitext(file)

        
        ext = ext[1:]

        
        if ext == '':
            continue

       
        folder_path = os.path.join(path, ext)
        file_path = os.path.join(path, file)

        
        if os.path.exists(folder_path):
            
            shutil.move(file_path, os.path.join(folder_path, file))
        else:
            
            os.makedirs(folder_path)
            
            shutil.move(file_path, os.path.join(folder_path, file))
    
    print("Folder successfully organized!")

except FileNotFoundError:
    print("Error: The specified path does not exist. Please check the path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")
