'''In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. '''

class Solution:
    def pairSum(self, head: Optional[ListNode]):
        n=head
        list1=[]
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        length=len(list1)
        
        i=0;j=length-1
        
        list2=[]
        
        while i<j:
            list2.append(list1[i]+list1[j])
            i+=1
            j-=1
            
        return max(list2)
