############################################
#squareCheck.py
#
#Takes: 4 ints or floats; or a tuple, list, or dict of 4 numbers
#Returns:   "Square" if the sides make a square
#           "Rectangle" if the sides make a rectangle
#
#Modified from source1.py, get_triangle_type() function
#
#Caleb Larson
#4/2/15
#CST 236
#
############################################


def get_rectangle_type(a=0, b=0, c=0, d=0):
    """
    Determine if the given rectangle is a square, or not

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float or int

    :param c: line c
    :type c: float or int

    :param d: line d
    :type d: float or int

    :return: "rectangle", "square", or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 4:
        d = a[3]
        c = a[2]
        b = a[1]
        a = a[0]

    elif isinstance(a, dict) and len(a.keys()) == 4:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]
        d = values[3]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(d, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d<= 0:
        return "invalid"

    if not (a == c and b == d):
        return "invalid"

    elif a == b:
        return "square"
    else:
        return "rectangle"
