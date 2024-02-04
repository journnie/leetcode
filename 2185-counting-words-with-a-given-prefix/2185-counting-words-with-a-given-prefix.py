class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pref_len = len(pref)
        prefix_count = 0

        for word in words:
            if word[0:pref_len] == pref:
                prefix_count += 1

        return prefix_count