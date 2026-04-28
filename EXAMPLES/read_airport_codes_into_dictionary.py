DATA_FILE = '../DATA/world_airport_codes.txt'
# sample data
# ABE ALLENTOWN, PENNSYLVANIA, USA
# ABF ABAIANG, REP. OF KIRIBATI
# ABG ABINGDON, QLD., AUSTRALIA

AIRPORT_CODES = {}

with open(DATA_FILE) as codes_in:
    for raw_line in codes_in:
        line = raw_line.rstrip('\n')
        code = line[:3]  # first three chars
        airport = line[4:]  # fourth char through end
        AIRPORT_CODES[code] = airport
                      
print(f"{len(AIRPORT_CODES) = }")

while True:
    code = input("Enter airport code: ")
    if code == '': # user just pressed <ENTER>
        print("Please enter a code")
        continue
    if code == 'q':
        print("goodbye")
        break
    if len(code) != 3:
        print("Code must be 3 letters")
        continue
    if not code.isalpha():
        print("Code must consist only of letters")
        continue
    # use code.upper() so user can type in lower or upper
    city = AIRPORT_CODES.get(code.upper(), "NOT FOUND")
    print(city)
