class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num_i = num_j = float("inf")
        for i in nums:
            if    i <= num_i:
                num_i = i
            elif  i <= num_j:
                num_j = i
            else:
                return True  
        return False