import os
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_folders(root_dir, prefix, start_number):
    """
    Rename folders within the root directory.

    Args:
    - root_dir (str): The path to the root directory.
    - prefix (str): The prefix to add to the directory names.
    - start_number (int): The starting number for renaming directories.
    """
    for i, folder_name in enumerate(os.listdir(root_dir), start=start_number):
        new_folder_name = f"{prefix}-{i:03d}"
        try:
            os.rename(os.path.join(root_dir, folder_name), os.path.join(root_dir, new_folder_name))
            print(f"Folder '{folder_name}' renamed to '{new_folder_name}'")
        except FileExistsError:
            print(f"Folder '{new_folder_name}' already exists.")

def rename_files_to_directory_name(root_dir):
    """
    Rename files within each directory to match the directory name.

    Args:
    - root_dir (str): The path to the root directory.
    """
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_name, file_extension = os.path.splitext(filename)
            counter = 0
            new_file_name = os.path.join(dirpath, f"{os.path.basename(dirpath)}-{counter}{file_extension}")
            while os.path.exists(new_file_name):
                counter += 1
                new_file_name = os.path.join(dirpath, f"{os.path.basename(dirpath)}-{counter}{file_extension}")
            try:
                os.rename(os.path.join(dirpath, filename), new_file_name)
                print(f"File '{filename}' renamed to '{os.path.basename(new_file_name)}'")
            except FileExistsError:
                print(f"File '{new_file_name}' already exists.")

def replace_specific_file_names(root_dir, search_name, replace_name):
    """
    Replace specific file names within each directory.

    Args:
    - root_dir (str): The path to the root directory.
    - search_name (str): The name to search for in file names.
    - replace_name (str): The replacement name for files with search_name.
    """
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if search_name in filename:
                new_filename = filename.replace(search_name, replace_name)
                try:
                    os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, new_filename))
                    print(f"File '{filename}' renamed to '{new_filename}'")
                except FileExistsError:
                    print(f"File '{new_filename}' already exists.")

def browse_folder():
    folder_path = filedialog.askdirectory()
    entry_folder_path.delete(0, tk.END)
    entry_folder_path.insert(0, folder_path)

def execute_rename_folders():
    root_directory = entry_folder_path.get()
    prefix = entry_prefix.get()
    start_number = entry_start_number.get()

    if not os.path.isdir(root_directory):
        messagebox.showerror("Error", "Invalid directory path.")
        return
    try:
        start_number = int(start_number)
    except ValueError:
        messagebox.showerror("Error", "Invalid starting number.")
        return
    rename_folders(root_directory, prefix, start_number)
    messagebox.showinfo("Success", "Folders renamed successfully.")

def execute_rename_files():
    root_directory = entry_folder_path.get()

    if not os.path.isdir(root_directory):
        messagebox.showerror("Error", "Invalid directory path.")
        return
    rename_files_to_directory_name(root_directory)
    messagebox.showinfo("Success", "Files renamed successfully.")

def execute_replace_names():
    root_directory = entry_folder_path.get()
    search_name = entry_search_name.get()
    replace_name = entry_replace_name.get()

    if not os.path.isdir(root_directory):
        messagebox.showerror("Error", "Invalid directory path.")
        return
    replace_specific_file_names(root_directory, search_name, replace_name)
    messagebox.showinfo("Success", "Specific file names replaced successfully.")

# Create GUI window
window = tk.Tk()
window.title("Directory and File Renamer")

# Add title and copyright notice
title_label = tk.Label(window, text="Made by Yaniv Logi", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=3, pady=10, sticky="we")
copyright_label = tk.Label(window, text="\u00a9 2024 Yaniv Logi. All rights reserved.", font=("Helvetica", 10))
copyright_label.grid(row=1, column=0, columnspan=3, pady=(0, 10), sticky="we")

# Add section for renaming folders
label_section_folders = tk.Label(window, text="Rename Folders")
label_section_folders.grid(row=2, column=0, columnspan=3, pady=5, sticky="we")

# Add folder path entry
label_folder_path = tk.Label(window, text="Root Directory:")
label_folder_path.grid(row=3, column=0, padx=10, sticky="w")
entry_folder_path = tk.Entry(window, width=40)
entry_folder_path.grid(row=3, column=1, padx=10, pady=5, sticky="we")
button_browse = tk.Button(window, text="Browse", command=browse_folder)
button_browse.grid(row=3, column=2, padx=10, pady=5)

# Add prefix entry
label_prefix = tk.Label(window, text="Prefix:")
label_prefix.grid(row=4, column=0, padx=10, sticky="w")
entry_prefix = tk.Entry(window)
entry_prefix.grid(row=4, column=1, padx=10, pady=5, sticky="we")

# Add starting number entry
label_start_number = tk.Label(window, text="Starting Number:")
label_start_number.grid(row=5, column=0, padx=10, sticky="w")
entry_start_number = tk.Entry(window)
entry_start_number.grid(row=5, column=1, padx=10, pady=5, sticky="we")

# Add execute button for renaming folders
button_execute_folders = tk.Button(window, text="Execute", command=execute_rename_folders)
button_execute_folders.grid(row=6, column=0, columnspan=3, pady=5, sticky="we")

# Add section for renaming files
label_section_files = tk.Label(window, text="Rename Files To Folder Name")
label_section_files.grid(row=7, column=0, columnspan=3, pady=5, sticky="we")

# Add execute button for renaming files
button_execute_files = tk.Button(window, text="Execute", command=execute_rename_files)
button_execute_files.grid(row=8, column=0, columnspan=3, pady=5, sticky="we")

# Add section for replacing specific file names
label_section_replace = tk.Label(window, text="Replacing part of the file's name with another name")
label_section_replace.grid(row=9, column=0, columnspan=3, pady=5, sticky="we")

# Add search name entry
label_search_name = tk.Label(window, text="Search Name:")
label_search_name.grid(row=10, column=0, padx=10, sticky="w")
entry_search_name = tk.Entry(window)
entry_search_name.grid(row=10, column=1, padx=10, pady=5, sticky="we")

# Add replace name entry
label_replace_name = tk.Label(window, text="Replace Name:")
label_replace_name.grid(row=11, column=0, padx=10, sticky="w")
entry_replace_name = tk.Entry(window)
entry_replace_name.grid(row=11, column=1, padx=10, pady=5, sticky="we")

# Add execute button for replacing specific file names
button_execute_replace = tk.Button(window, text="Execute", command=execute_replace_names)
button_execute_replace.grid(row=12, column=0, columnspan=3, pady=5, sticky="we")

window.mainloop()
