import os

def rename_files_in_folder(folder_path, start_number=100):
    # Get all files in the directory
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files.sort()  # Optional: Sort files alphabetically

    for i, filename in enumerate(files):
        # Extract the file extension
        _, ext = os.path.splitext(filename)
        # Create new filename
        new_name = f"{start_number + i}{ext}"
        # Construct full file paths
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        # Rename the file
        os.rename(src, dst)
        print(f"Renamed: {filename} -> {new_name}")

# Example usage
folder_path = "../data/bundles/230425/"  # Replace with your folder path
rename_files_in_folder(folder_path)
