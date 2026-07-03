class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_arr = {}

        for num in nums:
            freq_arr[num] = freq_arr.get(num, 0) + 1

        most_common = {}

        for key, value in sorted(freq_arr.items(), key=lambda item: item[1], reverse=True):
            most_common[key] = value

        return list(most_common)[:k]

        

        

        
