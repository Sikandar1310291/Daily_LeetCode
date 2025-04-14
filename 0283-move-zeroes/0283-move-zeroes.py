class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        lastNonZero = 0  # position to place the next non-zero element

        # Move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZero] = nums[i]
                lastNonZero += 1

        # Fill the remaining positions with zeroes
        for i in range(lastNonZero, len(nums)):
            nums[i] = 0

