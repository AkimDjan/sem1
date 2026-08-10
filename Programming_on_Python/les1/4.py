def horpodmass(nums:list, k:int) -> bool:
    dc={0:-1}
    c=0

    for i in range(len(nums)):
        num=nums[i]
        c+=num
        dl=c%k
        if dl in dc:
            if i - dc[dl]>1:
                return True
        else:
            dc[dl]=i
    return False


        

    

nums = list(map(int, input().split()))
k = int(input())
print(horpodmass(nums,k))
