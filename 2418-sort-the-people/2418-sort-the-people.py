class Solution:

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sort_list = []
        name_list = []
        for i in range(len(names)):
            sort_list.append([heights[i], names[i]])
        sort_list.sort(reverse=True)
        for i in range(len(sort_list)):
            name_list.append(sort_list[i][1])
        return name_list