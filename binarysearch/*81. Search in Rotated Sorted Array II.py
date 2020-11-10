# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        n = len(nums)
        l, r = 0, n

        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            else:
                if nums[m] > nums[r - 1]:
                    if nums[l] <= target < nums[m]:
                        r = m
                    else:
                        l = m + 1
                elif nums[m] < nums[r - 1]:
                    if nums[m] < target <= nums[r - 1]:
                        l = m + 1
                    else:
                        r = m
                else:
                    r -= 1

        return False