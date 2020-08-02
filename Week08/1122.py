class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        not_arry = []
        for i in range(len(arr1)):
            dic[arr1[i]] = dic.get(arr1[i], 0) + 1
            if arr1[i] not in arr2:
                not_arry.append(arr1[i])
        not_arry.sort()

        new_arr1 = []
        arr1 = set(arr1)
        for j in range(len(arr2)):
            new_arr1 += [arr2[j]] * dic[arr2[j]]
        return new_arr1 + not_arry
