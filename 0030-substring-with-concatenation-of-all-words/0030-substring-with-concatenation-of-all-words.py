class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])    # Length of each word
        word_count = len(words)     # Number of words
        total_len = word_len * word_count  # Total length of concatenated words
        
        result = []
        word_map = {}  # Dictionary to store frequency of each word
        
        # Build word frequency map
        for word in words:
            word_map[word] = word_map.get(word, 0) + 1
        
        # Try each possible starting position modulo word_len
        for i in range(word_len):
            left = i
            curr_map = {}  # Current window word frequency
            count = 0      # Number of valid words found
            
            # Slide window with step size of word_len
            for j in range(i, len(s) - word_len + 1, word_len):
                curr_word = s[j:j + word_len]
                
                if curr_word in word_map:
                    curr_map[curr_word] = curr_map.get(curr_word, 0) + 1
                    count += 1
                    
                    # Remove words from left if frequency exceeds required
                    while curr_map[curr_word] > word_map[curr_word]:
                        curr_map[s[left:left + word_len]] -= 1
                        count -= 1
                        left += word_len
                    
                    # If we have exactly the right number of words
                    if count == word_count:
                        result.append(left)
                else:
                    # Reset if we encounter a word not in words
                    curr_map.clear()
                    count = 0
                    left = j + word_len
        
        return result