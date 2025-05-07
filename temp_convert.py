# Author: 2025 Mikhail Ibrahim
# Date: May 7th, 2025
# Description: A crash-proof Python program that converts temperature
# from Celsius to Fahrenheit. The program handles invalid inputs safely.


def main():
    print("Welcome to the Temperature Converter (Celsius to Fahrenheit)")

    try:
        celsius = float(input("Enter temperature (Celsius): "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit:.1f}°F")

    except ValueError:
        print("Invalid input. Please enter a number.")


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
