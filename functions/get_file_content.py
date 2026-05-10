import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        #Absolute path of the working directory
        working_dir_abs = os.path.abspath(working_directory)

        #Full path to the target file
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        #Check whether the file_path falls within the absolute working_directory
        valid_target_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        if valid_target_path == False:
            return f"Error: Cannot read '{file_path}' as it is outside the permitted working directory"
        if not os.path.isfile(target_path):
            return f"Error: File not found or is not a regular file: '{file_path}'"
        
        #Opening the file for reading
        with open(target_path, "r") as file:
            contents = file.read(MAX_CHARS)
            if file.read(1):
                    contents += f"[...File '{file_path}' truncated at {MAX_CHARS} characters]"
            return contents
            
    except Exception as e:
        return f"Error: {e}"

       
        

