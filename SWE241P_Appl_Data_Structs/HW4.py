# Task Description:

# Imagine an island archipelago that consists of several disconnected islands.
# Within the islands, the pair of cities are connected through a unique highway.
# You can assume that you can reach every city from a city within the island.
# There can be multiple unique roads between cities.
# You are given two text files -  
# city_population.txt, contains a list of all cities and their population.
# The file data format is in <city name>: <population>.
# For example, City A: 1000 means City A has a population of 1000. 
# You can assume each city has a unique name.  


# road_network.txt, contains the list of all highways in the island archipelago.
# The file data format is in <city name 1>: <city name 2>.
# For example, City A: City B. Means City A and City B are connected by a unique highway.
# You can consider the highways as bi-directional.
# --------------------------------------------------------------------

# Task-1: Implement a class City that will include the following fields - [4 pt]

# Name of the city 
# The population of the city
# List of cities that are connected to this particular city. 

class City:
    def __init__(self,name,population = 0):
        self.name = name
        self.population = population
        self.connected_cities = []

    #adds a new city to the adjacency list 
    def add_Connection(self,City):
        if City not in self.connected_cities:  # ← Check for duplicates
            self.connected_cities.append(City)


# Task-2: Read the text file and construct a graph of cities.
# Use the objects of a class City to model a city and the graph.
# Note that conceptually, this is similar to the adjacency list representation of the graph. 


        """Creates a dict of city name/node object pairs
           Iterates through networktxt file and adds each connection to apecified citys node.
           returns created dict
        
        """
def read_road_network(filename):
    city_pairs = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Strip whitespace and split by ' : '
                line = line.strip()
                
                if line:  # Skip empty lines
                    # Split on ' : ' to get the two cities
                    parts = line.split(' : ')
                    
                    if len(parts) == 2:
                        city1 = parts[0].strip()
                        city2 = parts[1].strip()
                        city_pairs.append((city1, city2))
                    else:
                        print(f"Warning: Invalid line format: {line}")
        
        return city_pairs
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    


def read_city_population(filename, graph):
    """Read and update city populations"""
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(': ')
                    if len(parts) == 2:
                        city_name = parts[0].strip()
                        population = int(parts[1].strip())
                        
                        # Update existing city or create new one
                        if city_name in graph:
                            graph[city_name].population = population
                        else:
                            # City in population file but not in road network
                            graph[city_name] = City(city_name, population)
    
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")
"""
Creates a Adjacency list impleneted as a map.
Key = City name
Value = City class implementation
"""
def create_Graph():
    pairs = read_road_network('road_network.txt')
    #iterate through pairs, and create a frequency map implementation
    graph = {}
    for city1,city2 in pairs:
        #if city 1 isnt already in the dict, make a new City instance with that city
        if city1 not in graph:
            graph[city1] = City(city1)
        #if city2 isnt in the dict, make a new City instance with that city
        if city2 not in graph:
            graph[city2] = City(city2)

        #add the listed connection to each citys connected_cities attribute
        graph[city1].add_Connection(graph[city2])
        graph[city2].add_Connection(graph[city1])

    read_city_population('city_population.txt', graph)
    return graph



""" Task 3 """
# Task-3:  Given the list of City objects, write a function to return the number of islands in the 
# archipelago. Note that this function would require finding the number of connected components in 
# the graph.
def findIslands(graph):
    def dfs(city):
        visited.add(city.name)  
        for adjacent in city.connected_cities:
            if adjacent.name not in visited: 
                dfs(adjacent)

    visited = set()
    numIslands = 0
    
    for city in graph: 
        if city not in visited: 
            numIslands += 1
            dfs(graph[city]) 
    
    return numIslands
"""

Task-4:  Given the list of City objects, write a function that would return the
population of each island in the island archipelago.
Note that this function would require you to find the population of each connected component
in the graph. """
def findPopulation(graph):
    def dfs(city):
        visited.add(city.name)  # Adding STRING
        population = city.population
        for adjacent in city.connected_cities:
            if adjacent.name not in visited:  # ← Check STRING not object
                population += dfs(adjacent)
        return population
    
    visited = set()
    populations = []
    
    for city in graph:
        if city not in visited:
            islandpop = dfs(graph[city])
            populations.append(islandpop)
    
    return populations


def main():
    graph = create_Graph()
    print(findPopulation(graph))
    


# Call main when script is run
if __name__ == "__main__":
    main()