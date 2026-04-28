import sys

script_name = sys.argv.pop(0)
first_arg = sys.argv.pop(0)

print(f"first arg is '{first_arg}'")
for file_path in sys.argv:  # skip script name
    print(f"Processing {file_path}")
    with open(file_path) as file_in:
        pass   #  read each file here

