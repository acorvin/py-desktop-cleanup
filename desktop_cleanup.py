import os
import shutil

# Path to your desktop folder
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Create a new directory on the desktop called "Desktop Cleanup"
new_folder_name = "Desktop Cleanup"
new_folder_path = os.path.join(desktop_path, new_folder_name)
os.mkdir(new_folder_path)

# Define a dictionary that maps file extensions to folder names
file_extensions = {
    ".pdf": "PDFs",
    ".jpg": "Photos",
    ".png": "Photos",
    ".doc": "Word Documents",
    ".docx": "Word Documents",
    ".txt": "Text Files"
}

# Loop through all files on the desktop
for filename in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, filename)

    # Check if the file is a file (not a directory) and is not the script itself
    if os.path.isfile(file_path) and not filename.endswith(".py"):
        # Get the file extension (e.g. ".pdf")
        file_extension = os.path.splitext(filename)[1]

        # Check if the file extension is in the dictionary
        if file_extension in file_extensions:
            # Get the folder name from the dictionary
            folder_name = file_extensions[file_extension]

            # Create the folder if it doesn't already exist
            folder_path = os.path.join(new_folder_path, folder_name)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            # Move the file into the folder
            shutil.move(file_path, os.path.join(folder_path, filename))
