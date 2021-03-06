# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/25904/python-heap-solution-with-comments

        intervals.sort(key=lambda x: x.start)
        heap = [] # stores the end time of intervals
        for i in intervals:
            if heap and i.start >= heap[0]:
                # means two intervals can use the same room
                heapq.heapreplace(heap, i.end)
            else:
                # a new rrom is allocated
                heapq.heappush(heap, i.end)
        return len(heap)
