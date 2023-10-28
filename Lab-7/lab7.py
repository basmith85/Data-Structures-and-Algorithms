class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        bucket_index = self._hash_function(key)
        for item in self.hash_table[bucket_index]:
            if item[0] == key:
                item[1] = value
                return
        self.hash_table[bucket_index].append([key, value])

    def get(self, key) -> int:
        bucket_index = self._hash_function(key)
        for item in self.hash_table[bucket_index]:
            if item[0] == key:
                return item[1]
        return 0
    
    def remove(self, key, value):
        bucket_index = self._hash_function(key)
        for item in self.hash_table[bucket_index]:
            if item[0] == key and item[1] == value:
                self.hash_table[bucket_index].remove(item)

    def display(self) -> list[list]:
        displayed = []
        for bucket in self.hash_table:
            for item in bucket:
                displayed.append(item)
        return displayed
    
    def max_passengers_in_flight(self, flight_number):
        max_trip_id = None
        max_passengers = 0

        bucket_index = self._hash_function(flight_number)
        for item in self.hash_table[bucket_index]:
            if item[0] == flight_number:
                passengers = int(item[1].passengers)
                if passengers > max_passengers:
                    max_passengers = passengers
                    max_trip_id = item[1].trip_id 
        return max_trip_id, max_passengers


    
class FlightNode:
    def __init__(self, flight_number, trip_id, passengers):
        self.flight_number = flight_number
        self.trip_id = trip_id
        self.passengers = passengers



# Display the hash map
my_hash_map = HashMap(7)
0, 1, 4, 9, 16, 25, 36, 49, 64, 81
my_hash_map.put("aaa", 0)
my_hash_map.put("bbb", 1)
my_hash_map.put("ccc", 4)
my_hash_map.put("ddd", 9)
my_hash_map.put("eee", 16)
my_hash_map.put("fff", 25)
my_hash_map.put("ggg", 36)
my_hash_map.put("hhh", 49)
my_hash_map.put("ccc", 64)
my_hash_map.put("ccc", 81)
my_hash_map.display()  

# Retrieve values
print("Retrieve values:")
print("aaa:", my_hash_map.get("aaa"))  
print("bbb:", my_hash_map.get("bbb"))
print("ccc:", my_hash_map.get("ccc"))

# Remove a key-value pair
my_hash_map.remove("bbb", 1)  

# Display the updated hash map
my_hash_map.display() 

#Max Passengers on Trip
my_map = HashMap(11)
# Add flight nodes (flight_number, trip_id, passengers)
my_map.put(16, FlightNode(16, "Trip 1", 300))
my_map.put(16, FlightNode(16, "Trip 2", 700))
my_map.put(29, FlightNode(29, "Trip 1", 800))
my_map.put(29, FlightNode(29, "Trip 2", 250))
my_map.put(36, FlightNode(29, "Trip 3", 500))
my_map.put(36, FlightNode(36, "Trip 1", 500))
my_map.put(36, FlightNode(36, "Trip 2", 340))
my_map.put(36, FlightNode(36, "Trip 3", 900))
my_map.put(36, FlightNode(36, "Trip 4", 400))
my_map.put(49, FlightNode(49, "Trip 1", 250))
my_map.put(49, FlightNode(49, "Trip 2", 550))

max_passengers = my_map.max_passengers_in_flight(49)
if max_passengers is not None:
    print("Largest number of people in flight at once :", max_passengers)
else:
    print("Flight not found in the map")
