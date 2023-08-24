class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        arr1_length = len(nums1)
        arr2_length = len(nums2)
        arr3 = [None]*(arr1_length+arr2_length)

        i = 0
        j = 0
        k = 0
        
        while i < arr1_length and j < arr2_length:
            if(nums1[i] < nums2[j]):
                arr3[k] = nums1[i]
                i += 1
                k += 1
            else:
                arr3[k] = nums2[j]
                j+=1
                k+=1

        while(i<arr1_length):
            arr3[k] = nums1[i]
            i += 1
            k += 1

        while(j<arr2_length):
            arr3[k] = nums2[j]
            j += 1
            k += 1

       
        arr3_len = len(arr3)

        med = int(arr3_len/2)
        print("median is", med)
        med_item = arr3[med]
        print("number at median index ", med_item)
        med_item_prev = arr3[med-1]
        print("number before median index, ", med_item_prev)
        even_median = (med_item+med_item_prev)/2.0
   
        print("even median, ", even_median)
        print("odd median,", med_item)
        odd_median = med_item

        if (arr3_len % 2 == 0):
            return even_median
        return odd_median
        