class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_counter = Counter(nums)
        max_frequency = max(freq_counter.values())
        max_freq_elements = sum(1 for freq in freq_counter.values() if freq == max_frequency)
        total_max_freq = max_frequency * max_freq_elements
        return total_max_freq