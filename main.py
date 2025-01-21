def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def main():
    print("Unit Converter")
    print("Choose a conversion type:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        km = float(input("Enter the distance in kilometers: "))
        print(f"{km} kilometers is equal to {km_to_miles(km):.2f} miles.")
    elif choice == "2":
        miles = float(input("Enter the distance in miles: "))
        print(f"{miles} miles is equal to {miles_to_km(miles):.2f} kilometers.")
    elif choice == "3":
        celsius = float(input("Enter the temperature in Celsius: "))
        print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F.")
    elif choice == "4":
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C.")
    elif choice == "5":
        kg = float(input("Enter the weight in kilograms: "))
        print(f"{kg} kilograms is equal to {kg_to_pounds(kg):.2f} pounds.")
    elif choice == "6":
        pounds = float(input("Enter the weight in pounds: "))
        print(f"{pounds} pounds is equal to {pounds_to_kg(pounds):.2f} kilograms.")
    else:
        print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
