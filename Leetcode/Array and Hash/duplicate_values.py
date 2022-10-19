// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

'''Example 1:

// Input: nums = [1,2,3,1]
// Output: true
// Example 2:

// Input: nums = [1,2,3,4]
// Output: false

// https://leetcode.com/problems/contains-duplicate/

// arr = [4,5,6,7,2,4] BCR = O(N)

// Method 1
// 4 -> 5
// 4 -> 6
// 4 -> 7/2/1

// 5 -> 6

// Pseudo code
// Time complexity = O(n^2) NESTED LOOP
// space complexity = O(1)
// for loop, i starts from 0, till length of arr
//   for loop j starts from i+1 till length of arr
  
// METHOD 2 - Hash Map  = Object = Dictionary = Map
// nums = [4,5,6,7,2,4] BCR = O(N)
// Map = O(1) time complexity, if any element is there

// map = { 4: "true', 5: true, 6: true, 7:true, 2:true,}
// map = { 1: true, 8: true, ...100:true}

'''

  def containsDuplicate(nums):
    map = {}

    for n in nums:
      if n not in map:
        map[n] = true;
      else:
        return true
  
    return false


    nums= [1,2,3,4,]
    
#using Function

def containsDuplicate(nums):
    map = {}
    for i in nums:
        if i not in map:
            map[i] = True
        else:
            return True
    return False

result = containsDuplicate(nums)
print(result)
