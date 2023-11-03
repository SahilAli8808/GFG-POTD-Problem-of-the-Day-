#Pythagorean Triplet
class Solution:
    def checkTriplet(self, arr, n):
        # Square all elements in the array
        arr = [x * x for x in arr]
        
        # Find the maximum value in the squared array
        max_val = max(arr)
        
        # Create a set to store the squared values
        squared_set = set(arr)
        
        # Check for Pythagorean triplets
        for i in range(n):
            for j in range(i + 1, n):
                # Check if the sum of the squares of two elements is in the set
                if arr[i] + arr[j] in squared_set:
                    return True
        return False
