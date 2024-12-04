# Function to put the data into a 2D list
def get_elevation(file):
    elevations = []
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = list(line.strip("\n").split(' '))
            l = []
            for i in line:
                l.append(int(i))
            elevations.append(l)
    return elevations

# Return elevation difference between two vertices (x1, y1) and (x2, y2)
def get_elevation_diff(elevations, x1, y1, x2, y2):
	return abs(elevations[x1][y1] - elevations[x2][y2])

# Output all routes in a file
def output_file(file, routes):
    output_file = open(file, "w+")
    for route in routes:
        output_file.write(str(route[len(route)-1]))  # Last column is distance
        for i in range(len(route) - 1):
            output_file.write(' ' + str(route[i]))
        output_file.write("\n")

# Output the overall shortest path data to a file
def output_best(file, routes):
    lst = []
    with open(file, "w+") as output_best:
        for r in routes:
            lst.append(r[-1])  # get the total elevation difference
        minimum = min(lst)
        num = lst.index(minimum)
        best_route = routes[num]

        output_best.write(str(best_route[-1]))
        for i in range(len(best_route)-1):
            output_best.write(' ' + str(best_route[i]))
        output_best.write("\n")
