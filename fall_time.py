import math
from constants import earth_g, mars_g  # Importing constants from constants.py

def calculate_fall_time(height, gravity):
    """Calculate the fall time based on height and gravity."""
    return math.sqrt(2 * height / gravity)

if __name__ == '__main__':
    height = float(input('Height in meters: '))
    print(f'Earth: {calculate_fall_time(height, earth_g):.2f} seconds')
    print(f'Mars: {calculate_fall_time(height, mars_g):.2f} seconds')
