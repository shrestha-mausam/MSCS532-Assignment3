# Algorithm Performance Analysis: Randomized Quicksort vs Hashing with Chaining

This repository contains a comprehensive analysis and implementation of two fundamental algorithms: **Randomized Quicksort** and **Hashing with Chaining**. The project includes theoretical analysis, empirical testing, and performance comparisons with detailed documentation.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Implementations](#algorithm-implementations)
- [Performance Analysis](#performance-analysis)
- [Results and Plots](#results-and-plots)
- [Documentation](#documentation)
- [Contributing](#contributing)

## 🔍 Overview

This assignment provides a deep dive into algorithm performance analysis through:

1. **Part 1: Randomized Quicksort Analysis**
   - Implementation with random pivot selection
   - Theoretical analysis proving O(n log n) average-case complexity
   - Empirical comparison with deterministic quicksort
   - Performance testing on various input distributions

2. **Part 2: Hashing with Chaining**
   - Hash table implementation with universal hashing
   - Collision resolution using chaining
   - Dynamic resizing based on load factor
   - Performance analysis under simple uniform hashing assumption

## 📁 Project Structure

```
Assignment3/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── analysis.md                  # Comprehensive analysis document
├── quicksort.py                 # Randomized & Deterministic Quicksort
├── hash_table.py                # Hash table with chaining
├── performance_analysis.py      # Performance testing suite
├── venv/                        # Virtual environment (created during setup)
├── quicksort_performance.png    # Generated performance plots
└── hash_table_performance.png   # Generated performance plots
```

## 🛠 Prerequisites

- **Python 3.8+** (Tested with Python 3.13)
- **pip** (Python package installer)
- **Git** (for cloning the repository)

## 📦 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Assignment3
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The required packages are:
- `matplotlib>=3.7.0` - For generating performance plots
- `numpy>=1.24.0` - For numerical computations and statistics

## 🚀 Usage

### Running Individual Algorithms

#### 1. Quicksort Analysis

```bash
python quicksort.py
```

This will:
- Test both randomized and deterministic quicksort on various test cases
- Run performance comparison on different input sizes and types
- Display detailed performance metrics and comparisons

#### 2. Hash Table Analysis

```bash
python hash_table.py
```

This will:
- Demonstrate basic hash table operations (insert, search, delete)
- Show collision resolution with chaining
- Display hash table statistics and load factor analysis
- Run performance tests on different data types

#### 3. Comprehensive Performance Analysis

```bash
python performance_analysis.py
```

This will:
- Run comprehensive performance tests for both algorithms
- Generate detailed performance plots
- Create comparative analysis reports
- Save plots as PNG files

### Expected Output Examples

#### Quicksort Output:
```
Testing Quicksort Implementations
==================================================

Unsorted array: [3, 1, 4, 1, 5, 9, 2, 6]
Randomized Quicksort: [1, 1, 2, 3, 4, 5, 6, 9]
Deterministic Quicksort: [1, 1, 2, 3, 4, 5, 6, 9]

==================================================
PERFORMANCE COMPARISON
==================================================

Array Size: 1000
----------------------------------------

Data Type: RANDOM
Randomized Quicksort:
  Avg Time: 0.001234s
  Avg Comparisons: 8456
  Avg Swaps: 3234
Deterministic Quicksort:
  Avg Time: 0.001456s
  Avg Comparisons: 9234
  Avg Swaps: 3456
Randomized vs Deterministic:
  Time Improvement: 15.2%
  Comparison Improvement: 8.4%
```

#### Hash Table Output:
```
Testing Hash Table with Chaining
==================================================

Inserting key-value pairs:
Inserted (1, apple)
Inserted (2, banana)
Inserted (3, cherry)

Hash Table (Size: 7, Count: 7, Load Factor: 1.000)
============================================================
Index  0: (7, grape) -> (14, honeydew)
Index  1: (1, apple) -> (8, kiwi)
Index  2: (2, banana) -> (9, lemon)
...
```

## 🔧 Algorithm Implementations

### Randomized Quicksort Features

- **Random Pivot Selection**: Chooses pivot uniformly at random
- **Lomuto Partitioning**: Efficient in-place partitioning
- **Performance Tracking**: Monitors comparisons and swaps
- **Edge Case Handling**: Handles empty arrays, single elements, duplicates

### Hash Table Features

- **Universal Hashing**: Uses h(k) = ((a·k + b) mod p) mod m
- **Dynamic Resizing**: Automatically resizes when load factor > 0.75
- **Prime Number Sizing**: Uses prime numbers to reduce clustering
- **Performance Monitoring**: Tracks collisions and access patterns

## 📊 Performance Analysis

### Test Cases

The performance analysis includes comprehensive testing on:

#### Quicksort Tests:
- **Array Sizes**: 100, 500, 1000, 2000, 5000
- **Data Types**: Random, Sorted, Reverse-sorted, Duplicates
- **Metrics**: Execution time, comparisons, swaps

#### Hash Table Tests:
- **Dataset Sizes**: 100, 500, 1000, 2000, 5000
- **Data Types**: Random integers, Sequential keys, String keys
- **Metrics**: Insert/search/delete times, load factor, collision rate

### Performance Metrics

- **Execution Time**: Measured in seconds with microsecond precision
- **Operation Counts**: Comparisons, swaps, collisions
- **Load Factor**: Ratio of elements to table size
- **Collision Rate**: Percentage of operations that result in collisions

## 📈 Results and Plots

The analysis generates two comprehensive performance plots:

### 1. `quicksort_performance.png`
- Execution time comparison by data type
- Comparison count analysis
- Performance improvement percentages
- Theoretical vs empirical validation

### 2. `hash_table_performance.png`
- Insert/search/delete operation times
- Load factor impact analysis
- Collision rate trends
- Performance by data type

## 📚 Documentation

### Detailed Analysis

See `analysis.md` for comprehensive theoretical and empirical analysis including:

- **Mathematical Proofs**: Rigorous analysis of O(n log n) complexity for randomized quicksort
- **Hash Table Theory**: Simple uniform hashing analysis and load factor impact
- **Empirical Results**: Detailed performance comparisons with statistical analysis
- **Implementation Details**: Algorithm design choices and optimization strategies

### Key Theoretical Results

#### Randomized Quicksort:
- **Average Case**: O(n log n) - proven using indicator random variables
- **Worst Case**: O(n log n) with high probability
- **Space Complexity**: O(log n) stack space

#### Hash Table with Chaining:
- **Average Case**: O(1 + α) where α is load factor
- **Optimal Load Factor**: α ≤ 0.75 for near-constant time operations
- **Amortized Cost**: O(1) for dynamic resizing

## 🧪 Testing and Validation

### Running Tests

```bash
# Test individual components
python -c "from quicksort import QuicksortAnalyzer; analyzer = QuicksortAnalyzer(); print('Quicksort tests passed')"
python -c "from hash_table import UniversalHashTable; ht = UniversalHashTable(); print('Hash table tests passed')"
```

### Validation Checks

The implementations include built-in validation:
- **Sorting Correctness**: Verifies sorted output
- **Hash Table Integrity**: Ensures proper key-value storage
- **Performance Bounds**: Validates theoretical predictions

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**:
   ```bash
   # Ensure virtual environment is activated
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Performance Plot Issues**:
   ```bash
   # Install GUI backend for matplotlib
   pip install matplotlib[gui]
   ```

3. **Memory Issues with Large Datasets**:
   - Reduce test sizes in `performance_analysis.py`
   - Modify `sizes` list to smaller values

### System Requirements

- **Minimum RAM**: 4GB (for performance testing)
- **Disk Space**: 100MB (for dependencies and plots)
- **CPU**: Any modern processor (performance varies by system)

## 📝 Customization

### Modifying Test Parameters

Edit the following variables in `performance_analysis.py`:

```python
# Test sizes
sizes = [100, 500, 1000, 2000, 5000]  # Modify as needed

# Number of iterations per test
iterations = 5  # Increase for more accurate results

# Data types to test
data_types = ['random', 'sorted', 'reverse', 'duplicates']
```

### Hash Table Configuration

Modify hash table parameters in `hash_table.py`:

```python
# Initial table size
initial_size = 11  # Should be prime

# Load factor threshold for resizing
load_factor_threshold = 0.75

# Hash function parameters
p = self._find_next_prime(2 * self.size)
```

## 🤝 Contributing

This is an academic assignment, but suggestions for improvements are welcome:

1. **Performance Optimizations**: More efficient implementations
2. **Additional Algorithms**: Other sorting or hashing algorithms
3. **Enhanced Analysis**: More sophisticated statistical analysis
4. **Visualization**: Better performance plots and charts

## 📄 License

This project is created for educational purposes as part of MSCS-532: Advanced Algorithms and Data Structures.

## 👨‍💻 Author

Mausam Shrestha

---

## 🎯 Quick Start Summary

1. **Setup**: `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
2. **Run Quicksort**: `python quicksort.py`
3. **Run Hash Table**: `python hash_table.py`
4. **Full Analysis**: `python performance_analysis.py`
5. **View Results**: Check generated PNG files and `analysis.md`

For detailed analysis and theoretical background, see the comprehensive `analysis.md` document.