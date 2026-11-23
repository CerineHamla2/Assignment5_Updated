

def dice_roll(dice_configuration, desired_number):
    """Calculate the probability of rolling a sum greater than or equal to the desired number."""

    # Check if the dice configuration is a valid string containing 'd'
    if type(dice_configuration) != str or 'd' not in dice_configuration:
        raise ValueError("Invalid dice configuration. Please use a format like 2d6.")

    # Split the string to get the number of dice and sides
    my_list = dice_configuration.split("d")

    # Check that both parts contain valid integers
    if len(my_list) != 2 or not my_list[0].isdigit() or not my_list[1].isdigit():
        raise ValueError("Invalid dice configuration. Please use a format like 2d6.")

    num_dice = int(my_list[0])
    sides = int(my_list[1])

    # Check if the desired number is an integer
    if type(desired_number) != int:
        raise ValueError("Invalid desired number. Please enter an integer.")

    # Check that the entered values are positive
    if num_dice <= 0 or sides <= 1 or desired_number < 1:
        raise ValueError("Invalid input. Please enter positive integers.")

    # The maximum number of dice allowed is 4
    if num_dice > 4:
        raise ValueError("The maximum number of dice is 4.")

    # Calculate the total number of possible outcomes
    num_outcome = pow(sides, num_dice)
    probability = 0

    # One die
    if num_dice == 1:
        for j in range(1, sides + 1):
            if j >= desired_number:
                probability += 1 / num_outcome

    # Two dice
    elif num_dice == 2:
        for i in range(1, sides + 1):
            for j in range(1, sides + 1):
                if i + j >= desired_number:
                    probability += 1 / num_outcome

    # Three dice
    elif num_dice == 3:
        for i in range(1, sides + 1):
            for j in range(1, sides + 1):
                for k in range(1, sides + 1):
                    if i + j + k >= desired_number:
                        probability += 1 / num_outcome

    # Four dice
    elif num_dice == 4:
        for i in range(1, sides + 1):
            for j in range(1, sides + 1):
                for k in range(1, sides + 1):
                    for l in range(1, sides + 1):
                        if i + j + k + l >= desired_number:
                            probability += 1 / num_outcome

    # Return the probability rounded to 4 decimal places
    return round(probability, 4)


# Test the function using the assignment examples
test_cases = [ ("2d6", 7), ("4d6", 9), ("3d8", 22), ("1d20", 17), ("6e4", "A")]

for dice_config, desired_num in test_cases:
    try:
        result = dice_roll(dice_config, desired_num)
        print(dice_config, desired_num, "Probability:", result)
    except ValueError:
        print(dice_config, desired_num, "Error: Invalid Dice configuration/ desired output value, please enter a valid format")
