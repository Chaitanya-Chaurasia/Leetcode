# Leetcode
My leetcode problems log


## Tricks to remember :

### A) Sliding Window
- Make two pointers l and r, which are usually 0 and 1 or len(list) depending on question, and then increment or decrement size of window to check for condition.

### B) Reverse Linked List
- To reverse a linked list, the concept is that make 2 pointers prev, curr and temp. Remove next pointer of curr, and point it to prev. Before this store the next pointer of curr in the temp variable to not lose access of the list. Then point the prev pointer to curr, and then move the curr pointer to temp, since temp is nothing but curr->next.
- Once this algo runs, your prev counter in the last element, and temp and curr and both pointing to the next element of the tail of the original non-reversed linked list i.e. None.
- 
  ```
  prev = None
  curr = head

  while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  ```

### C) Reverse half Linked List to calculate twin sum AND Delete Middle Node
- These are based on fast and slow pointers. Concept for slow is that it is our "curr" pointer. Fast increments it self by 2 everytime. So if our slow pointer is at position i, fast pointer is already at 2*i. So, if length of linked list in n, and fast is at n, slow is at the mid-point. This is very helpful. From here, various problems can be solved.
- For first prob, reverse half the linked list by using 2 pointers namely fast and slow. Then start from head of both, and compare.

### D) Use collections and Counter() in string questions
