# Blind 75 Notes

<!-- AUTO-GENERATED FILE. DO NOT EDIT MANUALLY. -->
*Last updated: 2025-09-23 05:25 UTC*

[Source spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vRw_Ro70SyoCP4FIHwwfkDdwVhXWU_lKwfl6Rw3tXlD1nFD5gfPVk1B0SufuQATexITGzPiwNmeUav0/pub?output=csv)

## [Contains Duplicate](../Problems/contains-duplicate/)
- **Category:** Array & Hashing
- **Notes:** Hashset, check if the value is in seen otherwise, add it to seen

## [Valid Anagram](../Problems/valid-anagram/)
- **Category:** Array & Hashing
- **Notes:**
  - Two ways to solve this:
  - 1) Hashmaps to keep track of char count and then compare
  - 2) ASCII values list, adding count of 1 and subtracting count of 2, at the end, the list should have counts of all 0s

## [Two Sum](../Problems/two-sum/)
- **Category:** Array & Hashing
- **Notes:**
  - Loop through every value
  - If our target - the value we are looking at is in our hashmap of seen values, return them
  - Otherwise, add it to our hashmap

## [Group Anagrams](../Problems/group-anagrams/)
- **Category:** Array & Hashing
- **Notes:**
  - Loop through strings storing list of counts as the key and string as value (defaultdict(list))
  - ASCII values for count

## [Top K Frequent Elements](../Problems/top-k-frequent-elements/)
- **Category:** Array & Hashing
- **Notes:**
  - Hashmap for count and dict of lists per number in input list storing count as key and number as values
  - Loop to get count of each number
  - Loop to store each number and its count in dict
  - Return the k most frequent numbers

## [Encode and Decode Strings](../Problems/encode-and-decode-strings/)
- **Category:** Array & Hashing
- **Notes:**
  - Encode saving the new string as (length, unique char, string)
  - Decode Looping until we hit our right bound, using pointers front, middle, and end
  - Front points to our first number for our string length
  - Middle points to our unique char
  - End points to the end of our string

## [Product of Array Except Self](../Problems/product-of-array-except-self/)
- **Category:** Array & Hashing
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n)
- **Notes:**
  - Result list
  - Prefix, equal first then multiply update
  - Postfix, multiply first then multiply update

## [Longest Consecutive Sequence](../Problems/longest-consecutive-sequence/)
- **Category:** Array & Hashing
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  - Use a set to iterate quickly
  - Loop over every unique number
  - Check if it is a start of a sequence
  - If it is, continue to check the numbers after if it is a sequence
  - Then compare it to the length of the max

## [Valid Palindrome](../Problems/valid-palindrome/)
- **Category:** Two Pointers
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Loop through Two pointers
  - Increment/decrement whether pointer value is within ascii values to avoid non numeric values
  - Compare characters at pointer values
  - Update pointers

## [Two Sum II Input Array Is Sorted](../Problems/two-sum-ii-input-array-is-sorted/)
- **Category:** Two Pointers
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Loop 2 pointers
  - Calculate twoSum, and update pointers based on whether greater or less than target

## [Three Sum](../Problems/three-sum/)
- **Category:** Two Pointers
- **Time Complexity:** O(n^2)
- **Space Complexity:** O(1) or O(n)
- **Notes:**
  - Result list and sort the input list
  - Enumerate though each value in the list
  - Check if the smallest value is greater than target
  - After the first iteration, check if prev value is the same as current value
  - Loop through pointers which are the ends after the value we enumerate
  - Calculate threeSum, and update pointers based on whether equal, greater or less than target
  - When equal, update both pointers and duplicate check

## [Container With Most Water](../Problems/container-with-most-water/)
- **Category:** Two Pointers
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Two pointers
  - Loop through ends (pointers)
  - Calculate area
  - Update pointers based on which value is smaller

## [Best Time to Buy and Sell Stock](../Problems/best-time-to-buy-and-sell-stock/)
- **Category:** Sliding Window
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Two pointers
  - Loop until our sell pointer crosses input array bounds
  - If sell is greater than buy, get the max of our old and current profit
  - Otherwise, this means we have a new low buy, so update pointers accordingly

## [Longest Substring Without Repeating Characters](../Problems/longest-substring-without-repeating-characters/)
- **Category:** Sliding Window
- **Time Complexity:** O(n)
- **Space Complexity:** O(m)
- **Notes:**
  - Hashmap to store char as key and its index as the value
  - Two pointers
  - Loop through our right pointer, adding them to hashmap
  - If duplicate (already in seen) & last seen duplicate char index greater than our left pointer
  - Update left pointer to last seen duplicate char index + 1 (to skip it)

## [Longest Repeating Character Replacement](../Problems/longest-repeating-character-replacement/)
- **Category:** Sliding Window
- **Time Complexity:** O(n)
- **Space Complexity:** O(m)
- **Notes:**
  - Dictionary to store unique letters as keys and counts as values
  - Two pointers, loop with right pointer, update counts and max length
  - While the most frequency letter plus k is less than the length of the string
  - Update the letters count and left pointer

## [Minimum Window Substring](../Problems/minimum-window-substring/)
- **Category:** Sliding Window
- **Notes:**
  - Check if are target substring is empty else continue
  - Hashmaps for window and target substring
  - Two pointers, loop until our right pointer hits the right bound (end of input string)
  - Continously add unique char and their count to our window
  - If we have the count for all the unique letters we need save it if is it smaller than our old substring
  - Update our left pointer and decrease the count until we don't have what we need anymore

## [Valid Parentheses](../Problems/valid-parentheses/)
- **Category:** Stack
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  - Stack and Hashmap to map parentheses
  - Loop through every char and check if it is open or close, add opens as needed and check stack if looking at close
  - Return whether we have no more opens in our stack or if we run into the wrong close

## [Binary Search](../Problems/binary-search/)
- **Category:** Binary Search
- **Time Complexity:** O(logn)
- **Space Complexity:** O(1)
- **Notes:**
  - Two pointers and loop until they cross, it's okay if they're equal
  - If the middle pointer is less than target, update right pointer
  - Else means middle pointer is greater than target, update left pointer

## [Search a 2D Matrix](../Problems/search-a-2d-matrix/)
- **Category:** Binary Search
- **Time Complexity:** O(lognm)
- **Space Complexity:** O(1)
- **Notes:**
  - Four pointers, 2 for rows top and bottom, 2 for columns left and right
  - Loop until the row pointers cross, it's okay if they're equal, get middle row
  - If the first value in the middle row is less than target, update bottom row
  - If the last value in the middle row is greater than target, update top row
  - Else, means target must be in row and perform traditional binary search

## [Koko Eating Bananas](../Problems/koko-eating-bananas/)
- **Category:** Binary Search
- **Time Complexity:** O(lognm)
- **Space Complexity:** O(1)
- **Notes:**
  - Two pointers, between values 1 and max rate per hour
  - Loop until pointers cross, it's okay if they're equal
  - Calculate total hours it takes to eat all bananas with middle rate (math.ceil(float(x) / m))
  - If valid, update right pointer
  - Else this means we didn't finish eating in time, update left (to eat more per hour)

## [Find Minimum In Rotated Sorted Array](../Problems/find-minimum-in-rotated-sorted-array/)
- **Category:** Binary Search
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Notes:**
  - Two pointers, loop until they cross
  - If our middle pointer is less than our right, its impossible to have a smaller number than middle
  - Else means it is greater and our right subarray has the smaller value than our middle
  - Last case, middle and left pointer will be the same, and if it's greater than our right, l = m + 1 = r, next iteration pointers cross

## [Search In Rotated Sorted Array](../Problems/search-in-rotated-sorted-array/)
- **Category:** Binary Search
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Notes:**
  - Two pointers and loop until they cross, it's okay if they're equal
  - If our middle is the target, return, otherwise, two subcases
  - Elif middle is greater than our left pointer (left side is sorted)
  - And If our target is greater than our middle pointer or less than our left pointer (meaning it's not in our sorted side), update left
  - Else, our target is in our sorted side and update right
  - Else, meaning our right side is sorted
  - And our target is less than our middle pointer but greater than our right pointer (meaning it's not in our sorted sid), update right
  - Else, our target is in our sorted side and update left

## [Reverse Linked List](../Problems/reverse-linked-list/)
- **Category:** Linked List
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Think of creating a new List starting with None, and redirecting every node to point to that new list 1 by 1
  - Update our current nodes next to point to our previous
  - Change our prevous pointer to be our current node (to continue iterating)
  - Change our old current nodes next (before we changed it) to be our new current

## [Merge Two Sorted Lists](../Problems/merge-two-sorted-lists/)
- **Category:** Linked List
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(1)
- **Notes:**
  - 1) Edge case, 2) determine head node, 3) merge loop, 4) attach rest
  - Edge case if lists are None
  - Compare list.val and set as head and tail, move to next node in list we took node from
  - Loop while both lists have nodes, attaching smaller node to tail.next and updating tail to tail.next
  - Tail.next is the node that is not None

## [Linked List Cycle](../Problems/linked-list-cycle/)
- **Category:** Linked List
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Slow/fast pointers
  - Loop until fast and its next are None constantly checking if the pointers nodes are ever equal

## [Reorder List](../Problems/reorder-list/)
- **Category:** Linked List
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Slow/fast pointers, reverse second half, merge lists:
  - Slow/fast pointers to find second half, slow.next is our start second half, fast to find our end bound
  - Then we need to reverse the links so we start at the end and point to the middle (second half points backwards)
  - While second, save next nodes, change the nodes our currents point to, update our current nodes to temps

## [Remove Nth Node From End of List](../Problems/remove-nth-node-from-end-of-list/)
- **Category:** Linked List
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Slow/fast pointers, slow = head, fast = n
  - If n is the size of the list (meaning fast is None) return the next node after the head
  - Else we loop until the node after fast is None (because we want slow to point to the node before our nth end node)
  - Then, redirect links

## [Merge K Sorted Lists](../Problems/merge-k-sorted-lists/)
- **Category:** Linked List
- **Time Complexity:** O(n log k)
- **Space Complexity:** O(log k)
- **Notes:**
  - Two pointers, Divide and conquer (recursive)
  - Divide: Get the range of lists, divide until we only look at 1 which is sorted (pointers are same)
  - Two pointers/conquer: Used to look at two nodes from divide and begin merging sorted lists into 1 sorted list
  - Key: Recursivly divide until we only have a list from both left and right halves, then slowly merge them until we have 1 resulting list

## [Invert Binary Tree](../Problems/invert-binary-tree/)
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:** 1) Edge case, 2) swap left and right nodes, 3) Recursively call on both left and right nodes (the ones we changed)

## [Maximum Depth of Binary Tree (DFS)](../Problems/maximum-depth-of-binary-tree-dfs/)
- **Time Complexity:** O(n)
- **Space Complexity:** O(h) - O(log n), O(n)
- **Notes:**
  - Case 1 (no node): if root is None, that side of the tree is empty, so depth = 0.
  - Case 2 (node exists): return 1 (for the current node) plus the max depth of the left and right subtrees.

## [Same Tree (DFS)](../Problems/same-tree-dfs/)
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  - Base case: return true if nodes are null
  - Then if both not null and equal, recursively return the comparision of the left and right nodes of both trees
  - Otherwise, false

## [Subtree of Another Tree (DFS)](../Problems/subtree-of-another-tree-dfs/)
- **Time Complexity:** O(nm)
- **Space Complexity:** O(n + m)
- **Notes:**
  - Iterate the tree using a basic stack or recursive call
  - If found subtree, perform same tree check (either recursively with a seperate function or iteratively with a stack)

## [Lowest Common Ancestor of a Binary Search Tree](../Problems/lowest-common-ancestor-of-a-binary-search-tree/)
- **Time Complexity:** O(h)
- **Space Complexity:** O(1)
- **Notes:**
  - Case 1: Both nodes are greater than our current node, we go right
  - Case 2: Both nodes are less than our current node, we go left
  - Case 3: This means a split occured (one node is to the left and the other is to the right) or one node equals our current, LCA found

## [Binary Tree Level Order Traversal](../Problems/binary-tree-level-order-traversal/)
- _No details provided._

## [Validate Binary Search Tree](../Problems/validate-binary-search-tree/)
- _No details provided._

## [Kth Smallest Element In a Bst](../Problems/kth-smallest-element-in-a-bst/)
- _No details provided._

## [Construct Binary Tree From Preorder And Inorder Traversal](../Problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- _No details provided._

## [Binary Tree Maximum Path Sum](../Problems/binary-tree-maximum-path-sum/)
- _No details provided._

## [Serialize And Deserialize Binary Tree](../Problems/serialize-and-deserialize-binary-tree/)
- _No details provided._
