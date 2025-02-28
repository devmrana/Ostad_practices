def find_triplet(arr, n, P):
    arr.sort()  # Step 1: Sort the array

    for i in range(n - 2):
        left, right = i + 1, n - 1  # Two-pointer approach
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == P:
                print(arr[i], arr[left], arr[right])
                return  # Since only one triplet is needed
            elif current_sum < P:
                left += 1  # Increase sum by moving left pointer
            else:
                right -= 1  # Decrease sum by moving right pointer
    
    print("No triplet found")  # If no valid triplet is found

# Input handling
n = int(input())  # Read N
arr = list(map(int, input().split()))  # Read the array
P = int(input())  # Read target sum P

find_triplet(arr, n, P)
