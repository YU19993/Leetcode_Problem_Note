import os

def rename_files_in_directory(directory_path="."):
    """
    This function renames all .py files in the specified directory by replacing spaces with underscores.
    
    Args:
    - directory_path (str): The path to the directory containing the .py files. Defaults to the current directory.
    """
    
    # List all files in the given directory
    for filename in os.listdir(directory_path):
        
        # Check if the file has a .py extension
        if filename.endswith(".py"):
            
            # Replace spaces with underscores
            new_filename = filename.replace(" ", "_")
            
            # Rename the file if the new filename is different
            if new_filename != filename:
                os.rename(os.path.join(directory_path, filename),
                          os.path.join(directory_path, new_filename))
                print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    # If the script is being run as the main module, call the rename_files_in_directory function
    rename_files_in_directory()
