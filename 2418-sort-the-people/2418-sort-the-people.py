class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people_dict = {}

        for i in range(len(names)):
            people_dict[heights[i]] = names[i]

        sorted_dict = sorted(people_dict.items(), reverse=True)
        sorted_names = [i[1] for i in sorted_dict]
        
        return sorted_names
