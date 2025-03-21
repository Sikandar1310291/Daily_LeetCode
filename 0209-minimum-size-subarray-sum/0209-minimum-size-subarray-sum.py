class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums) + 1
        start = end = 0
        cur_sum = 0

        for end in range(len(nums)):
            cur_sum += nums[end]
            print(cur_sum)

            while cur_sum >= target:
                size = min(size , end - start + 1)
                print(size)
                cur_sum -= nums[start]
                print(cur_sum)
                start += 1
        return size if size != len(nums) + 1 else 0
