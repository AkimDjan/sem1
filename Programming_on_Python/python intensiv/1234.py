def min_jumps(jumps):
    n = len(jumps)
    if n == 1:
        return 0
    if jumps[0] == 0:
        return -1
    
    max_reach = jumps[0]    
    steps = jumps[0]         
    jumps_count = 1          
    for i in range(1, n):
        if i == n - 1:
            return jumps_count
        max_reach = max(max_reach, i + jumps[i])
        steps -= 1
        if steps == 0:
            jumps_count += 1
            if i >= max_reach:
                return -1            
            steps = max_reach - i
    return -1

jumps=list(map(int,input().split()))
print(min_jumps(jumps))
