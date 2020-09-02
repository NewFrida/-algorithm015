class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 考虑特殊情况
        if len(nums) < 3:
            return []

        # 排序后再遍历
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            # 由于排序的原因，如果nums[i]大于0的话，后面再加两个大于0的数，不可能为0，所以到这里，遍历就要结束了
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start = i + 1
            end = len(nums) - 1
            while start < end:

                # 判断当前的三数和与0的大小，并移动指针
                three_sum = nums[i] + nums[start] + nums[end]
                if three_sum == 0:
                    result.append([nums[i], nums[start], nums[end]])

                    # 如果当前元素和前一个已经判断过的元素一样，则跳过继续
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1

                    start += 1
                    end -= 1
                elif three_sum > 0:
                    end -= 1
                else:
                    start += 1

        return result

