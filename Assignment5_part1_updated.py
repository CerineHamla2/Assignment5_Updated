
def temp_conversion(degree, scale, desired_scale):
    """Convert temperature from Celsius, Fahrenheit, or Kelvin to another scale."""

    # Check if the temperature is a valid number
    if not isinstance(degree, (int, float)):
        raise ValueError("Invalid temperature value. Please enter a valid number.")

    # Convert scales to uppercase to accept both lowercase and uppercase inputs
    scale = scale.upper()
    desired_scale = desired_scale.upper()

    # Check if the entered scales are valid
    if scale not in ("C", "F", "K") or desired_scale not in ("C", "F", "K"):
        raise ValueError("Invalid scale. Please use C, F, or K.")


    # If both scales are the same, return the original temperature
    if scale == desired_scale:
        return degree

    elif scale == "C" and desired_scale == "F":  # Celsius to Fahrenheit
        return (degree * 9/5) + 32

    elif scale == "C" and desired_scale == "K":  # Celsius to Kelvin
        return degree + 273.15

    elif scale == "F" and desired_scale == "C":  # Fahrenheit to Celsius
        return (degree - 32) * 5/9

    elif scale == "F" and desired_scale == "K":  # Fahrenheit to Kelvin
        return ((degree - 32) * 5/9) + 273.15

    elif scale == "K" and desired_scale == "C":  # Kelvin to Celsius
        return degree - 273.15

    elif scale == "K" and desired_scale == "F":  # Kelvin to Fahrenheit
        return ((degree - 273.15) * 9/5) + 32



# Test the function

try:
    degree = float(input("Enter the temperature value: "))
    scale = input("Enter the scale (C, F, K): ")
    desired_scale = input("Enter the desired scale (C, F, K): ")

    converted_temp = round(temp_conversion(degree, scale, desired_scale), 2)
    print("The converted temperature is:", converted_temp)

except ValueError:
    print("Invalid input, enter a valid Temperature value")
