# array nums and int target
# return indices i and j so num[i+J] = target
# i not equal j


class Solution(object):
    def two_sum(nums, target):
        hash = {}
        for i, num in enumerate(nums):
            diff = target - num

            if diff in hash:
                return [hash[diff], i]

            hash[num] = i

        return None


solution = Solution()
