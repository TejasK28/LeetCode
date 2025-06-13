class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        arr = []
        nums.sort()
        max_len = -float('inf')
        for num in nums:
            if len(arr) == 0:
                arr.append(num)
                max_len = max(max_len, len(arr))
            if (num == arr[-1]):
                continue
            else:
                if(arr[-1] + 1 == num):
                    arr.append(num)
                    max_len = max(max_len, len(arr))
                else:
                    arr.clear()
                    arr.append(num)
        return max_len
        