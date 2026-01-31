class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # code here
        n=len(start)
        mat=[]
        for ind in range(0,n):
            mat.append([start[ind],end[ind]])
        mat.sort(key=lambda x:x[1])
        c=1
        endTime=mat[0][1]
        for row in range(1,n):
            if(mat[row][0]>endTime):
                c+=1
                endTime=mat[row][1]
        return c
        
