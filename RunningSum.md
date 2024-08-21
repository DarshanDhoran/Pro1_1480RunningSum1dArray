# Problem 1480: Running Sum of 1D Array

## Problem Statement

Given an array `nums`, we define the running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.

**Return** the running sum of `nums`.

### Example 1

**Input:** `nums = [1, 2, 3, 4]`  
**Output:** `[1, 3, 6, 10]`  
**Explanation:** Running sum is obtained as follows: `[1, 1+2, 1+2+3, 1+2+3+4]`.

### Example 2

**Input:** `nums = [1, 1, 1, 1, 1]`  
**Output:** `[1, 2, 3, 4, 5]`  
**Explanation:** Running sum is obtained as follows: `[1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1]`.

### Example 3

**Input:** `nums = [3, 1, 2, 10, 1]`  
**Output:** `[3, 4, 6, 16, 17]`  
**Explanation:** Running sum is obtained as follows: `[3, 3+1, 3+1+2, 3+1+2+10, 3+1+2+10+1]`.

### Constraints

- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`

## Solution Explanation

The solution takes a list of numbers and creates a new list where each number is the sum of all the numbers before it, including itself. This is called a "running sum."

### Steps to Implement the Solution

1. **Create a Blueprint (Class):**
   - The `Solution` class acts as a blueprint that defines how to calculate the running sum.

2. **Define the Task (Method):**
   - Inside this blueprint, a method called `runningSum` is defined. This method tells the computer how to add up the numbers one by one and keep track of the total as it goes.

3. **Start with a Clean Slate:**
   - The code initializes an empty list (like an empty notepad) where it will record each running total.
   - It also keeps a total that starts at zero.

4. **Add Up the Numbers:**
   - The method goes through each number in the input list, adds it to the cumulative total, and records this new total in the list.

5. **Return the Result:**
   - After processing all the numbers, the method returns the complete list of running totals.

### How to Use the Solution

- **Create an Instance:** You need to create an instance of the `Solution` class (called `solution`).
- **Call the Method:** You then pass your list of numbers to the `runningSum` method of this instance. The method will return the list of running totals.

### Example Usage

```python
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
print(solution.runningSum(nums))  # Output: [1, 3, 6, 10]
