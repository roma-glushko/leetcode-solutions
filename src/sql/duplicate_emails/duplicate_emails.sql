/**
Problem Link: https://leetcode.com/problems/duplicate-emails/
Complexity: Easy

Runtime: 370ms
Memory: OB
**/

SELECT Email FROM Person GROUP BY Email HAVING count(id) > 1