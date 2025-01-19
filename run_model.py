import numpy as np
import pandas as pd
import subprocess

# Define the input vector X_input with the desired values
X_input = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 42])

# Optionally, create a batch of N input vectors (N copies of X_input)
N = 3
X_input_batch = np.tile(X_input, (N, 1))  # Shape will be (N, 9)

# input
input_file_path = 'input.txt'
np.savetxt(input_file_path, X_input_batch, delimiter=',')
print(f'Input data written to {input_file_path}')

exe_path = './local_model_dummy.exe'  # Path to the executable in the current folder
#exe_path = '/Users/hasal/OneDrive/UQ_Resources/local_model_windows.exe'
command = [exe_path, input_file_path]

print('Running simulation executable...')
result = subprocess.run(command, capture_output=True, text=True)

# Print the output from the executable
print(result.stdout)

output_file_path = 'Y_out.csv'
df = pd.read_csv(output_file_path, header=None)

print(f'Simulation output data loaded from {output_file_path}')

# Extract unique sample indices (Column 7 contains sample indices)
sample_indices = df[6].unique()
num_samples = len(sample_indices)

# Drop the sample index column
df = df.drop(columns=[6])

# Convert the DataFrame to a NumPy array and reshape into the desired 3D format (num_time_steps x num_features x num_samples)
Y_out = df.to_numpy().reshape(num_samples, 60, 6).transpose(1, 2, 0)

print('Output values for the first timestep for all 6 features of sample 3:')
print(Y_out[0, :, 2])

