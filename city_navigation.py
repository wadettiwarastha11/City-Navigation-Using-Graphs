
import heapq
from collections import deque

class CityMap:
    def __init__(self):
        self.graph = {}

    def add_road(self, place1, place2, distance):
        self.graph.setdefault(place1, [])
        self.graph.setdefault(place2, [])
        self.graph[place1].append((place2, distance))
        self.graph[place2].append((place1, distance))

    def display_map(self):
        print("\n--- City Map ---")
        for place, roads in self.graph.items():
            print(place, "->", roads)

    # Dijkstra's shortest path algorithm
    def shortest_path(self, start, destination):
        if start not in self.graph or destination not in self.graph:
            print("Location not found.")
            return

        distances = {place: float("inf") for place in self.graph}
        previous = {}
        distances[start] = 0
        queue = [(0, start)]

        while queue:
            distance, current = heapq.heappop(queue)

            if distance > distances[current]:
                continue

            if current == destination:
                break

            for neighbor, weight in self.graph[current]:
                new_distance = distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current
                    heapq.heappush(queue, (new_distance, neighbor))

        if distances[destination] == float("inf"):
            print("No route available.")
            return

        path = []
        current = destination

        while current != start:
            path.append(current)
            current = previous[current]

        path.append(start)
        path.reverse()

        print("Shortest route:", " -> ".join(path))
        print("Total distance:", distances[destination], "km")

    # Breadth-First Search
    def bfs(self, start):
        if start not in self.graph:
            print("Location not found.")
            return

        visited = {start}
        queue = deque([start])

        print("BFS traversal:")

        while queue:
            current = queue.popleft()
            print(current, end=" ")

            for neighbor, _ in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print()


# Create a sample city map
city = CityMap()

city.add_road("Home", "Market", 4)
city.add_road("Home", "College", 6)
city.add_road("Market", "Hospital", 3)
city.add_road("Market", "College", 2)
city.add_road("College", "Hospital", 5)
city.add_road("Hospital", "Airport", 8)
city.add_road("College", "Airport", 10)

# Menu-driven application
while True:
    print("\n--- GPS Navigation System ---")
    print("1. Display City Map")
    print("2. Find Shortest Route")
    print("3. BFS Traversal")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        city.display_map()

    elif choice == "2":
        start = input("Enter starting location: ").strip()
        destination = input("Enter destination: ").strip()
        city.shortest_path(start, destination)

    elif choice == "3":
        start = input("Enter starting location: ").strip()
        city.bfs(start)

    elif choice == "4":
        print("Thank you for using GPS Navigation!")
        break

    else:
        print("Invalid choice. Try again.")
