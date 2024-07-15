import os
import subprocess

# Get the current directory
current_directory = os.getcwd()

# Iterate over every file in the current directory
for filename in os.listdir(current_directory):
    # Check if the file has a .svg extension
    if filename.endswith(".svg"):
        # Construct the full file path
        file_path = os.path.join(current_directory, filename)
        
        # Format the command with the file path
        command = f"svgexport {filename} {filename.replace("svg", "png")} :30"
        # Run the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
        # Print the output and error (if any) of the command
        print(f"Running command: {command}")
        print(f"Output:\n{result.stdout}")
        print(f"Error:\n{result.stderr}")
