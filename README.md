# Merge two sorted arrays

## Question:
Two sorted arrays in ascending order. Create a merged array with both, sorted in ascending order. Repeated elements are allowed.

## Algorithm:

### Brute Force, as discussed
Loop through each array and add elements into another array, then sort it at the end. Not optimal!

### Optimal solution

Parse one array, loop through each element, using a three pointer approach
See if that element already exists in the second array.
If it exists, then push it in the first index of merged one.
If not, then push both the elements it to the index and index + 1 positions in the merged one - increment pointers accordingly
Then repeat the scanning for remainder of the elements in arr1 and arr2

## Examples:
arr1 = [1,2,3]; arr2 = [4,5,6]

Output --> [1,2,3,4,5,6]


arr1 = [1,3,4,5,6]
arr2 = [1,2,5,6]

Output --> [1,1,2,3,4,5,5,6,6]

## Execution

Clone the repo and change directory to root of repo before running `python main.py`
