# encoding=utf-8
'''
题目：按奇偶排序数组 II
给定一个非负整数数组A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当A[i] 为奇数时，i也是奇数；当A[i]为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。

提示：
2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''


array_list = [4,2,5,7,2,3]
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if 2 <= len(A) <= 20000 and len(A) % 2 == 0:
            odd_list = []
            even_list = []
            final_list = []
            for num in A:
                if(0 <= num <= 1000):
                    if (num % 2 == 0):
                        even_list.append(num)
                    else:
                        odd_list.append(num)
                else:
                    raise ValueError
            for i in range(len(A) // 2):
                final_list.append(odd_list[i])
                final_list.append(even_list[i])
            return final_list
        else:
            raise ValueError

result = Solution().sortArrayByParityII(array_list) #  184 ms  15.2 MB
