import os

# Define the directory you want to compile files from
project_directory = "/workspaces/DesktopAutomationAI"
output_file = "compiled_project.txt"
excluded_extensions = ['.pyc', '.o', '.exe', '.bin', '.pack']  # List of binary file extensions to exclude

def is_binary_file(file_path):
    """
    Returns True if the file contains binary data, otherwise False.
    """
    try:
        with open(file_path, 'rb') as file:
            # Read the first 1024 bytes and check if any non-text character is found
            chunk = file.read(1024)
            if b'\x00' in chunk:  # Null byte is an indicator of a binary file
                return True
        return False
    except Exception as e:
        print(f"Could not check file: {file_path}, error: {str(e)}")
        return True  # Skip files that can't be read

def compile_project_files(directory, output):
    # Open the output file in write mode
    with open(output, 'w') as output_f:
        # Walk through the project directory recursively
        for root, dirs, files in os.walk(directory):
            # Skip hidden directories (starting with ".")
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for file in files:
                file_path = os.path.join(root, file)
                # Check file extension for exclusions
                if any(file.endswith(ext) for ext in excluded_extensions) or is_binary_file(file_path):
                    continue
                
                try:
                    # Write the file header (path)
                    output_f.write(f"\n# Start of file: {file_path}\n")
                    # Read the file contents
                    with open(file_path, 'r', encoding='utf-8') as f:
                        output_f.write(f.read())
                    # Write the file footer
                    output_f.write(f"\n# End of file: {file_path}\n")
                except Exception as e:
                    print(f"Could not read file: {file_path}, error: {str(e)}")

if __name__ == "__main__":
    compile_project_files(project_directory, output_file)
    print(f"All files have been compiled into {output_file}")
