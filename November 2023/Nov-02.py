class Solution:
    def minDist(self, arr, n, x, y):
        # Initialize variables to store the indices of the last occurrences of x and y.
        last_x_index = -1
        last_y_index = -1
        min_distance = float('inf')

        for i in range(n):
            if arr[i] == x:
                # If x is found, update its last index.
                last_x_index = i
                # If y has been found before, calculate the distance and update min_distance.
                if last_y_index != -1:
                    min_distance = min(min_distance, abs(last_x_index - last_y_index))
            elif arr[i] == y:
                # If y is found, update its last index.
                last_y_index = i
                # If x has been found before, calculate the distance and update min_distance.
                if last_x_index != -1:
                    min_distance = min(min_distance, abs(last_y_index - last_x_index))

        # Check if both x and y were found in the array.
        if last_x_index == -1 or last_y_index == -1:
            return -1

        return min_distance