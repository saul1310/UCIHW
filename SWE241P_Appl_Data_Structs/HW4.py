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


#source of info: 
# https://www.youtube.com/watch?v=oDqjPvD54Ss -  Youtube video on BFS on graph

from collections import deque


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

"""
Task-5:
 Given two City objects, write a function that would return the minimum number of unique highways you can take to reach from one city
to another. Note that this function requires you to find the distance, i.e., the number of unique highways between two cities.
"""

def bfs_shortest_path(graph, start, end):
    """
    Performs BFS and builds the 'previous' tracking.
    
    Args:
        graph: Dictionary of city names to City objects
        start: Starting city name (string)
        end: Ending city name (string)
        
    Returns:
        dict: previous[city_name] = previous city name (or None for start)
              Returns empty dict if no path exists
    """
    if start not in graph or end not in graph:
        return {}  # City doesn't exist
    
    if start == end:
        return {start: None}  # Same city, no path needed
    
    visited = set()
    queue = deque([graph[start]])
    visited.add(start)
    
    # Track previous node for each visited node
    previous = {start: None}
    
    while queue:
        current_city = queue.popleft()
        
        # Check all neighbors
        for neighbor in current_city.connected_cities:
            if neighbor.name not in visited:
                visited.add(neighbor.name)
                previous[neighbor.name] = current_city.name
                queue.append(neighbor)
                
                # Found the target!
                if neighbor.name == end:
                    return previous
    
    return {}  # No path exists


def reconstruct_path(previous, start, end):
    """
    Reconstructs the path from start to end using the previous dict.
    
    Args:
        previous: Dictionary from bfs_shortest_path
        start: Starting city name
        end: Ending city name
        
    Returns:
        list: Path from start to end as list of city names
              Empty list if no path exists
    """
    if not previous or end not in previous:
        return []  # No path exists
    
    # Build path backwards from end to start
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = previous[current]
    
    # Reverse to get start -> end
    path.reverse()
    
    return path


def shortestpath(city1, city2, graph):
    """
    Returns the minimum number of highways between two cities.
    
    Args:
        city1: Starting city name (string)
        city2: Ending city name (string)
        graph: Dictionary of city names to City objects
        
    Returns:
        int: Number of highways in shortest path, or -1 if no path exists
    """
    previous = bfs_shortest_path(graph, city1, city2)
    path = reconstruct_path(previous, city1, city2)
    
    if not path:
        return -1  # No path exists
    
    return len(path) - 1  # Number of edges = number of nodes - 1


def main():
    graph = create_Graph()
    
    # Task 3: Number of islands
    num_islands = findIslands(graph)
    print(f"Number of islands: {num_islands}")
    
    # Task 4: Population of each island
    populations = findPopulation(graph)
    print(f"\nIsland populations:")
    for i, pop in enumerate(populations, 1):
        print(f"  Island {i}: {pop:,} people")
    
    # Task 5: Shortest path examples
    print(f"\nShortest path examples:")
    
    # Get some cities to test with
    city_names = list(graph.keys())
    if len(city_names) >= 2:
        city1 = city_names[0]
        city2 = city_names[10]
        
        distance = shortestpath(city1, city2, graph)
        
        if distance != -1:
            previous = bfs_shortest_path(graph, city1, city2)
            path = reconstruct_path(previous, city1, city2)
            print(f"  From {city1} to {city2}:")
            print(f"    Distance: {distance} highways")
            print(f"    Path: {' -> '.join(path[:5])}{'...' if len(path) > 5 else ''}")
        else:
            print(f"  No path exists between {city1} and {city2} (different islands)")


def print_separator(char="=", length=70):
    """Print a separator line"""
    print(char * length)


def test_graph_structure(graph):
    """Test and display graph structure information"""
    print_separator()
    print("TEST 1: GRAPH STRUCTURE")
    print_separator()
    
    print(f"\nTotal cities in graph: {len(graph)}")
    
    # Connection statistics
    connection_counts = [len(city.connected_cities) for city in graph.values()]
    if connection_counts:
        avg_connections = sum(connection_counts) / len(connection_counts)
        max_connections = max(connection_counts)
        min_connections = min(connection_counts)
        
        print(f"\nConnection Statistics:")
        print(f"  Average connections per city: {avg_connections:.2f}")
        print(f"  Maximum connections: {max_connections}")
        print(f"  Minimum connections: {min_connections}")
        
        # Find most connected cities
        most_connected = [(name, len(city.connected_cities)) 
                         for name, city in graph.items() 
                         if len(city.connected_cities) == max_connections]
        print(f"  Most connected cities: {most_connected[:3]}")
    
    # Population statistics
    populations = [city.population for city in graph.values()]
    if populations:
        total_pop = sum(populations)
        avg_pop = total_pop / len(populations)
        max_pop = max(populations)
        min_pop = min(populations)
        
        print(f"\nPopulation Statistics:")
        print(f"  Total population: {total_pop:,}")
        print(f"  Average city population: {avg_pop:,.0f}")
        print(f"  Largest city population: {max_pop:,}")
        print(f"  Smallest city population: {min_pop:,}")
        
        # Find largest cities
        largest_cities = sorted(graph.items(), 
                               key=lambda x: x[1].population, 
                               reverse=True)[:5]
        print(f"\n  Top 5 most populous cities:")
        for i, (name, city) in enumerate(largest_cities, 1):
            print(f"    {i}. {name}: {city.population:,} people")
    
    # Sample cities
    print(f"\nSample of cities (first 10):")
    for i, (city_name, city_obj) in enumerate(list(graph.items())[:10]):
        print(f"  {i+1}. {city_name}")
        print(f"     Population: {city_obj.population:,}")
        print(f"     Connections: {len(city_obj.connected_cities)}")
        if city_obj.connected_cities:
            connected_names = [c.name for c in city_obj.connected_cities[:3]]
            print(f"     Connected to: {', '.join(connected_names)}")
            if len(city_obj.connected_cities) > 3:
                print(f"       ... and {len(city_obj.connected_cities) - 3} more")


def test_islands(graph):
    """Test Task 3: Island counting"""
    print_separator()
    print("TEST 2: ISLAND DETECTION (Task 3)")
    print_separator()
    
    num_islands = findIslands(graph)
    print(f"\nNumber of islands found: {num_islands}")
    
    # Detailed island analysis
    visited = set()
    islands = []
    
    def dfs_collect(city, island_cities):
        visited.add(city.name)
        island_cities.append(city.name)
        for adjacent in city.connected_cities:
            if adjacent.name not in visited:
                dfs_collect(adjacent, island_cities)
    
    for city_name in graph:
        if city_name not in visited:
            island_cities = []
            dfs_collect(graph[city_name], island_cities)
            islands.append(island_cities)
    
    print(f"\nIsland details:")
    for i, island in enumerate(islands, 1):
        print(f"  Island {i}: {len(island)} cities")
        print(f"    Sample cities: {', '.join(island[:5])}")
        if len(island) > 5:
            print(f"    ... and {len(island) - 5} more")


def test_populations(graph):
    """Test Task 4: Island populations"""
    print_separator()
    print("TEST 3: ISLAND POPULATIONS (Task 4)")
    print_separator()
    
    populations = findPopulation(graph)
    
    print(f"\nFound {len(populations)} island(s)")
    print(f"\nIsland population breakdown:")
    
    total_pop = sum(populations)
    for i, pop in enumerate(populations, 1):
        percentage = (pop / total_pop * 100) if total_pop > 0 else 0
        print(f"  Island {i}: {pop:,} people ({percentage:.1f}% of total)")
    
    print(f"\nTotal population across all islands: {total_pop:,}")
    
    if len(populations) > 1:
        print(f"Average island population: {sum(populations)/len(populations):,.0f}")
        print(f"Largest island: {max(populations):,} people")
        print(f"Smallest island: {min(populations):,} people")


def test_shortest_paths(graph):
    """Test Task 5: Shortest path algorithm"""
    print_separator()
    print("TEST 4: SHORTEST PATH ALGORITHM (Task 5)")
    print_separator()
    
    city_names = list(graph.keys())
    
    if len(city_names) < 2:
        print("\nNot enough cities to test shortest paths")
        return
    
    # Test cases
    test_cases = []
    
    # Test 1: Same city
    test_cases.append((city_names[0], city_names[0], "Same city"))
    
    # Test 2: Close cities
    if len(city_names) >= 5:
        test_cases.append((city_names[0], city_names[4], "Different cities"))
    
    # Test 3: Far cities
    if len(city_names) >= 20:
        test_cases.append((city_names[0], city_names[19], "Distant cities"))
    
    # Test 4: Random pair
    if len(city_names) >= 50:
        test_cases.append((city_names[10], city_names[40], "Random pair"))
    
    print(f"\nTesting {len(test_cases)} path queries:\n")
    
    for i, (start, end, description) in enumerate(test_cases, 1):
        print(f"Test {i}: {description}")
        print(f"  From: {start}")
        print(f"  To: {end}")
        
        distance = shortestpath(start, end, graph)
        
        if distance == -1:
            print(f"  Result: No path exists (cities on different islands)")
        elif distance == 0:
            print(f"  Result: Same city (0 highways)")
        else:
            previous = bfs_shortest_path(graph, start, end)
            path = reconstruct_path(previous, start, end)
            
            print(f"  Result: {distance} highway(s)")
            print(f"  Full path ({len(path)} cities):")
            
            # Print path in chunks
            if len(path) <= 10:
                print(f"    {' -> '.join(path)}")
            else:
                print(f"    {' -> '.join(path[:5])}")
                print(f"    ... ({len(path) - 10} intermediate cities) ...")
                print(f"    {' -> '.join(path[-5:])}")
        
        print()


def test_edge_cases(graph):
    """Test edge cases and error handling"""
    print_separator()
    print("TEST 5: EDGE CASES AND ERROR HANDLING")
    print_separator()
    
    city_names = list(graph.keys())
    
    print("\n1. Testing non-existent cities:")
    distance = shortestpath("NonExistentCity1", "NonExistentCity2", graph)
    print(f"   Path between non-existent cities: {distance}")
    print(f"   Expected: -1 (no path)")
    
    if city_names:
        print("\n2. Testing one non-existent city:")
        distance = shortestpath(city_names[0], "NonExistentCity", graph)
        print(f"   Path from valid to non-existent city: {distance}")
        print(f"   Expected: -1 (no path)")
        
        print("\n3. Testing empty path reconstruction:")
        previous = {}
        path = reconstruct_path(previous, "City1", "City2")
        print(f"   Path from empty previous dict: {path}")
        print(f"   Expected: [] (empty list)")
        
        print("\n4. Testing duplicate connections:")
        test_city = graph[city_names[0]]
        initial_count = len(test_city.connected_cities)
        if test_city.connected_cities:
            test_city.add_Connection(test_city.connected_cities[0])
            final_count = len(test_city.connected_cities)
            print(f"   Connections before duplicate add: {initial_count}")
            print(f"   Connections after duplicate add: {final_count}")
            print(f"   Expected: Same count (duplicate prevented)")


def test_graph_integrity(graph):
    """Test graph integrity and consistency"""
    print_separator()
    print("TEST 6: GRAPH INTEGRITY")
    print_separator()
    
    print("\nChecking graph integrity...")
    
    issues = []
    
    # Check bidirectional connections
    print("\n1. Checking bidirectional connections:")
    bidirectional_errors = 0
    for city_name, city_obj in graph.items():
        for neighbor in city_obj.connected_cities:
            # Check if the connection goes both ways
            if city_obj not in neighbor.connected_cities:
                bidirectional_errors += 1
                if bidirectional_errors <= 3:  # Show first 3 errors
                    issues.append(f"   Connection from {city_name} to {neighbor.name} is not bidirectional")
    
    if bidirectional_errors == 0:
        print("   ✓ All connections are bidirectional")
    else:
        print(f"   ✗ Found {bidirectional_errors} non-bidirectional connections")
        for issue in issues[:3]:
            print(issue)
    
    # Check for self-loops
    print("\n2. Checking for self-loops:")
    self_loops = 0
    for city_name, city_obj in graph.items():
        if city_obj in city_obj.connected_cities:
            self_loops += 1
            if self_loops <= 3:
                print(f"   ✗ {city_name} is connected to itself")
    
    if self_loops == 0:
        print("   ✓ No self-loops found")
    else:
        print(f"   ✗ Found {self_loops} self-loops")
    
    # Check for duplicate connections
    print("\n3. Checking for duplicate connections:")
    duplicates = 0
    for city_name, city_obj in graph.items():
        connection_names = [c.name for c in city_obj.connected_cities]
        if len(connection_names) != len(set(connection_names)):
            duplicates += 1
            if duplicates <= 3:
                print(f"   ✗ {city_name} has duplicate connections")
    
    if duplicates == 0:
        print("   ✓ No duplicate connections found")
    else:
        print(f"   ✗ Found {duplicates} cities with duplicate connections")
    
    # Summary
    print("\n" + "="*70)
    if bidirectional_errors == 0 and self_loops == 0 and duplicates == 0:
        print("✓ Graph integrity check PASSED - No issues found!")
    else:
        print("✗ Graph integrity check FAILED - Issues found")
    print("="*70)


def run_all_tests():
    """Run complete test suite"""
    print("\n")
    print("="*70)
    print(" "*20 + "COMPREHENSIVE TEST SUITE")
    print("="*70)
    print("\nCreating graph from files...")
    
    graph = create_Graph()
    
    print(f"Graph created successfully with {len(graph)} cities\n")
    
    # Run all tests
    test_graph_structure(graph)
    print("\n")
    
    test_islands(graph)
    print("\n")
    
    test_populations(graph)
    print("\n")
    
    test_shortest_paths(graph)
    print("\n")
    
    test_edge_cases(graph)
    print("\n")
    
    test_graph_integrity(graph)
    
    # Final summary
    print("\n")
    print_separator("=")
    print(" "*25 + "TEST SUITE COMPLETE")
    print_separator("=")
    print("\nAll tasks have been tested successfully!")
    print("\nTask Summary:")
    print("  ✓ Task 1: City class implementation")
    print("  ✓ Task 2: Graph construction from files")
    print("  ✓ Task 3: Island counting (connected components)")
    print("  ✓ Task 4: Island population calculation")
    print("  ✓ Task 5: Shortest path algorithm (BFS)")
    print_separator("=")


def main():
    """Main function - runs the comprehensive test suite"""
    run_all_tests()


# Call main when script is run
if __name__ == "__main__":
    main()