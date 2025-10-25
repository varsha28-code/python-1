-----------------------Two Sum-1----------------
nums=list(map(int,input().split()))
target=int(input())
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j]==target):
            print(i,j)

class Solution(object): 
    def twoSum(nums,target):
      for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
           if(nums[i]+nums[j]==target):
               return(i,j)

        --------------------Two Sum-2------------------------
nums=list(map(int,input().split()))
target=int(input())
d={}
for a in range(0,len(nums)):
    b=target-nums[a]
    if(b in d):
        print(a,d[b])
    else:
        d[nums[a]]=a

class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for a in range(len(nums)):
            b = target - nums[a]
            if b in d:
                return [d[b], a]   
            else:
                d[nums[a]] = a   

        -------------------Two Sum-3-------------------------

def twoSum(nums,target):
    low=0
    high=len(nums)-1
    while(low<high):
        Sum=nums[low]+nums[high]
        if(Sum==target):
            return "Yes"
        elif(Sum>target):
            high-=1
        elif(Sum<target):
            low+=1
    return "No"
nums=list(map(int,input().split()))
