from route_utility import get_elevation
from route_utility import output_file
from route_utility import output_best
from greedy_route import get_greedy_route

file = input("Please enter the name of the map file you want to analyse:\n")  # this enable users to choose a map to analyze


elevations = get_elevation(file)  # Store the data in a 2D list
row = elevations[0][0]
column = elevations[0][1]
del elevations[0]

# Now get the route from every starting point
routes = []
for x in range(column):
    route = get_greedy_route(x, elevations)
    routes.append(route)

# Now output all routes and the best route 
output_file("greedy_routes.rt", routes)
output_best("greedy_best.rt",routes)
    
