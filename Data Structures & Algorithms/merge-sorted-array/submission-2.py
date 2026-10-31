class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        space = n
        p1, p2 = 0,0
        while p1 < m and p2 < n:
            if nums1[p1] >= nums2[p2]:
                nums1[p1], nums2[p2] = nums2[p2], nums1[p1]
                
            p1 += 1

        while p2 < n:
            nums1[p1], nums2[p2] = nums2[p2], nums1[p1]
            p2 += 1

        return nums1
        

            

            
