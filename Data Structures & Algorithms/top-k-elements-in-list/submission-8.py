class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_arr = {}

        for num in nums:
            freq_arr[num] = freq_arr.get(num, 0) + 1

        sorted_freq_arr = dict(sorted(freq_arr.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_freq_arr)[:k]

        

        

        
