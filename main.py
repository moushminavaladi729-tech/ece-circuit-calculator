def calculate_voltage():
    current = float(input("Enter Current (A): "))
    resistance = float(input("Enter Resistance (Ohm): "))
    voltage = current * resistance
    print(f"Voltage = {voltage} V")


def calculate_current():
    voltage = float(input("Enter Voltage (V): "))
    resistance = float(input("Enter Resistance (Ohm): "))

    if resistance == 0:
        print("Resistance cannot be zero!")
    else:
        current = voltage / resistance
        print(f"Current = {current} A")


def calculate_resistance():
    voltage = float(input("Enter Voltage (V): "))
    current = float(input("Enter Current (A): "))

    if current == 0:
        print("Current cannot be zero!")
    else:
        resistance = voltage / current
        print(f"Resistance = {resistance} Ohm")


def calculate_power():
    voltage = float(input("Enter Voltage (V): "))
    current = float(input("Enter Current (A): "))
    power = voltage * current
    print(f"Power = {power} W")


while True:
    print("\n===== ECE CIRCUIT CALCULATOR =====")
    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")
    print("4. Calculate Power")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        calculate_voltage()
    elif choice == "2":
        calculate_current()
    elif choice == "3":
        calculate_resistance()
    elif choice == "4":
        calculate_power()
    elif choice == "5":
        print("Thank you for using ECE Circuit Calculator!")
        break
    else:
        print("Invalid choice! Please try again.")
