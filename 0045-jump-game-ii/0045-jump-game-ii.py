from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_reach = 0  # The furthest we can reach with the current number of jumps
        cur_max = 0    # The furthest index we can reach overall
        jumps = 0
        i = 0
        
        while i < len(nums) - 1:
            cur_max = max(cur_max, i + nums[i])
            
            if i == cur_reach:  # We must make a jump
                jumps += 1
                cur_reach = cur_max  # Update the reachable range
                
                if cur_reach >= len(nums) - 1:
                    break  # If we can reach the end, stop early
            
            i += 1
        
        return jumps
