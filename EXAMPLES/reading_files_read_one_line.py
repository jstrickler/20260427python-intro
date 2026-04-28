FILE_PATH = '../DATA/mary.txt'

with open(FILE_PATH) as mary_in:
    first_line = mary_in.readline()
    print(first_line.rstrip())
    print('-' * 60)
    for line in mary_in:
        print(line.rstrip())

