class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        set1 = set(nums1)
        set2 = set(nums2)

        only1 = set1.difference(set2)
        only2 = set2.difference(set1)

        answer.append(list(only1))
        answer.append(list(only2))

        return answer