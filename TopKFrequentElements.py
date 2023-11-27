class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
     
        for value in nums:
            freq[value] = freq.get(value, 0) + 1

        newF = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        return [value for value, _ in newF[:k]]
