class Solution:
    def minSwaps(self, data) -> int:
        k = sum(data)
        l, r = 0, k
        cur_sum = sum(data[:k])
        min_swaps = k - cur_sum

        while r < len(data):
            cur_sum += data[r]
            cur_sum -= data[l]
            r += 1
            l += 1
            min_swaps = min(min_swaps, k - cur_sum)
        
        return min_swaps