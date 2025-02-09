import subprocess

# input file path
input_file_path = './input3.txt'


# Step 3: Run the executable and capture its output
exe_path = 'local_model_windows.exe'  # Path to the executable in the current folder
command = [exe_path, input_file_path]

print('Simulation executable has been called.')
result = subprocess.run(command, capture_output=True, text=True)


# Print the output from the executable
print(result.stdout)