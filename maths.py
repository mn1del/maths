# Something to help the kids with, not to be confused with the built in math module!


from random import randint

def get_simple_addition(max_x=10, max_y=10):
    """
    Generate the number of an addition problem: x + y = z .
    Return a dict with keys: operator, x, y, z

    args:
        max_x: (int) max allowable x
        max_y: (int) max allowable y
    """
    x = randint(0, max_x)
    y = randint(0, max_y)
    z = x + y
    return ("+", x, y, z)

def get_simple_subtraction(max_x=100, max_y=10):
    """
    Generate the number of an subtraction problem: x - y = z .
    Return a dict with keys: operator, x, y, z

    args:
        max_x: (int) max allowable x
        max_y: (int) max allowable y
    """
    y = randint(0, max_y)
    x = max(y, randint(0, max_x))
    z = x - y
    return ("-", x, y, z)

def make_simple_sentance(operator, x, y, z, solve_for="random"):
    """
    return string in the format "x + y = z"

    args:
        operator: (str) e.g. "+"
        x: (number)
        y: (number)
        z: (number)
        solve_for: (str) "x"|"y"|"z"|"random"
    """
    if solve_for == "random":
        solve_for = ("x", "y", "z")[randint(0,2)]
    if solve_for == "z":
        sentance = "{} {} {} = ___".format(x, operator, y)
    elif solve_for == "x":
        sentance = "___ {} {} = {}".format(operator, y, z)
    elif solve_for == "y":
        sentance = "{} {} ___ = {}".format(x, operator, z)
    return sentance
