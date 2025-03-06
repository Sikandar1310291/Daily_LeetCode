class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = []
        min_len = min(len(word1) , len(word2))

        for i in range(min_len):
            merge.append(word1[i])
            print(merge)
            merge.append(word2[i])
            print(merge)

        merge.append(word1[min_len:])
        print(merge)
        merge.append(word2[min_len:])
        print(merge)
            
        return "".join(merge) 
        print(merge)   