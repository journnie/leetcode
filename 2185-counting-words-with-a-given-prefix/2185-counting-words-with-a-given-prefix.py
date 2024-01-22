class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        start_with = 0
        for i in words:
            start_bool = i.startswith(pref)
            if start_bool == True:
                start_with += 1
        return start_with
            