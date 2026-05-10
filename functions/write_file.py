import os

def write_file(working_directory, file_path, content):
    try:
        #Absolute path of the working directory
        working_dir_abs = os.path.abspath(working_directory)

        #Full path to the target file
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        #Check whether the file_path falls within the absolute working_directory
        valid_target_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        if valid_target_path == False:
            return f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory"
        if os.path.isdir(target_path):
            return f"Error: Cannot write to '{file_path}' as it is a directory"
        
        #making sure all parent directories of the file_path exist (otherwise, does nothing)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        with open(target_path, "w") as file:
            file.write(content)
        
        return f"Successfully wrote to '{file_path}' ({len(content)} characters written)"

    except Exception as e:
        return f"Error: {e}"
