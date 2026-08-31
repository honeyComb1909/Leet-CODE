from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # A critical point cannot exist if there are fewer than 3 nodes
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        index = 1
        
        first_cp_index = -1
        prev_cp_index = -1
        min_distance = float('inf')
        
        while curr.next:
            # Check if curr is a local maxima or local minima
            is_critical = (curr.val > prev.val and curr.val > curr.next.val) or \
                          (curr.val < prev.val and curr.val < curr.next.val)
            
            if is_critical:
                if first_cp_index == -1:
                    first_cp_index = index
                else:
                    # Update the minimum distance between adjacent critical points
                    min_distance = min(min_distance, index - prev_cp_index)
                
                prev_cp_index = index
            
            prev = curr
            curr = curr.next
            index += 1
            
        # If fewer than 2 critical points were found
        if min_distance == float('inf'):
            return [-1, -1]
        
        max_distance = prev_cp_index - first_cp_index
        return [min_distance, max_distance]