FILE1_PATH = "../DATA/customerdata1.txt"
FILE2_PATH = "../DATA/customerdata2.txt"

customer_data = {}

for file_path in FILE1_PATH, FILE2_PATH:
    customer_data[file_path] = []
    with open(file_path) as file_in:
        for line in file_in:
            row_id, customer_id, first_name, last_name, email = line.split('\t')
            customer_data[file_path].append(f"{first_name} {last_name}")

customer1_names = set(customer_data[FILE1_PATH])
customer2_names = set(customer_data[FILE2_PATH])

print(f"{customer1_names = }\n")

print(f"{customer2_names = }\n")

common = customer1_names & customer2_names
print(f"{common = }\n")

delta = customer1_names ^ customer2_names
print(f"delta (XOR) = {delta}\n")

combined = customer1_names | customer2_names
print(f"{combined = }\n")
