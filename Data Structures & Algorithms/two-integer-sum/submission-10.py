class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for num in range(len(nums)):
            needed=target-nums[num]

            if needed in hashmap:
                return [hashmap[needed],num]
            
            hashmap[nums[num]] = num