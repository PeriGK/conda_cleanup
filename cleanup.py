import os

# Example function, not uninstall packages with the 
# digram py in their name. Please update accordingly
def filter_function(name):
    return 'py' not in name

# Get the installed conda packages
conda_list_output = os.popen('conda list').read()

# Put them in a list
output_in_lines = conda_list_output.split('\n')

# Line 4 and onwards is what we want (feel free to examine it)
output_in_lines = output_in_lines[3:]

# Name appears in the beginning of the line
only_names = [line.strip().split(' ')[0] for line in output_in_lines]

# Apply the filter defined above
filtered_list = list(filter(filter_function, only_names))

# Convert the list of uninstall candidates to a string
# and run the unins
cmd = f'conda uninstall {" ".join(filtered_list)}'

os.system(cmd)
