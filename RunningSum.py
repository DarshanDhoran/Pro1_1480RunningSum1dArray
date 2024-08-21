class Solution(object):
    def runningSum(self, nums):
        running_sum = []  # Initialize an empty list to store the running sums
        current_sum = 0   # Initialize a variable to keep track of the cumulative sum
        
        for num in nums:  # Iterate through each number in the input list
            current_sum += num  # Add the current number to the cumulative sum
            running_sum.append(current_sum)  # Append the cumulative sum to the list
        
        return running_sum  # Return the list containing the running sums

# Example usage:
solution = Solution()  # Create an instance of the Solution class
nums = [1, 2, 3, 4]  # Example input
print(solution.runningSum(nums))  # Call the method and print the result
