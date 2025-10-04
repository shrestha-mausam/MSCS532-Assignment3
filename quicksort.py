"""
Randomized Quicksort and Deterministic Quicksort Implementation
Author: Mausam 
"""

import random
import time
import numpy as np
from typing import List, Tuple, Callable


class QuicksortAnalyzer:
    """Implementation and analysis of Randomized and Deterministic Quicksort algorithms."""
    
    def __init__(self):
        self.comparison_count = 0
        self.swap_count = 0
    
    def reset_counts(self):
        """Reset comparison and swap counters."""
        self.comparison_count = 0
        self.swap_count = 0
    
    def partition(self, arr: List[int], low: int, high: int, pivot_index: int) -> int:
        """
        Partition the array around the pivot element.
        
        Args:
            arr: The array to partition
            low: Starting index
            high: Ending index
            pivot_index: Index of the pivot element
            
        Returns:
            Final position of the pivot element
        """
        # Move pivot to the end
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        self.swap_count += 1
        
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            self.comparison_count += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.swap_count += 1
        
        # Move pivot to its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.swap_count += 1
        
        return i + 1
    
    def randomized_quicksort(self, arr: List[int], low: int = None, high: int = None) -> None:
        """
        Randomized Quicksort implementation.
        Pivot is chosen uniformly at random from the subarray.
        
        Args:
            arr: Array to sort
            low: Starting index (default: 0)
            high: Ending index (default: len(arr) - 1)
        """
        if low is None:
            low = 0
        if high is None:
            high = len(arr) - 1
        
        if low < high:
            # Choose random pivot
            pivot_index = random.randint(low, high)
            
            # Partition around the pivot
            pivot_pos = self.partition(arr, low, high, pivot_index)
            
            # Recursively sort elements before and after partition
            self.randomized_quicksort(arr, low, pivot_pos - 1)
            self.randomized_quicksort(arr, pivot_pos + 1, high)
    
    def deterministic_quicksort(self, arr: List[int], low: int = None, high: int = None) -> None:
        """
        Deterministic Quicksort implementation.
        Pivot is always the first element.
        
        Args:
            arr: Array to sort
            low: Starting index (default: 0)
            high: Ending index (default: len(arr) - 1)
        """
        if low is None:
            low = 0
        if high is None:
            high = len(arr) - 1
        
        # Use iterative approach to avoid recursion depth issues
        stack = [(low, high)]
        
        while stack:
            low, high = stack.pop()
            
            if low < high:
                # Choose first element as pivot
                pivot_index = low
                
                # Partition around the pivot
                pivot_pos = self.partition(arr, low, high, pivot_index)
                
                # Add subarrays to stack (process larger subarray first to limit stack size)
                if pivot_pos - 1 - low > high - pivot_pos - 1:
                    stack.append((low, pivot_pos - 1))
                    stack.append((pivot_pos + 1, high))
                else:
                    stack.append((pivot_pos + 1, high))
                    stack.append((low, pivot_pos - 1))
    
    def measure_performance(self, arr: List[int], sort_func: Callable) -> Tuple[float, int, int]:
        """
        Measure the performance of a sorting function.
        
        Args:
            arr: Array to sort (will be copied)
            sort_func: The sorting function to test
            
        Returns:
            Tuple of (execution_time, comparisons, swaps)
        """
        # Create a copy to avoid modifying the original array
        test_arr = arr.copy()
        
        # Reset counters
        self.reset_counts()
        
        # Measure execution time
        start_time = time.time()
        sort_func(test_arr)
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        return execution_time, self.comparison_count, self.swap_count
    
    def generate_test_data(self, size: int, data_type: str) -> List[int]:
        """
        Generate test data of various types.
        
        Args:
            size: Size of the array
            data_type: Type of data ('random', 'sorted', 'reverse', 'duplicates')
            
        Returns:
            Generated array
        """
        if data_type == 'random':
            return [random.randint(1, size) for _ in range(size)]
        elif data_type == 'sorted':
            return list(range(1, size + 1))
        elif data_type == 'reverse':
            return list(range(size, 0, -1))
        elif data_type == 'duplicates':
            return [random.randint(1, 10) for _ in range(size)]
        else:
            raise ValueError(f"Unknown data type: {data_type}")
    
    def run_performance_comparison(self, sizes: List[int], data_types: List[str], iterations: int = 5) -> dict:
        """
        Run comprehensive performance comparison between randomized and deterministic quicksort.
        
        Args:
            sizes: List of array sizes to test
            data_types: List of data types to test
            iterations: Number of iterations per test case
            
        Returns:
            Dictionary containing performance results
        """
        results = {
            'randomized': {},
            'deterministic': {}
        }
        
        for size in sizes:
            results['randomized'][size] = {}
            results['deterministic'][size] = {}
            
            for data_type in data_types:
                results['randomized'][size][data_type] = {
                    'times': [], 'comparisons': [], 'swaps': []
                }
                results['deterministic'][size][data_type] = {
                    'times': [], 'comparisons': [], 'swaps': []
                }
                
                for _ in range(iterations):
                    # Generate test data
                    test_data = self.generate_test_data(size, data_type)
                    
                    # Test randomized quicksort
                    time_r, comp_r, swap_r = self.measure_performance(
                        test_data, self.randomized_quicksort
                    )
                    results['randomized'][size][data_type]['times'].append(time_r)
                    results['randomized'][size][data_type]['comparisons'].append(comp_r)
                    results['randomized'][size][data_type]['swaps'].append(swap_r)
                    
                    # Test deterministic quicksort
                    time_d, comp_d, swap_d = self.measure_performance(
                        test_data, self.deterministic_quicksort
                    )
                    results['deterministic'][size][data_type]['times'].append(time_d)
                    results['deterministic'][size][data_type]['comparisons'].append(comp_d)
                    results['deterministic'][size][data_type]['swaps'].append(swap_d)
        
        return results
    
    def print_results(self, results: dict):
        """Print formatted performance results."""
        print("=" * 80)
        print("QUICKSORT PERFORMANCE COMPARISON")
        print("=" * 80)
        
        for size in results['randomized'].keys():
            print(f"\nArray Size: {size}")
            print("-" * 40)
            
            for data_type in results['randomized'][size].keys():
                print(f"\nData Type: {data_type.upper()}")
                
                # Calculate averages
                rand_times = results['randomized'][size][data_type]['times']
                det_times = results['deterministic'][size][data_type]['times']
                rand_comps = results['randomized'][size][data_type]['comparisons']
                det_comps = results['deterministic'][size][data_type]['comparisons']
                rand_swaps = results['randomized'][size][data_type]['swaps']
                det_swaps = results['deterministic'][size][data_type]['swaps']
                
                print(f"Randomized Quicksort:")
                print(f"  Avg Time: {np.mean(rand_times):.6f}s")
                print(f"  Avg Comparisons: {np.mean(rand_comps):.0f}")
                print(f"  Avg Swaps: {np.mean(rand_swaps):.0f}")
                
                print(f"Deterministic Quicksort:")
                print(f"  Avg Time: {np.mean(det_times):.6f}s")
                print(f"  Avg Comparisons: {np.mean(det_comps):.0f}")
                print(f"  Avg Swaps: {np.mean(det_swaps):.0f}")
                
                # Calculate improvement
                time_improvement = (np.mean(det_times) - np.mean(rand_times)) / np.mean(det_times) * 100
                comp_improvement = (np.mean(det_comps) - np.mean(rand_comps)) / np.mean(det_comps) * 100
                
                print(f"Randomized vs Deterministic:")
                print(f"  Time Improvement: {time_improvement:.2f}%")
                print(f"  Comparison Improvement: {comp_improvement:.2f}%")


def main():
    """Main function to demonstrate the quicksort implementations."""
    analyzer = QuicksortAnalyzer()
    
    # Test with small arrays first
    print("Testing Quicksort Implementations")
    print("=" * 50)
    
    # Test cases
    test_cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6], "Unsorted array"),
        ([1, 2, 3, 4, 5], "Sorted array"),
        ([5, 4, 3, 2, 1], "Reverse sorted array"),
        ([1, 1, 1, 1, 1], "Array with duplicates"),
        ([42], "Single element"),
        ([], "Empty array")
    ]
    
    for test_array, description in test_cases:
        print(f"\n{description}: {test_array}")
        
        # Test randomized quicksort
        rand_arr = test_array.copy()
        analyzer.randomized_quicksort(rand_arr)
        print(f"Randomized Quicksort: {rand_arr}")
        
        # Test deterministic quicksort
        det_arr = test_array.copy()
        analyzer.deterministic_quicksort(det_arr)
        print(f"Deterministic Quicksort: {det_arr}")
    
    # Performance comparison
    print("\n" + "=" * 50)
    print("PERFORMANCE COMPARISON")
    print("=" * 50)
    
    sizes = [100, 500, 1000, 2000]
    data_types = ['random', 'sorted', 'reverse', 'duplicates']
    
    results = analyzer.run_performance_comparison(sizes, data_types, iterations=3)
    analyzer.print_results(results)


if __name__ == "__main__":
    main()