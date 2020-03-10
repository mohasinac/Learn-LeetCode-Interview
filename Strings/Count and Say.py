"""
he count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. 
You can do so recursively, in other words from the previous member read off the digits, 
counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.

Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", 
"2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", 
so the answer is the concatenation of "12" and "11" which is "1211".
"""
class Solution:
    def countAndSay(self, terms: int) -> str:
        """
        1 has only 1
        2 will 11 as (previous had only single 1)
        3 will have 21 as (previous had 2 continous 1 )
        4 will have 1211 as prvious has a single 2 and single 1
        5 will have 111221 as previous has single 1 single 2 and then double 1
        6 will have 312211 as previous has thrice 1 twice 2 and then double 1
        """
        ans="1"
        for i in range(1,terms):
            n=ans
            last=n[0]
            count=0
            ans=""
            for c in n:
                if c==last:
                    count+=1
                else:
                    ans+=str(count)+str(last)
                    count=1
                    last=c
            if count:
                ans+=str(count)+str(last)
        return ans
        