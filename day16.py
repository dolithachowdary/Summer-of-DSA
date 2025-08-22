
#pattern1 - constant k value
#pattern2 - Maximum or minimum subarray with some conditions
#subarray
'''arr = [5,10,8]
n = len(arr)
for i in range(0,n):
    for j in range(i,n):
        print(arr[i:j+1])'''

#Maximum sum of subarray of size 4
#TC : O(N**2) 
# constant variable
'''def Max_Sum(arr,k):
    n = len(arr)
    Max = 0
    for i in range(0,n):
        for j in range(i,n):
            if len(arr[i:j+1]) == k:
                Max = max(Max,sum(arr[i:j+1]))
    return Max
    
print(Max_Sum([1,3,10,7,4],3))'''

#optimal
#sliding window

'''def Max_Sum(arr,k):

    n = len(arr)
    if n < k:
        return -1

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(1,n-k+1):
        window_sum = window_sum - arr[i-1] + arr[i+k-1]
        max_sum = max(window_sum,max_sum)

    return max_sum

print(Max_Sum([2,3,5,8,10,12,3,1],4))'''

#Exapanison and shrink

'''def Max_Sum(arr,k):

    n = len(arr)
    left,right = 0,k-1
    Sum = sum(arr[:k])
    Max = Sum

    while right < n-1:
        Sum -= arr[left]
        left += 1
        right += 1
        Sum += arr[right]
        Max = max(Sum,Max)
    return Max

print(Max_Sum([2,3,5,8,10,12,3,1],4))'''

# FInd the maximum length of the subarray whose sum is less than some value
'''def Max_length(arr,k):
    n = len(arr)
    max_Len = 0
    for i in range(0,n):
        for j in range(i,n):
            if sum(arr[i:j+1]) <= k:
                max_Len = max(max_Len,j-i+1)

    return max_Len

print(Max_length([2,3,5,8,10,12,3,1],4))'''

#optimal TC : O(N)
'''def Max_Length(arr,k):
    n = len(arr)
    left,right = 0,1
    Sum = arr[0]
    Max_Len = 1

    while right < n:

        if Sum + arr[right] <= k:
            Sum += arr[right]
            Max_Len = max(Max_Len,right - left + 1)
            right += 1

        elif Sum + arr[right] > k:
            Sum -= arr[left]
            left += 1

    return Max_Len

print(Max_Length([2,5,1,7,10],14))'''

#TC : O(N)
'''def Length(arr,k):
    n = len(arr)
    left,right = 0,0
    Sum = 0
    Max_Len = 0
    while right < n: #O(N)
        Sum += arr[right]
        while Sum > k: #O(N)
            Sum -= arr[left]
            left += 1
        Max_Len = max(Max_Len,right-left+1)
        right += 1
    return Max_Len
print(Length([2,5,1,7,10],14))'''

#Silding window - leetcode 1432
'''def practice(cardpoints,k):
    n=len(cardpoints)
    left=0
    right=k-1
    Sum=0
    left_sum=sum(cardpoints[left:right+1])  # Sum of the first k elements
    right_sum=0
    right_index=n-1
    maxSum=left_sum
    for i in range(k,-1,-1):
        if right_index >= 0:
            right_sum += cardpoints[right_index]
            right_index -= 1
        if left < n:
            left_sum -= cardpoints[left]
            left += 1
        maxSum = max(maxSum, left_sum + right_sum)
    return maxSum
print(practice([1,2,3,4,5,6,1],3))  
'''

#Leetcode longest substring without repeating
#TC : O(N**2)
#SC : O(1) because here the space is not dependent on the input size rather uses a constant size 256 for any input 
'''def lengthOfLongestSubstring(s):
    n = len(s)
    maxLength = 0
    for i in range(n):
        checker = [0] * 256
        for j in range(i,n):
            if checker[ord(s[j])] == 1:
                break
            checker[ord(s[j])] = 1
            maxLength = max(maxLength,j-i+1)
    return maxLength

print(lengthOfLongestSubstring("abcabcbb"))'''

#optimal
'''def length(s):
    n = len(s)
    maxLength = 0
    d = {}
    left , right = 0 , 0
    while right < n:
        if s[right] in d and d[s[right]] >= left:
            left = d[s[right]] + 1
        d[s[right]] = right
        maxLength = max(maxLength,right-left+1)
        right += 1
    return maxLength
print(length("abcabcbb"))'''

#mycode don't read,not correct for all the testcases
'''def length(s):
    n = len(s)
    maxLength = 0
    d = {}
    left , right = 0 , 0
    while right < n:
        if s[right] in d:
            r = d.pop(s[right])
            left = r + 1
            maxLength = max(maxLength,right-left+1)
        else:
            d[s[right]] = right
            right += 1
    return maxLength
print(length("abcabcbb"))'''

#leetcode maximum consecutive one - 1004 
#longest subarray with atmost k zeros
'''def longest(nums,k):
    n = len(nums)
    maxLen = 0
    for i in range(0,n):
        zero = 0
        for j in range(i,n):
            if nums[j] == 0:
                zero += 1
            if zero > k:
                break
            maxLen = max(maxLen,j-i+1)

print(longest([1,0,0,1,0,1,0,1],2))'''

#optimal sol
'''def one(arr,k):
    n = len(arr)
    maxLength = 0
    left,right = 0,0
    count = 0
    while right < n:
        if arr[right] == 0:
            count += 1
        if count > k:
            while count > k:
                if arr[left] == 0:
                    count -= 1
                left += 1
        maxLength = max(maxLength , right - left + 1)
        right += 1
    return maxLength
print(one([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))'''
