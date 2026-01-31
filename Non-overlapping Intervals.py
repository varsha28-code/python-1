class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n=len(intervals)
        intervals.sort(key=lambda x:x[1])
        c=1
        endTime=intervals[0][1]
        for row in range(1,n):
            if(intervals[row][0]>=endTime):
                c+=1
                endTime=intervals[row][1]
        return n-c
        
        
