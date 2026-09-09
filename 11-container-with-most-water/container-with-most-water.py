class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right  = len(height) - 1
        max_vol = 0
        while left < right:
            if min(height[left],height[right]) * (right - left) > max_vol:
                max_vol = min(height[left],height[right]) * (right- left)
                # while left < right:
                #     if height[left] > height[right]:
                #         right -=1
                #     else:
                #         left +=1

            elif height[left] > height[right]:
                right -=1
            else:
                left +=1
        return max_vol

        