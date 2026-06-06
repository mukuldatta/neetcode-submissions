class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [0] * len(nums)
        x = len(nums)
        prods = 1
        zero_count = nums.count(0)
        if zero_count > 1:
            return prod
        for i in range(x):
            if nums[i] != 0:
                prods = prods * nums[i]
        for i in range(x):
            if zero_count == 1:
                prod[i] = prods if nums[i] == 0 else 0
            else:
                prod[i] = int(prods / nums[i])
        return prod