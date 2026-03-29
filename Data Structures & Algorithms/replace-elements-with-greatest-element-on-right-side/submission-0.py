class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxele = -1
        n = len(arr)
        for i in range(0,n):
            for j in range(i+1,n):
                maxele = max(arr[j],maxele)
            arr[i] = maxele
            maxele = -1
        return arr