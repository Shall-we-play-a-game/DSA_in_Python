with open('input.txt', 'r') as file:
    nums = list(map(int, file.readline().strip().split()))
    target = int(file.readline().strip())

def twoSum(nums, target):
    # we initialize an empty dictionary num_dict to store number and its index
    num_dict = {} 
    # We Iterate through the list nums using enumerate to get both index i and value num
    for i, num in enumerate(nums): 
        # for each number we calculate complement, complement = target - num 
        complement = target - num 
        # We check if complement is in the dictionary num_dict If it is that means we have found a pair of numbers that add up to the target so we return their indices
        if complement in num_dict: 
            # if the complement is not in the dictionary we add the current number num and its index i to dictionary
            return [num_dict[complement], i]
        num_dict[num] = i
    # if we finished iterating through the list and haven't found a pair of numbers then return an empty list []
    return []

print(twoSum(nums, target))
