# Linked List — How I’m Learning It

**Date:** 2025-11-14  
**Category:** LeetCode Learning Notes  
**Key Problem Reference:** LC #002 Add Two Numbers  

---

## What I Learned
- A linked list is a chain of nodes: each node has a `val` and a pointer to `next`.
- Access is sequential (O(n)); random access is not supported.
- Useful when you need frequent insertion/deletion in the middle of data.
- Common patterns:
  - Dummy head simplifies edge cases.
  - Two-pointer technique for middle finding or cycle detection.
  - Carry propagation for arithmetic.

---

## Visualization
head → [2 | •-] → [4 | •-] → [3 | / ]

(Each box = a node, arrow = link to next node.)

---

## Pseudocode for LC #002 Add Two Numbers
carry = 0
dummy = new Node(0)
curr = dummy
while l1 or l2 or carry:
v1 = l1.val if l1 else 0
v2 = l2.val if l2 else 0
total = v1 + v2 + carry
carry = total // 10
curr.next = new Node(total % 10)
curr = curr.next
l1 = l1.next if l1 else None
l2 = l2.next if l2 else None
return dummy.next

## Complexity
- Traversal: O(n)
- Insertion at head: O(1)
- Deletion (with previous node): O(1)

---

## Common Pitfalls
- Forgetting to move pointer → infinite loop  
- Losing track of `next` reference before linking  
- Forgetting to handle final carry  

---

## Related Problems
- LC 206: Reverse Linked List  
- LC 21: Merge Two Sorted Lists  
- LC 141: Linked List Cycle  

---

## Reflection
**What confused me:** two pointers  
**What I understand now:** linked list 
**Next step:** note books
