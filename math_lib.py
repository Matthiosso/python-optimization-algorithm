def compute_line_between_two_coordinates(xA: int, yA: int, xB: int, yB: int) -> tuple:
    """
    Compute a and b representing the straight line crossing the two input coordinates (equation : y = a*x + b)

    Example :

    Input:
    pA = (1, 0)
    pB = (3, 2)

    Output:
    (1.0, -1.0) # y = x - 1
    """
    if xA == xB:
        return xA
    else:
        a = (yB - yA)/(xB - xA)
        b = yA - a*xA
        return a,b

def compute_perpendicular_line_crossing_one_coordinate(a: float, x: int, y: int):
    """
    Compute a and b representing the perpendicular line crossing a given axis (equation : y = a*x + b)
    
    Example :

    Input:
    a = 2.5
    pC = (7, 0)

    Output:
    (-0.4, 2.8000000000000003) # y = -0.4x+2.8000000000000003
    """
    newA = 0
    if a == 0:
        return x
    newA = -1/a
    newB = y - (newA * x)
    return newA, newB

def compute_crossing_point_between_two_lines(a1: float, b1: float, a2: float, b2: float) -> tuple:
    """
    Compute the coordinates of the point crossing two straight lines
    """
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return x, y

def get_point_from_line_crossing_C_and_perpendicular_with_line_between_A_and_B(point_A_x, point_A_y, point_B_x, point_B_y, point_C_x, point_C_y):
    """
    Get coordinates of the crossing point between the line from A to B, and its perpendicular line crossing C
    
    Example :

    Input:
    pA = (1, 1)
    pB = (6, 6)
    pC = (6, 1)

    Output:
    pD = (3.5, 3.5)
    """
    pointA = point_A_x, point_A_y
    pointB = point_B_x, point_B_y
    pointC = point_C_x, point_C_y
    line_A_B = compute_line_between_two_coordinates(*pointA, *pointB)
    if type(line_A_B) != tuple:
        print(f"Line A <-> B : x = {line_A_B}")
        raise Exception("A and B are aligned.")
    else:
        print(f"Line A <-> B : y = {line_A_B[0]}x+{line_A_B[1]}")
        line_crossing_C_perpendicular_to_line_A_B = compute_perpendicular_line_crossing_one_coordinate(line_A_B[0], *pointC)

    if type(line_crossing_C_perpendicular_to_line_A_B) != tuple:
        print(f"Line C <-> D : x = {line_crossing_C_perpendicular_to_line_A_B}")
        return line_crossing_C_perpendicular_to_line_A_B, line_A_B[1]
    else:
        print(f"Line C <-> D : y = {line_crossing_C_perpendicular_to_line_A_B[0]}x+{line_crossing_C_perpendicular_to_line_A_B[1]}")
        return compute_crossing_point_between_two_lines(*line_A_B, *line_crossing_C_perpendicular_to_line_A_B)


if __name__ == '__main__':

    examples = [
        ((1, 1), (6, 6), (6, 1)), #1
        ((0, 0), (5, 5), (5, 0)), #2
        ((0, 0), (7, 3), (7, 0)), #3
        ((0, 0), (2, 5), (7, 0)), #4 
        ((0, 2), (6, 2), (3, 0)), #5
        ((0, 2), (6, 2), (1, 1)), #6
        ((1, 0), (3, 2), (0, 5)), #7
        ((1, 2), (1, 3), (3, 1)), #8
    ]

    for idx, example in enumerate(examples):
        pA, pB, pC = example
        print(f"\nExample {idx+1}\nPoint A: {pA} ; Point B: {pB} ; Point C: {pC}")
        output = get_point_from_line_crossing_C_and_perpendicular_with_line_between_A_and_B(*pA, *pB, *pC)
        print(f"Output point is: {output}\n")
        print("-"*100)


