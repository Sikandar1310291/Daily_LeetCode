class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]  # Start with the first string as a prefix
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Reduce prefix size if it doesn't match
                if not prefix:
                    return ""  # If prefix becomes empty, return immediately
        
        return prefix