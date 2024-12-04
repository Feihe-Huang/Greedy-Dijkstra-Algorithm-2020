import dijkastra_route

from route_utility import get_elevation_diff
from route_utility import get_elevation

from route_utility import output_file
from route_utility import output_best

file = input("Please enter the name of the map file you want to analyse:\n")  # this enable users to choose a map to analyze

# Return the string representation of a vertex in the format of (x, y)
def get_vertex_str(x, y):
	return "("+str(x)+", "+str(y)+")"

# Return the x value in a string representation of a vertex in the format of (x, y)
def get_vertex_str_x(vertex_str):
	return vertex_str.split(", ")[0].strip("(")

# Return the y value in a string representation of a vertex in the format of (x, y)
def get_vertex_str_y(vertex_str):
	return vertex_str.split(", ")[1].strip(")")

# Return the tuple path representation requested by the dijkstra algorithm in the format of (vertex1, vertex2, elevation_diff)
def get_path_tuple(elevation_list, x1, y1, x2, y2):
	return (get_vertex_str(x1, y1), get_vertex_str(x2, y2), get_elevation_diff(elevation_list, x1, y1, x2, y2))

# Output route data in a dictionary to a list
def get_routes(route_dict):
	routes = []
	for start_vertex in route_dict:
		route = []
		elevation_diff = route_dict[start_vertex][0]
		route_data = route_dict[start_vertex][1]
		for vertex in route_data[::-1]:
			column = get_vertex_str_y(vertex)
			route.append(column)
		route.append(elevation_diff)
		routes.append(route)

	return routes


elevations = get_elevation(file)  # Store the data in a 2D list
row = elevations[0][0]
column = elevations[0][1]
del elevations[0]

# Now get all edges
edges = []

for j in range(row-1):  # row
	for k in range(column):  # column
		if k == 0:
			edges.append(get_path_tuple(elevations, j, k, j+1, k))
			edges.append(get_path_tuple(elevations, j, k, j+1, k+1))
		elif k == len(elevations[0]) - 1:
			edges.append(get_path_tuple(elevations, j, k, j+1, k))
			edges.append(get_path_tuple(elevations, j, k, j+1, k-1))
		else:
			edges.append(get_path_tuple(elevations, j, k, j+1, k))
			edges.append(get_path_tuple(elevations, j, k, j+1, k-1))
			edges.append(get_path_tuple(elevations, j, k, j+1, k+1))

route_dict = {}
routes = []

# Now get the route from every starting point
for i in range(column): #column
	start_vertex = get_vertex_str(0, i)
	for j in range(column):  # column
		end_vertex = get_vertex_str(row-1, j)
		route = dijkastra_route.get_route(edges, start_vertex, end_vertex)

		if start_vertex in route_dict:
			cur_shortest_path = route_dict[start_vertex]
			if route[0] < cur_shortest_path[0]:
				route_dict[start_vertex] = route
		else:
			route_dict[start_vertex] = route

# Convert data to the format required by output functions
routes = get_routes(route_dict)

path_file = "dijkstra_routes.rt"
best_path_file = "dijkstra_best.rt"

output_file(path_file, routes)
output_best(best_path_file, routes)
