import random

from route_utility import get_elevation_diff

def get_greedy_route(x, elevations):  # this function is used to record the route
    d = 0  # Total elevation difference
    row = len(elevations)
    column = len(elevations[0])

    route = []
    route.append(x)
    for i in range(row-1):
        if x == 0:  # This code is used when the start point is leftmost
            a1 = get_elevation_diff(elevations, i+1, x, i, x)
            a2 = get_elevation_diff(elevations, i+1, x+1, i, x)
            if a1 < a2:
                x = x
                d += a1
            else:
                x = x + 1
                d += a2
            route.append(x)
        elif x == column-1:  # This code is used when the start point is rightmost
            a3 = get_elevation_diff(elevations, i+1, x, i, x)
            a4 = get_elevation_diff(elevations, i+1, x-1, i, x)
            if a3 < a4:
                x = x
                d += a3
            else:
                x = x - 1
                d += a4
            route.append(x)
        else:  # This code is used when the start point is in the middle
            a5 = get_elevation_diff(elevations, i+1, x+1, i, x)  # Elevation difference to right
            a6 = get_elevation_diff(elevations, i+1, x, i, x)  # Elevation diffence to middle
            a7 = get_elevation_diff(elevations, i+1, x-1, i, x)  # Elevation diffence to left
            if a5 > a6 and a7 > a6:  # This is used when the middle elevation difference is the smallest
                x = x
                d += a6
            elif a5 < a6 and a5 < a7:  # This is used when the right elevation difference is the smallest
                x = x + 1
                d += a5
            elif a7 < a6 and a7 < a5:  # This is used when the left elevation difference is the smallest
                x = x - 1
                d += a7
            elif a5 == a7 and a5 < a6:  # This is used when the middle elevation difference is the largest and the left and the right is the same
                choice = random.choice( (1, -1))
                x = x + choice
                d += a5
            elif a5 == a6 or a6 == a7:  # This is used when the middle elevation difference is the same with the right or left
                x = x
                d += a6
            route.append(x)
    route.append(d)
    return route
