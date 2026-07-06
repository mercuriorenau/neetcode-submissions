class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_count = {}
        k_nums = []
        for num in (nums):
            if num in k_count:
                k_count[num] += 1
            else:
                k_count[num] = 1 

        return sorted(k_count, key=lambda x: k_count[x], reverse=True)[:k]




