# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.


# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Solution

# 1. For sorting I used python's sorting Fxn which take O(n*logn).
# 2. Now we gonna interate through our sorted intervals using a loop.
# 3. Intially as our result list is empty we gonna add first interval from intervals
# as it.
# 4. Then for next interval if end of last added interval in result is greater
# than or equal to current pointer interval start we gonna merge both such that
# start of new interval is start of already added interval and end gonna be
# maximum of both end points otherwise simply add the current interval as it using append from.


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            if not res or intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        return res
