import os

def rename_directories(root_dir, prefix, start_number):
    """
    Rename directories within the root directory.

    Args:
    - root_dir (str): The path to the root directory.
    - prefix (str): The prefix to add to the directory names.
    - start_number (int): The starting number for renaming directories.
    """
    dirs = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]
    for i, old_name in enumerate(dirs, start=start_number):
        new_name = f"{prefix}-{i:03d}"
        old_path = os.path.join(root_dir, old_name)
        new_path = os.path.join(root_dir, new_name)
        try:
            os.rename(old_path, new_path)
            print(f"Directory '{old_name}' renamed to '{new_name}'")
        except FileExistsError:
            print(f"Directory '{new_name}' already exists.")

# Example usage
root_directory = input("Enter the path to the root directory: ")
prefix = input("Enter the prefix for the directory names: ")
start_number = int(input("Enter the starting number: "))

rename_directories(root_directory, prefix, start_number)
