# Something to help the kids with, not to be confused with the built in math module!


from random import randint

def get_simple_addition(x_range=(0, 10), y_range=(0, 10)):
    """
    Generate the number of an addition problem: x + y = z .
    Return a dict with keys: operator, x, y, z

    args:
        x_range: (list like) min and max allowable x
        y_range: (list like) min and max allowable y
    """
    x = randint(*x_range)
    y = randint(*y_range)
    z = x + y
    return ("+", x, y, z)

def get_simple_subtraction(x_range=(10, 50), y_range=(0, 10)):
    """
    Generate the number of an subtraction problem: x - y = z .
    Return a dict with keys: operator, x, y, z

    args:
        x_range: (list like) min and max allowable x
        y_range: (list like) min and max allowable y
    """
    y = randint(*y_range)
    x = max(y, randint(*x_range))
    z = x - y
    return ("-", x, y, z)

def get_number_bond(z=10):
    """
    Return number bond adding up to answer

    args:
        z: (int) x and y to add up to z
    """
    x = randint(0, z)
    y = z - x
    return ("+", x, y, z)

def get_tens_partition(z_range=(11,100)):
    """
    Partitions a number, z, into x + y, where x is a multiple of 10.

    args:
        z_range: (list like) min and max allowable z
    """
    z = randint(*z_range)
    x = 10 * randint(int(round(z/10,0))-1)
    y = z - x
    return ("+", x, y, z)

def make_simple_sentance(operator, x, y, z, solve_for=("x", "y", "z"), line_break=True):
    """
    return string in the format "x + y = z"

    args:
        operator: (str) e.g. "+"
        x: (number)
        y: (number)
        z: (number)
        solve_for: (list like) values must be "x"|"y"|"z". Determines which number to solve for.
                   If multiple values are supplied, one will be randomly chosen
        line_break: (bool) If True, add a line break at the end of the sentance           
    """
    if type(solve_for) == str:
        solve_for = list(solve_for)
    solve_for = solve_for[randint(0, len(solve_for)-1)]    
    if solve_for == "z":
        sentance = "{} {} {} = ___".format(x, operator, y)
    elif solve_for == "x":
        sentance = "___ {} {} = {}".format(operator, y, z)
    elif solve_for == "y":
        sentance = "{} {} ___ = {}".format(x, operator, z)
    if line_break:
        sentance = "{}\n".format(sentance)
    return sentance


