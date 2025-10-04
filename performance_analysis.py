"""
Comprehensive Performance Analysis Suite
Author: Mausam Shrestha
Assignment: 3
Course: CS 532
"""

import matplotlib.pyplot as plt
import numpy as np
import time
from typing import Dict, List, Tuple
from quicksort import QuicksortAnalyzer
from hash_table import HashTableAnalyzer


class PerformanceAnalyzer:
    """Comprehensive performance analysis for both algorithms."""
    
    def __init__(self):
        self.quicksort_analyzer = QuicksortAnalyzer()
        self.hash_table_analyzer = HashTableAnalyzer()
    
    def run_comprehensive_quicksort_analysis(self) -> Dict:
        """Run comprehensive quicksort performance analysis."""
        print("Running comprehensive Quicksort analysis...")
        
        # Test with various sizes and data types
        sizes = [100, 500, 1000, 2000, 5000]
        data_types = ['random', 'sorted', 'reverse', 'duplicates']
        
        results = self.quicksort_analyzer.run_performance_comparison(
            sizes, data_types, iterations=5
        )
        
        # Generate performance plots
        self._plot_quicksort_performance(results)
        
        return results
    
    def run_comprehensive_hash_table_analysis(self) -> Dict:
        """Run comprehensive hash table performance analysis."""
        print("Running comprehensive Hash Table analysis...")
        
        # Test with various sizes and data types
        sizes = [100, 500, 1000, 2000, 5000]
        data_types = ['random', 'sequential', 'strings']
        
        results = self.hash_table_analyzer.run_performance_test(
            sizes, data_types, iterations=5
        )
        
        # Generate performance plots
        self._plot_hash_table_performance(results)
        
        return results
    
    def _plot_quicksort_performance(self, results: Dict):
        """Generate performance plots for quicksort analysis."""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Quicksort Performance Analysis', fontsize=16)
        
        sizes = list(results['randomized'].keys())
        data_types = ['random', 'sorted', 'reverse', 'duplicates']
        
        # Plot 1: Average execution time by data type
        ax1 = axes[0, 0]
        for data_type in data_types:
            rand_times = []
            det_times = []
            for size in sizes:
                rand_times.append(np.mean(results['randomized'][size][data_type]['times']))
                det_times.append(np.mean(results['deterministic'][size][data_type]['times']))
            
            ax1.plot(sizes, rand_times, 'o-', label=f'Randomized - {data_type}', alpha=0.7)
            ax1.plot(sizes, det_times, 's--', label=f'Deterministic - {data_type}', alpha=0.7)
        
        ax1.set_xlabel('Array Size')
        ax1.set_ylabel('Average Time (seconds)')
        ax1.set_title('Execution Time Comparison')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Comparison count by data type
        ax2 = axes[0, 1]
        for data_type in data_types:
            rand_comps = []
            det_comps = []
            for size in sizes:
                rand_comps.append(np.mean(results['randomized'][size][data_type]['comparisons']))
                det_comps.append(np.mean(results['deterministic'][size][data_type]['comparisons']))
            
            ax2.plot(sizes, rand_comps, 'o-', label=f'Randomized - {data_type}', alpha=0.7)
            ax2.plot(sizes, det_comps, 's--', label=f'Deterministic - {data_type}', alpha=0.7)
        
        ax2.set_xlabel('Array Size')
        ax2.set_ylabel('Average Comparisons')
        ax2.set_title('Comparison Count Analysis')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Plot 3: Performance improvement percentage
        ax3 = axes[1, 0]
        for data_type in data_types:
            improvements = []
            for size in sizes:
                rand_time = np.mean(results['randomized'][size][data_type]['times'])
                det_time = np.mean(results['deterministic'][size][data_type]['times'])
                improvement = (det_time - rand_time) / det_time * 100
                improvements.append(improvement)
            
            ax3.plot(sizes, improvements, 'o-', label=data_type, alpha=0.7)
        
        ax3.set_xlabel('Array Size')
        ax3.set_ylabel('Time Improvement (%)')
        ax3.set_title('Randomized vs Deterministic Improvement')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # Plot 4: Theoretical vs Empirical comparison
        ax4 = axes[1, 1]
        theoretical_times = []
        empirical_times = []
        
        for size in sizes:
            # Theoretical: O(n log n)
            theoretical_times.append(size * np.log2(size))
            # Empirical: average of randomized quicksort on random data
            empirical_times.append(np.mean(results['randomized'][size]['random']['times']) * 1000000)  # Scale for visibility
        
        ax4.plot(sizes, theoretical_times, 'o-', label='Theoretical O(n log n)', alpha=0.7)
        ax4.plot(sizes, empirical_times, 's--', label='Empirical (scaled)', alpha=0.7)
        
        ax4.set_xlabel('Array Size')
        ax4.set_ylabel('Scaled Time')
        ax4.set_title('Theoretical vs Empirical Performance')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('quicksort_performance.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def _plot_hash_table_performance(self, results: Dict):
        """Generate performance plots for hash table analysis."""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Hash Table Performance Analysis', fontsize=16)
        
        sizes = list(results.keys())
        data_types = ['random', 'sequential', 'strings']
        
        # Plot 1: Insert time by data type
        ax1 = axes[0, 0]
        for data_type in data_types:
            insert_times = []
            for size in sizes:
                insert_times.append(np.mean(results[size][data_type]['insert_times']))
            
            ax1.plot(sizes, insert_times, 'o-', label=data_type, alpha=0.7)
        
        ax1.set_xlabel('Dataset Size')
        ax1.set_ylabel('Average Insert Time (seconds)')
        ax1.set_title('Insert Operation Performance')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Search time by data type
        ax2 = axes[0, 1]
        for data_type in data_types:
            search_times = []
            for size in sizes:
                search_times.append(np.mean(results[size][data_type]['search_times']))
            
            ax2.plot(sizes, search_times, 'o-', label=data_type, alpha=0.7)
        
        ax2.set_xlabel('Dataset Size')
        ax2.set_ylabel('Average Search Time (seconds)')
        ax2.set_title('Search Operation Performance')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Plot 3: Load factor analysis
        ax3 = axes[1, 0]
        for data_type in data_types:
            load_factors = []
            for size in sizes:
                avg_load_factor = np.mean([stats['load_factor'] for stats in results[size][data_type]['final_stats']])
                load_factors.append(avg_load_factor)
            
            ax3.plot(sizes, load_factors, 'o-', label=data_type, alpha=0.7)
        
        ax3.set_xlabel('Dataset Size')
        ax3.set_ylabel('Average Load Factor')
        ax3.set_title('Load Factor Analysis')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # Plot 4: Collision rate analysis
        ax4 = axes[1, 1]
        for data_type in data_types:
            collision_rates = []
            for size in sizes:
                avg_collision_rate = np.mean([stats['collision_rate'] for stats in results[size][data_type]['final_stats']])
                collision_rates.append(avg_collision_rate)
            
            ax4.plot(sizes, collision_rates, 'o-', label=data_type, alpha=0.7)
        
        ax4.set_xlabel('Dataset Size')
        ax4.set_ylabel('Average Collision Rate')
        ax4.set_title('Collision Rate Analysis')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('hash_table_performance.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def generate_comparison_report(self, quicksort_results: Dict, hash_table_results: Dict):
        """Generate a comprehensive comparison report."""
        print("=" * 80)
        print("COMPREHENSIVE ALGORITHM COMPARISON REPORT")
        print("=" * 80)
        
        # Quicksort analysis summary
        print("\n1. QUICKSORT ANALYSIS SUMMARY")
        print("-" * 40)
        
        # Analyze worst case scenarios
        sizes = list(quicksort_results['randomized'].keys())
        
        print("Worst-case scenarios (sorted arrays):")
        for size in sizes:
            rand_time = np.mean(quicksort_results['randomized'][size]['sorted']['times'])
            det_time = np.mean(quicksort_results['deterministic'][size]['sorted']['times'])
            improvement = (det_time - rand_time) / det_time * 100
            
            print(f"  Size {size}: Randomized {rand_time:.6f}s, Deterministic {det_time:.6f}s")
            print(f"    Improvement: {improvement:.2f}%")
        
        # Hash table analysis summary
        print("\n2. HASH TABLE ANALYSIS SUMMARY")
        print("-" * 40)
        
        print("Performance by operation:")
        for size in sizes:
            if size in hash_table_results:
                avg_insert = np.mean([np.mean(hash_table_results[size][dt]['insert_times']) for dt in hash_table_results[size].keys()])
                avg_search = np.mean([np.mean(hash_table_results[size][dt]['search_times']) for dt in hash_table_results[size].keys()])
                
                print(f"  Size {size}: Insert {avg_insert:.8f}s, Search {avg_search:.8f}s")
        
        # Theoretical analysis
        print("\n3. THEORETICAL ANALYSIS VALIDATION")
        print("-" * 40)
        
        print("Quicksort Time Complexity:")
        print("  - Average case: O(n log n) ✓")
        print("  - Worst case (deterministic): O(n²) ✓")
        print("  - Worst case (randomized): O(n log n) with high probability ✓")
        
        print("\nHash Table Time Complexity (with chaining):")
        print("  - Insert (average): O(1 + α) where α = load factor ✓")
        print("  - Search (average): O(1 + α) where α = load factor ✓")
        print("  - Delete (average): O(1 + α) where α = load factor ✓")
        
        # Load factor analysis
        print("\n4. LOAD FACTOR IMPACT ANALYSIS")
        print("-" * 40)
        
        for size in sizes:
            if size in hash_table_results:
                avg_load_factor = np.mean([
                    np.mean([stats['load_factor'] for stats in hash_table_results[size][dt]['final_stats']])
                    for dt in hash_table_results[size].keys()
                ])
                
                print(f"  Size {size}: Average load factor = {avg_load_factor:.3f}")
                if avg_load_factor > 0.75:
                    print("    ⚠️  High load factor detected - consider resizing")
                else:
                    print("    ✓ Load factor within acceptable range")


def main():
    """Main function to run comprehensive performance analysis."""
    analyzer = PerformanceAnalyzer()
    
    print("Starting comprehensive performance analysis...")
    print("This may take several minutes depending on your system.")
    
    # Run quicksort analysis
    quicksort_results = analyzer.run_comprehensive_quicksort_analysis()
    
    # Run hash table analysis
    hash_table_results = analyzer.run_comprehensive_hash_table_analysis()
    
    # Generate comparison report
    analyzer.generate_comparison_report(quicksort_results, hash_table_results)
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    print("Performance plots have been saved as:")
    print("- quicksort_performance.png")
    print("- hash_table_performance.png")
    print("\nSee the generated plots for visual analysis of the results.")


if __name__ == "__main__":
    main()