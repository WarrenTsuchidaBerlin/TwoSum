#https://leetcode.com/problems/two-sum/description/
#You have an array with a bunch of numbers and then you have one number outside of the array called target. Two numbers in the array, when added together, should equal target. You need to return the indices of these two numbers.

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    #here we create an empty hash table that will be used to store keys and values as we move through the array. The value will be the number in the array, and they key will be it's indice. Remember, we need both because the number is what's used in the calculation to find the target, and the indice is what we use in the answer itself. 
    numMap = {}

    #here we are defining n which is necessary for the calculation for the loop in the next line. Basically, this is how we define the last number of the array, which is key because we need the loop to start at the beginning and go to the end, n.
    n = len(nums)

    #here we begin the loop
    for i in range(n):
      #this is how we find our answer. Basically, every number the loop passes through puts the number in this equation into the "nums[i]" spot. So, it subtracts it from target, which is the number we are trying to find here. You'll see how this finds our answer in the next few lines, because if the number we are currently on in the loop is half of the answer, then complement is the other half. Continueing the loop, if complement is already in numMap (which remember is the first thing we made, which was an empty has table), then we are done!
      complement = target - nums[i]
            if complement in numMap:
              #if we got a bingo, this line prints out the answer right here. Complement, and i which is the number in the loop we were on when we struck gold.
              return [numMap[complement], i]
            #If the complement is not in numMap, this line "files away" (remember the file cabinet analogy for has maps) the current number nums[i] in the hash table, using the number itself as the key and its index i as the value.
            numMap[nums[i]] = i
      
    return []
