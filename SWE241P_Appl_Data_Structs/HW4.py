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
# –road_network.txt, tcontains the list of all highways in the island archipelago.
# The file data format is in <city name 1>: <city name 2>.
# For example, City A: City B. Means City A and City B are connected by a unique highway.
# You can consider the highways as bi-directional.
# --------------------------------------------------------------------

# Task-1: Implement a class City that will include the following fields - [4 pt]

# Name of the city 
# The population of the city
# List of cities that are connected to this particular city. 

class City:
    def __init__(self,name,population,connected):
        City.name = name
        City.population = population
        City.connected = connected

        

    
