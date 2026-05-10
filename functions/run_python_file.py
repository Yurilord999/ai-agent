import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        #Absolute path of the working directory
        working_dir_abs = os.path.abspath(working_directory)

        #Full path to the target file
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        #Check whether the file_path falls within the absolute working_directory
        valid_target_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        if valid_target_path == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        #Make sure file_path exists and points to a regular file
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        #Make sure it's a python file
        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_path]
        if args != None:
            command.extend(args)
        
        execution = subprocess.run(command, cwd=working_directory, capture_output=True, text=True, timeout=30)
        output = ""
        if execution.returncode != 0:
            output += f"Process exited with code {execution.returncode}\n"
        if execution.stdout == "" and execution.stderr == "":
            output += "No output produced\n"
        else:
            output += f"STDOUT: {execution.stdout}\n"
            output += f"STDERR: {execution.stderr}\n"

        return output
        
    except Exception as e:
        return f"Error: executing python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs python file in a specified directory relative to the working directory, providing arguments",
    parameters=types.Schema(
        required=["file_path"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to execute python file, relative to the working directory",
                ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Arguments for function call if required",
                ),
            },
        ),
    )     