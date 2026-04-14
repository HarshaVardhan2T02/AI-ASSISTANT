"""
Lab 11 - Data Structures with AI: Implementing Fundamental Structures
Implementing all required data structures and system designs
"""

# ==================== TASK 1: STACK IMPLEMENTATION ====================
class Stack:
    """A Last-In-First-Out (LIFO) data structure."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)


# ==================== TASK 2: QUEUE IMPLEMENTATION ====================
class Queue:
    """A First-In-First-Out (FIFO) data structure."""
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def peek(self):
        """Return the front item without removing it."""
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)


# ==================== TASK 3: LINKED LIST IMPLEMENTATION ====================
class Node:
    """A node in a singly linked list."""
    
    def __init__(self, data):
        """Initialize a node with data."""
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list implementation."""
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
    
    def insert(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete(self, data):
        """Delete the first node with the specified data."""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self):
        """Print all elements in the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" → ".join(elements) if elements else "Empty List")
    
    def search(self, data):
        """Search for a node with the specified data."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


# ==================== TASK 4: HASH TABLE IMPLEMENTATION ====================
class HashTable:
    """A hash table with collision handling using chaining."""
    
    def __init__(self, size=10):
        """Initialize a hash table with specified size."""
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Generate hash value for a key."""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
    
    def search(self, key):
        """Search for a value by key."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]
    
    def display(self):
        """Display all key-value pairs in the hash table."""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# ==================== TASK 5: GRAPH IMPLEMENTATION ====================
class Graph:
    """A graph represented using an adjacency list."""
    
    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, u, v, weight=1):
        """Add an edge between two vertices."""
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append((v, weight))
    
    def display(self):
        """Display the graph connections."""
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")
    
    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex."""
        return self.graph.get(vertex, [])


# ==================== TASK 6: HOSPITAL MANAGEMENT SYSTEM ====================
"""
HOSPITAL MANAGEMENT SYSTEM - DATA STRUCTURE SELECTION

1. Patient Check-In System → QUEUE (Circular/Regular)
   Justification: Patients are treated in FIFO order. A queue ensures 
   fair treatment based on arrival time.

2. Emergency Case Handling → PRIORITY QUEUE
   Justification: Critical patients must be prioritized regardless of 
   arrival time. Priority queue handles urgent cases first.

3. Medical Records Storage → HASH TABLE
   Justification: Fast O(1) average retrieval of patient records using 
   unique patient ID as key.

4. Doctor Appointment Scheduling → BINARY SEARCH TREE (BST)
   Justification: Appointments can be sorted by time efficiently, allowing 
   quick insertion and retrieval in sorted order.

5. Hospital Room Navigation → GRAPH
   Justification: Wards and rooms form a network structure. Graph 
   representation allows pathfinding between locations.
"""

class PatientCheckIn:
    """Patient check-in system using Queue - TASK 6 Implementation."""
    
    def __init__(self):
        """Initialize the patient check-in queue."""
        self.queue = Queue()
        self.patient_id = 0
    
    def register_patient(self, name, age):
        """Register a new patient."""
        self.patient_id += 1
        patient = {"id": self.patient_id, "name": name, "age": age, "status": "Waiting"}
        self.queue.enqueue(patient)
        print(f"Patient {name} registered with ID {self.patient_id}")
    
    def call_next_patient(self):
        """Call the next patient for treatment."""
        if not self.queue.is_empty():
            patient = self.queue.dequeue()
            patient["status"] = "Being Treated"
            print(f"Calling Patient: {patient['name']} (ID: {patient['id']})")
            return patient
        print("No patients in queue")
        return None
    
    def display_queue(self):
        """Display all waiting patients."""
        print(f"Patients in queue: {self.queue.size()}")


# ==================== TASK 7: SMART CITY TRAFFIC CONTROL ====================
"""
TRAFFIC CONTROL SYSTEM - DATA STRUCTURE SELECTION

1. Traffic Signal Queue → QUEUE
   Justification: Vehicles wait in FIFO order at traffic signals. 
   Queue naturally represents this waiting mechanism.

2. Emergency Vehicle Priority Handling → PRIORITY QUEUE
   Justification: Ambulances and fire trucks get higher priority. 
   Priority queue processes urgent vehicles first.

3. Vehicle Registration Lookup → HASH TABLE
   Justification: O(1) lookup of vehicle details using registration 
   number as key for instant access.

4. Road Network Mapping → GRAPH
   Justification: Roads and intersections form a connected network. 
   Graphs efficiently represent this spatial relationship.

5. Parking Slot Availability → HASH TABLE or ARRAY
   Justification: Quick lookup and update of availability status 
   using parking slot ID as key.
"""

class TrafficSignalQueue:
    """Traffic signal queue system - TASK 7 Implementation."""
    
    def __init__(self, signal_id):
        """Initialize traffic signal with queue."""
        self.signal_id = signal_id
        self.queue = Queue()
        self.vehicle_count = 0
    
    def add_vehicle(self, vehicle_number):
        """Add vehicle to traffic signal queue."""
        self.vehicle_count += 1
        self.queue.enqueue({"id": self.vehicle_count, "number": vehicle_number})
        print(f"Vehicle {vehicle_number} added to signal {self.signal_id}")
    
    def allow_passage(self):
        """Allow next vehicle to pass."""
        if not self.queue.is_empty():
            vehicle = self.queue.dequeue()
            print(f"Vehicle {vehicle['number']} can pass signal {self.signal_id}")
            return vehicle
        print("No vehicles waiting")
        return None
    
    def get_waiting_count(self):
        """Get number of vehicles waiting."""
        return self.queue.size()


# ==================== TASK 8: E-COMMERCE PLATFORM ====================
"""
E-COMMERCE SYSTEM - DATA STRUCTURE SELECTION

1. Shopping Cart Management → LINKED LIST or DEQUE
   Justification: Dynamic addition/removal of products. Linked list 
   provides efficient insertion/deletion.

2. Order Processing System → QUEUE
   Justification: Orders processed in FIFO (First Come First Served). 
   Queue ensures fair sequential processing.

3. Top-Selling Products Tracker → MAX HEAP / PRIORITY QUEUE
   Justification: Products ranked by sales count. Priority queue 
   efficiently retrieves top sellers.

4. Product Search Engine → HASH TABLE
   Justification: O(1) lookup of products using product ID. Fast 
   retrieval for search queries.

5. Delivery Route Planning → GRAPH
   Justification: Warehouses and delivery locations form a network. 
   Graph enables route optimization algorithms.
"""

class ShoppingCart:
    """Shopping cart using Linked List - TASK 8 Implementation."""
    
    def __init__(self):
        """Initialize empty shopping cart."""
        self.cart = LinkedList()
        self.total_price = 0
    
    def add_product(self, product_name, price):
        """Add product to cart."""
        self.cart.insert_at_end({"name": product_name, "price": price})
        self.total_price += price
        print(f"Added {product_name} (${price}) to cart")
    
    def remove_product(self, product_name):
        """Remove product from cart."""
        self.cart.delete(product_name)
        print(f"Removed {product_name} from cart")
    
    def display_cart(self):
        """Display cart contents."""
        print("Shopping Cart Contents:")
        self.cart.display()
        print(f"Total: ${self.total_price}")


# ==================== DEMO/TESTING ====================
if __name__ == "__main__":
    print("=" * 60)
    print("DATA STRUCTURES DEMONSTRATION")
    print("=" * 60)
    
    # Test Hospital System
    print("\n--- Hospital Patient Check-In ---")
    hospital = PatientCheckIn()
    hospital.register_patient("John Doe", 45)
    hospital.register_patient("Jane Smith", 32)
    hospital.call_next_patient()
    hospital.display_queue()
    
    # Test Traffic System
    print("\n--- Traffic Signal Queue ---")
    signal = TrafficSignalQueue(1)
    signal.add_vehicle("ABC123")
    signal.add_vehicle("XYZ789")
    signal.allow_passage()
    print(f"Vehicles waiting: {signal.get_waiting_count()}")
    
    # Test E-Commerce Cart
    print("\n--- Shopping Cart ---")
    cart = ShoppingCart()
    cart.add_product("Laptop", 999)
    cart.add_product("Mouse", 25)
    cart.display_cart()