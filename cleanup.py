import os

# Example function, not uninstall packages with the 
# digram py in their name. Please update accordingly
def filter_function(name):
    return 'py' not in name

conda_list_output = os.popen('conda list').read()

output_in_lines = conda_list_output.split('\n')

# Line 4 and onwards is what we want

output_in_lines = output_in_lines[3:]

# Name appears in the beginning of the line
only_names = [line.strip().split(' ')[0] for line in output_in_lines]

filtered_list = list(filter(filter_function, only_names))

cmd = f'conda uninstall {" ".join(filtered_list)}'

os.system(cmd)

