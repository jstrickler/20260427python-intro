import logging

logging.basicConfig(
    filename="c2f_loop.log",
)

while True:
    celsius = input('Enter Celsius temp: ')
    if celsius.lower().startswith('q'):
        break
    try:
        celsius = float(celsius)
    except ValueError as err:
        print("Please enter a number")
        logging.warning("Invalid value %s", celsius)
        continue
    fahrenheit = ((9 * celsius) / 5) + 32
    print(f"{celsius:.1f} C is {fahrenheit:.1f} F")

