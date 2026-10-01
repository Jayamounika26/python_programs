class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        max_count=max(freq.values())
        count=0

        for num in freq:
            if freq[num]==max_count:
                count+=freq[num]
        return count