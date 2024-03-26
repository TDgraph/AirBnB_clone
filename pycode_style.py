#!/usr/bin/python3

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width


def main():
    # Inputs
    length = 5
    width = 10

    # Calculate area
    area = calculate_area(length, width)

    # Output
    print(f"The area of the rectangle is: {area}")


if __name__ == "__main__":
    main()
