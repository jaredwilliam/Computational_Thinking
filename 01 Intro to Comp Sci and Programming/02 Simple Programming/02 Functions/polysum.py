def polysum(n,s):
    '''
    Assumes n and s are numbers
    n is the number of sides to the regular polygon
    s is the length of each side to the regular polygon
    Returns the sum of the area and perimeter squared, rounded to 4 decimals
    '''
    import math

    # Calculate the area of the regular poygon
    area = 0.25*n*s**2 / math.tan(math.pi/n)

    # Calculate perimeter squared of the regular polygon
    perim_sq = (n*s)**2

    # Return the sum of area and perimeter squared
    return round(area+perim_sq,4)
