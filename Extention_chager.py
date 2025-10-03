import os

def change_extension(file_path, new_extension):
    # Remove leading dot if present
    if new_extension.startswith('.'):
        new_extension = new_extension[1:]
    base_name, _ = os.path.splitext(file_path)
    new_file_path = base_name + "." + new_extension
    try:
        os.rename(file_path, new_file_path)
        return True, f"File extension changed to .{new_extension}!"
    except Exception as e:
        return False, f"Error: {str(e)}"
