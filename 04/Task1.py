def max_length(nums):

    dp = [1] * len(nums) # dp[i] массив из максимальных, заканчивающийся на i

    for i in range(len(nums)):
        for j in range(i): # смотрим элементы перед i

            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

nums1 = [20, 5, 4, 7, 5, 100, 1]
nums2 = [1, 3, 5, 3, 6]
nums3 = [55, 55, 55]
assert max_length(nums1) == 3
assert max_length(nums2) == 4
assert max_length(nums3) == 1
