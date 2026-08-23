class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            i_sorted = "".join(sorted(i))
            if i_sorted in anagrams.keys():
                anagrams[i_sorted].append(i)
            else:
                anagrams[i_sorted] = [i]

        
        return list(anagrams.values())

                