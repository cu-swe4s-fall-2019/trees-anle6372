# trees

## Running
    - Include bits that explain how to initalize submodules

## Creation
    - Added hash-tables-anle6372 as submodule
    - Added avl_tree as submodule
    - Created README.md file
    - Created .travis.yml file

## binary_tree.py
    - Created testing file test_binary_tree.py
    - Created add, search functions with appropriate testing framework

## insert_key_value_pairs.py

### Benchmarking Results
    Using the random list, 1000 entries
    - Binary Tree yielded:
        + Add time of 0.089 seconds
        + Search time for real keys of 0.0042 seconds
        + Search time for nonreal keys of 0.0057 seconds
    - AVL Tree yielded:
        + Add time of 0.23 seconds
        + Search time for real keys of 0.0033 seconds
        + Search time for nonreal keys of 0.0051 seconds
    - Hash Table yielded:
        + Add time of 0.048 seconds
        + Search time for real keys of 0.0039 seconds
        + Search time for nonreal keys of 0.005 seconds
        
    Using the sorted list, 1000 entries
    - Binary Tree yielded:
        Would not work due to recursion limit issues
    - AVL Tree yielded:
        + Add time of 0.237 seconds
        + Search time for real keys of 0.0033 seconds
        + Search time for nonreal keys of 0.0041 seconds
    - Hash Table yielded:
        + Add time of 0.040 seconds
        + Search time for real keys of 0.0026 seconds
        + Search time for nonreal keys of 0.0036 seconds.