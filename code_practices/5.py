def min_swaps_to_sort(arr):
    n = len(arr)
    visited = [False] * n  # To keep track of visited elements
    index_map = {val: i for i, val in enumerate(arr)}  # Map value to index
    swaps = 0

    for i in range(n):
        # If already visited or in the correct position, continue
        if visited[i] or arr[i] == i + 1:
            continue
        
        # Find cycle size
        cycle_size = 0
        x = i

        while not visited[x]:
            visited[x] = True
            x = index_map[x + 1]  # Move to the index where the correct number should be
            cycle_size += 1
        
        # If cycle_size > 1, we need (cycle_size - 1) swaps
        if cycle_size > 1:
            swaps += (cycle_size - 1)

    return swaps

# Example usage:
n = int(input())  # Read N
arr = list(map(int, input().split()))  # Read the permutation
print(min_swaps_to_sort(arr))
