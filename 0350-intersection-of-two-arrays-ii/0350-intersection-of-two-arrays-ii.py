class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res=[]
        l=len(nums1)
        r=len(nums2)
        i=j=0
        while i<l and j<r:
            if nums1[i]<nums2[j]:
                i+=1
            elif nums2[j]<nums1[i]:
                j+=1
            else:
                res.append(nums1[i])
                i+=1
                j+=1
        return res
        
            
            
        
        