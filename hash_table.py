"""
Hash Table with Chaining Implementation
Author: Mausam Shrestha
Assignment: 3
Course: CS 532
"""

import random
import time
import math
from typing import List, Optional, Tuple, Any
import numpy as np


class HashNode:
    """Node for the linked list in chaining."""
    
    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.next = None


class UniversalHashTable:
    """
    Hash table implementation using chaining for collision resolution.
    Uses universal hashing to minimize collisions.
    """
    
    def __init__(self, initial_size: int = 11):
        """
        Initialize hash table with chaining.
        
        Args:
            initial_size: Initial size of the hash table (should be prime)
        """
        self.size = initial_size
        self.count = 0
        self.table: List[Optional[HashNode]] = [None] * self.size
        
        # Universal hash function parameters
        # h(k) = ((a * k + b) mod p) mod m
        # where p is a large prime > max key, a ∈ [1, p-1], b ∈ [0, p-1]
        self.p = self._find_next_prime(2 * self.size)  # p > m
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
        
        # Performance counters
        self.access_count = 0
        self.collision_count = 0
    
    def _find_next_prime(self, n: int) -> int:
        """Find the next prime number greater than or equal to n."""
        if n <= 2:
            return 2
        
        # Make sure n is odd
        if n % 2 == 0:
            n += 1
        
        while not self._is_prime(n):
            n += 2
        
        return n
    
    def _is_prime(self, n: int) -> bool:
        """Check if a number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        
        return True
    
    def _hash(self, key: Any) -> int:
        """
        Universal hash function.
        
        Args:
            key: The key to hash
            
        Returns:
            Hash index
        """
        # Convert key to integer if it's not already
        if isinstance(key, str):
            key_int = sum(ord(c) for c in key)
        elif isinstance(key, (int, float)):
            key_int = int(key)
        else:
            key_int = hash(key)
        
        # Ensure key is positive
        key_int = abs(key_int)
        
        # Universal hash function: ((a * k + b) mod p) mod m
        hash_value = ((self.a * key_int + self.b) % self.p) % self.size
        
        return hash_value
    
    def _get_load_factor(self) -> float:
        """Calculate the current load factor."""
        return self.count / self.size
    
    def _resize_table(self, new_size: int):
        """
        Resize the hash table to a new size.
        
        Args:
            new_size: New size for the hash table
        """
        old_table = self.table
        old_size = self.size
        
        # Create new table
        self.size = new_size
        self.table = [None] * self.size
        self.count = 0
        
        # Update hash function parameters
        self.p = self._find_next_prime(2 * self.size)
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
        
        # Rehash all elements
        for i in range(old_size):
            current = old_table[i]
            while current is not None:
                self.insert(current.key, current.value)
                current = current.next
    
    def insert(self, key: Any, value: Any) -> bool:
        """
        Insert a key-value pair into the hash table.
        
        Args:
            key: The key
            value: The value
            
        Returns:
            True if insertion was successful
        """
        # Check if we need to resize (load factor > 0.75)
        if self._get_load_factor() > 0.75:
            self._resize_table(self._find_next_prime(2 * self.size))
        
        hash_index = self._hash(key)
        self.access_count += 1
        
        # Check if key already exists
        current = self.table[hash_index]
        while current is not None:
            if current.key == key:
                current.value = value  # Update existing key
                return True
            current = current.next
        
        # Insert new key-value pair
        new_node = HashNode(key, value)
        new_node.next = self.table[hash_index]
        self.table[hash_index] = new_node
        
        # Count collision if there was already a node at this index
        if new_node.next is not None:
            self.collision_count += 1
        
        self.count += 1
        return True
    
    def search(self, key: Any) -> Optional[Any]:
        """
        Search for a key in the hash table.
        
        Args:
            key: The key to search for
            
        Returns:
            The value associated with the key, or None if not found
        """
        hash_index = self._hash(key)
        self.access_count += 1
        
        current = self.table[hash_index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        
        return None
    
    def delete(self, key: Any) -> bool:
        """
        Delete a key-value pair from the hash table.
        
        Args:
            key: The key to delete
            
        Returns:
            True if deletion was successful, False if key not found
        """
        hash_index = self._hash(key)
        self.access_count += 1
        
        current = self.table[hash_index]
        previous = None
        
        while current is not None:
            if current.key == key:
                if previous is None:
                    # First node in the chain
                    self.table[hash_index] = current.next
                else:
                    previous.next = current.next
                
                self.count -= 1
                return True
            
            previous = current
            current = current.next
        
        return False
    
    def get_stats(self) -> dict:
        """
        Get performance statistics.
        
        Returns:
            Dictionary containing performance metrics
        """
        return {
            'size': self.size,
            'count': self.count,
            'load_factor': self._get_load_factor(),
            'access_count': self.access_count,
            'collision_count': self.collision_count,
            'collision_rate': self.collision_count / max(self.access_count, 1)
        }
    
    def display_table(self):
        """Display the current state of the hash table."""
        print(f"Hash Table (Size: {self.size}, Count: {self.count}, Load Factor: {self._get_load_factor():.3f})")
        print("=" * 60)
        
        for i in range(self.size):
            print(f"Index {i:2d}: ", end="")
            current = self.table[i]
            
            if current is None:
                print("Empty")
            else:
                elements = []
                while current is not None:
                    elements.append(f"({current.key}, {current.value})")
                    current = current.next
                print(" -> ".join(elements))


class HashTableAnalyzer:
    """Analyzer for hash table performance."""
    
    def __init__(self):
        self.operation_times = {'insert': [], 'search': [], 'delete': []}
    
    def measure_operation(self, operation_func, *args, **kwargs) -> Tuple[float, Any]:
        """
        Measure the time taken by an operation.
        
        Args:
            operation_func: The operation function to measure
            *args: Arguments for the operation
            **kwargs: Keyword arguments for the operation
            
        Returns:
            Tuple of (execution_time, result)
        """
        start_time = time.time()
        result = operation_func(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        return execution_time, result
    
    def generate_test_data(self, size: int, data_type: str) -> List[Tuple[Any, Any]]:
        """
        Generate test data for hash table operations.
        
        Args:
            size: Number of key-value pairs to generate
            data_type: Type of data ('random', 'sequential', 'strings')
            
        Returns:
            List of (key, value) tuples
        """
        if data_type == 'random':
            return [(random.randint(1, size * 2), random.randint(1, 1000)) for _ in range(size)]
        elif data_type == 'sequential':
            return [(i, f"value_{i}") for i in range(1, size + 1)]
        elif data_type == 'strings':
            return [(f"key_{i}", f"value_{i}") for i in range(size)]
        else:
            raise ValueError(f"Unknown data type: {data_type}")
    
    def run_performance_test(self, sizes: List[int], data_types: List[str], iterations: int = 5) -> dict:
        """
        Run comprehensive performance tests on hash table operations.
        
        Args:
            sizes: List of dataset sizes to test
            data_types: List of data types to test
            iterations: Number of iterations per test case
            
        Returns:
            Dictionary containing performance results
        """
        results = {}
        
        for size in sizes:
            results[size] = {}
            
            for data_type in data_types:
                results[size][data_type] = {
                    'insert_times': [],
                    'search_times': [],
                    'delete_times': [],
                    'final_stats': []
                }
                
                for _ in range(iterations):
                    # Create fresh hash table for each iteration
                    hash_table = UniversalHashTable()
                    
                    # Generate test data
                    test_data = self.generate_test_data(size, data_type)
                    
                    # Test insertions
                    insert_times = []
                    for key, value in test_data:
                        time_taken, _ = self.measure_operation(hash_table.insert, key, value)
                        insert_times.append(time_taken)
                    
                    results[size][data_type]['insert_times'].append(np.mean(insert_times))
                    
                    # Test searches (search for half the keys)
                    search_times = []
                    search_keys = [key for key, _ in test_data[:size//2]]
                    for key in search_keys:
                        time_taken, _ = self.measure_operation(hash_table.search, key)
                        search_times.append(time_taken)
                    
                    results[size][data_type]['search_times'].append(np.mean(search_times))
                    
                    # Test deletions (delete quarter of the keys)
                    delete_times = []
                    delete_keys = [key for key, _ in test_data[:size//4]]
                    for key in delete_keys:
                        time_taken, _ = self.measure_operation(hash_table.delete, key)
                        delete_times.append(time_taken)
                    
                    results[size][data_type]['delete_times'].append(np.mean(delete_times))
                    
                    # Store final statistics
                    results[size][data_type]['final_stats'].append(hash_table.get_stats())
        
        return results
    
    def print_results(self, results: dict):
        """Print formatted performance results."""
        print("=" * 80)
        print("HASH TABLE PERFORMANCE ANALYSIS")
        print("=" * 80)
        
        for size in results.keys():
            print(f"\nDataset Size: {size}")
            print("-" * 40)
            
            for data_type in results[size].keys():
                print(f"\nData Type: {data_type.upper()}")
                
                # Calculate averages
                insert_times = results[size][data_type]['insert_times']
                search_times = results[size][data_type]['search_times']
                delete_times = results[size][data_type]['delete_times']
                final_stats = results[size][data_type]['final_stats']
                
                avg_load_factor = np.mean([stats['load_factor'] for stats in final_stats])
                avg_collision_rate = np.mean([stats['collision_rate'] for stats in final_stats])
                
                print(f"Average Insert Time: {np.mean(insert_times):.8f}s")
                print(f"Average Search Time: {np.mean(search_times):.8f}s")
                print(f"Average Delete Time: {np.mean(delete_times):.8f}s")
                print(f"Average Load Factor: {avg_load_factor:.3f}")
                print(f"Average Collision Rate: {avg_collision_rate:.3f}")


def main():
    """Main function to demonstrate the hash table implementation."""
    print("Testing Hash Table with Chaining")
    print("=" * 50)
    
    # Create hash table
    hash_table = UniversalHashTable(initial_size=7)
    
    # Test basic operations
    print("Testing basic operations:")
    
    # Insert some key-value pairs
    test_data = [
        (1, "apple"), (2, "banana"), (3, "cherry"), 
        (4, "date"), (5, "elderberry"), (11, "grape"),  # 11 will hash to same as 1
        (12, "honeydew")  # 12 will hash to same as 2
    ]
    
    print("\nInserting key-value pairs:")
    for key, value in test_data:
        hash_table.insert(key, value)
        print(f"Inserted ({key}, {value})")
    
    print(f"\nHash table after insertions:")
    hash_table.display_table()
    print(f"\nStatistics: {hash_table.get_stats()}")
    
    # Test search operations
    print("\nSearching for keys:")
    search_keys = [1, 3, 5, 11, 99]  # 99 doesn't exist
    for key in search_keys:
        value = hash_table.search(key)
        if value is not None:
            print(f"Key {key} found with value: {value}")
        else:
            print(f"Key {key} not found")
    
    # Test delete operations
    print("\nDeleting key 2:")
    if hash_table.delete(2):
        print("Key 2 deleted successfully")
    else:
        print("Key 2 not found for deletion")
    
    print(f"\nHash table after deletion:")
    hash_table.display_table()
    print(f"\nFinal statistics: {hash_table.get_stats()}")
    
    # Performance analysis
    print("\n" + "=" * 50)
    print("PERFORMANCE ANALYSIS")
    print("=" * 50)
    
    analyzer = HashTableAnalyzer()
    sizes = [100, 500, 1000]
    data_types = ['random', 'sequential', 'strings']
    
    results = analyzer.run_performance_test(sizes, data_types, iterations=3)
    analyzer.print_results(results)


if __name__ == "__main__":
    main()