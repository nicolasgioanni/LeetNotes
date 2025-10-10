# Blind 75 Notes

<!-- AUTO-GENERATED FILE. DO NOT EDIT MANUALLY. -->
*Last updated: 2025-10-10 13:28 UTC*

[Source spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vRw_Ro70SyoCP4FIHwwfkDdwVhXWU_lKwfl6Rw3tXlD1nFD5gfPVk1B0SufuQATexITGzPiwNmeUav0/pub?output=csv
)

## Array & Hashing

**Contains Duplicate** *([Problem](https://leetcode.com/problems/contains-duplicate/) | [Solution](../Problems/0217.%20Contains%20Duplicate/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:** Hashset, check if the value is in seen otherwise, add it to seen

**Valid Anagram** *([Problem](https://leetcode.com/problems/valid-anagram/) | [Solution](../Problems/0242.%20Valid%20Anagram/solution.py))*
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(1)
- **Notes:**
  - Two ways to solve this:
  - 1) Hashmaps to keep track of char count and then compare
  - 2) ASCII values list, adding count of 1 and subtracting count of 2, at the end, the list should have counts of all 0s

**Two Sum** *([Problem](https://leetcode.com/problems/two-sum/) | [Solution](../Problems/0001.%20Two%20Sum/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  - Loop through every value
  - If our target - the value we are looking at is in our hashmap of seen values, return them
  - Otherwise, add it to our hashmap

**Group Anagrams** *([Problem](https://leetcode.com/problems/group-anagrams/) | [Solution](../Problems/0049.%20Group%20Anagrams/solution.py))*
- **Time Complexity:** O(nm)
- **Space Complexity:** O(nm)
- **Notes:**
  - Loop through strings storing list of counts as the key and string as value (defaultdict(list))
  - ASCII values for count

**Top K Frequent Elements** *([Problem](https://leetcode.com/problems/top-k-frequent-elements/) | [Solution](../Problems/0347.%20Top%20K%20Frequent%20Elements/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  - Hashmap for count and dict of lists per number in input list storing count as key and number as values
  - Loop to get count of each number
  - Loop to store each number and its count in dict
  - Return the k most frequent numbers

**Encode and Decode Strings** *([Problem](https://leetcode.com/problems/encode-and-decode-strings/) | [Solution](../Problems/0271.%20Encode%20and%20Decode%20Strings/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n + m)
- **Notes:**
  - Encode saving the new string as (length, unique char, string)
  - Decode Looping until we hit our right bound, using pointers front, middle, and end
  - Front points to our first number for our string length
  - Middle points to our unique char
  - End points to the end of our string

**Product of Array Except Self** *([Problem](https://leetcode.com/problems/product-of-array-except-self/) | [Solution](../Problems/0238.%20Product%20of%20Array%20Except%20Self/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n)
- **Notes:**
  - Result list
  - Prefix, equal first then multiply update
  - Postfix, multiply first then multiply update

**Longest Consecutive Sequence** *([Problem](https://leetcode.com/problems/longest-consecutive-sequence/) | [Solution](../Problems/0128.%20Longest%20Consecutive%20Sequence/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  - Use a set to iterate quickly
  - Loop over every unique number
  - Check if it is a start of a sequence
  - If it is, continue to check the numbers after if it is a sequence
  - Then compare it to the length of the max

## Two Pointers

**Valid Palindrome** *([Problem](https://leetcode.com/problems/valid-palindrome/) | [Solution](../Problems/0125.%20Valid%20Palindrome/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Loop through Two pointers
  - Increment/decrement whether pointer value is within ascii values to avoid non numeric values
  - Compare characters at pointer values
  - Update pointers

**Two Sum II Input Array Is Sorted** *([Problem](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Solution](../Problems/0167.%20Two%20Sum%20II%20Input%20Array%20Is%20Sorted/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Loop 2 pointers
  - Calculate twoSum, and update pointers based on whether greater or less than target

**Three Sum** *([Problem](https://leetcode.com/problems/3sum/) | [Solution](../Problems/0015.%20Three%20Sum/solution.py))*
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

**Container With Most Water** *([Problem](https://leetcode.com/problems/container-with-most-water/) | [Solution](../Problems/0011.%20Container%20With%20Most%20Water/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Two pointers
  - Loop through ends (pointers)
  - Calculate area
  - Update pointers based on which value is smaller

## Sliding Window

**Best Time to Buy and Sell Stock** *([Problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Solution](../Problems/0121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Two pointers
  - Loop until our sell pointer crosses input array bounds
  - If sell is greater than buy, get the max of our old and current profit
  - Otherwise, this means we have a new low buy, so update pointers accordingly

**Longest Substring Without Repeating Characters** *([Problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Solution](../Problems/0003.%20Longest%20Substring%20Without%20Repeating%20Characters/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(m)
- **Notes:**
  - Hashmap to store char as key and its index as the value
  - Two pointers
  - Loop through our right pointer, adding them to hashmap
  - If duplicate (already in seen) & last seen duplicate char index greater than our left pointer
  - Update left pointer to last seen duplicate char index + 1 (to skip it)

**Longest Repeating Character Replacement** *([Problem](https://leetcode.com/problems/longest-repeating-character-replacement/) | [Solution](../Problems/0424.%20Longest%20Repeating%20Character%20Replacement/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(m)
- **Notes:**
  - Dictionary to store unique letters as keys and counts as values
  - Two pointers, loop with right pointer, update counts and max length
  - While the most frequency letter plus k is less than the length of the string
  - Update the letters count and left pointer

**Minimum Window Substring** *([Problem](https://leetcode.com/problems/minimum-window-substring/) | [Solution](../Problems/0076.%20Minimum%20Window%20Substring/solution.py))*
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(m)
- **Notes:**
  - Check if are target substring is empty else continue
  - Hashmaps for window and target substring
  - Two pointers, loop until our right pointer hits the right bound (end of input string)
  - Continously add unique char and their count to our window
  - If we have the count for all the unique letters we need save it if is it smaller than our old substring
  - Update our left pointer and decrease the count until we don't have what we need anymore

## Stack

**Valid Parentheses** *([Problem](https://leetcode.com/problems/valid-parentheses/) | [Solution](../Problems/0020.%20Valid%20Parentheses/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  - Stack and Hashmap to map parentheses
  - Loop through every char and check if it is open or close, add opens as needed and check stack if looking at close
  - Return whether we have no more opens in our stack or if we run into the wrong close

## Binary Search

**Binary Search** *([Problem](https://leetcode.com/problems/binary-search/) | [Solution](../Problems/0704.%20Binary%20Search/solution.py))*
- **Time Complexity:** O(logn)
- **Space Complexity:** O(1)
- **Notes:**
  - Two pointers and loop until they cross, it's okay if they're equal
  - If the middle pointer is less than target, update right pointer
  - Else means middle pointer is greater than target, update left pointer

**Search a 2D Matrix** *([Problem](https://leetcode.com/problems/search-a-2d-matrix/) | [Solution](../Problems/0074.%20Search%20a%202D%20Matrix/solution.py))*
- **Time Complexity:** O(lognm)
- **Space Complexity:** O(1)
- **Notes:**
  - Four pointers, 2 for rows top and bottom, 2 for columns left and right
  - Loop until the row pointers cross, it's okay if they're equal, get middle row
  - If the first value in the middle row is less than target, update bottom row
  - If the last value in the middle row is greater than target, update top row
  - Else, means target must be in row and perform traditional binary search

**Koko Eating Bananas** *([Problem](https://leetcode.com/problems/koko-eating-bananas/) | [Solution](../Problems/0875.%20Koko%20Eating%20Bananas/solution.py))*
- **Time Complexity:** O(lognm)
- **Space Complexity:** O(1)
- **Notes:**
  - Two pointers, between values 1 and max rate per hour
  - Loop until pointers cross, it's okay if they're equal
  - Calculate total hours it takes to eat all bananas with middle rate (math.ceil(float(x) / m))
  - If valid, update right pointer
  - Else this means we didn't finish eating in time, update left (to eat more per hour)

**Find Minimum In Rotated Sorted Array** *([Problem](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Solution](../Problems/0153.%20Find%20Minimum%20In%20Rotated%20Sorted%20Array/solution.py))*
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Notes:**
  - Two pointers, loop until they cross
  - If our middle pointer is less than our right, its impossible to have a smaller number than middle
  - Else means it is greater and our right subarray has the smaller value than our middle
  - Last case, middle and left pointer will be the same, and if it's greater than our right, l = m + 1 = r, next iteration pointers cross

**Search In Rotated Sorted Array** *([Problem](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Solution](../Problems/0033.%20Search%20In%20Rotated%20Sorted%20Array/solution.py))*
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

## Linked List

**Reverse Linked List** *([Problem](https://leetcode.com/problems/reverse-linked-list/) | [Solution](../Problems/0206.%20Reverse%20Linked%20List/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Think of creating a new List starting with None, and redirecting every node to point to that new list 1 by 1
  - Update our current nodes next to point to our previous
  - Change our prevous pointer to be our current node (to continue iterating)
  - Change our old current nodes next (before we changed it) to be our new current

**Merge Two Sorted Lists** *([Problem](https://leetcode.com/problems/merge-two-sorted-lists/) | [Solution](../Problems/0021.%20Merge%20Two%20Sorted%20Lists/solution.py))*
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(1)
- **Notes:**
  - 1) Edge case, 2) determine head node, 3) merge loop, 4) attach rest
  - Edge case if lists are None
  - Compare list.val and set as head and tail, move to next node in list we took node from
  - Loop while both lists have nodes, attaching smaller node to tail.next and updating tail to tail.next
  - Tail.next is the node that is not None

**Linked List Cycle** *([Problem](https://leetcode.com/problems/linked-list-cycle/) | [Solution](../Problems/0141.%20Linked%20List%20Cycle/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Slow/fast pointers
  - Loop until fast and its next are None constantly checking if the pointers nodes are ever equal

**Reorder List** *([Problem](https://leetcode.com/problems/reorder-list/) | [Solution](../Problems/0143.%20Reorder%20List/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Slow/fast pointers, reverse second half, merge lists:
  - Slow/fast pointers to find second half, slow.next is our start second half, fast to find our end bound
  - Then we need to reverse the links so we start at the end and point to the middle (second half points backwards)
  - While second, save next nodes, change the nodes our currents point to, update our current nodes to temps

**Remove Nth Node From End of List** *([Problem](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [Solution](../Problems/0019.%20Remove%20Nth%20Node%20From%20End%20of%20List/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  - Slow/fast pointers, slow = head, fast = n
  - If n is the size of the list (meaning fast is None) return the next node after the head
  - Else we loop until the node after fast is None (because we want slow to point to the node before our nth end node)
  - Then, redirect links

**Merge K Sorted Lists** *([Problem](https://leetcode.com/problems/merge-k-sorted-lists/) | [Solution](../Problems/0023.%20Merge%20K%20Sorted%20Lists/solution.py))*
- **Time Complexity:** O(n log k)
- **Space Complexity:** O(log k)
- **Notes:**
  - Two pointers, Divide and conquer (recursive)
  - Divide: Get the range of lists, divide until we only look at 1 which is sorted (pointers are same)
  - Two pointers/conquer: Used to look at two nodes from divide and begin merging sorted lists into 1 sorted list
  - Key: Recursivly divide until we only have a list from both left and right halves, then slowly merge them until we have 1 resulting list

## Trees

**Invert Binary Tree** *([Problem](https://leetcode.com/problems/invert-binary-tree/) | [Solution](../Problems/0226.%20Invert%20Binary%20Tree/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:** 1) Edge case, 2) swap left and right nodes, 3) Recursively call on both left and right nodes (the ones we changed)

**Maximum Depth of Binary Tree** *([Problem](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Solution](../Problems/0104.%20Maximum%20Depth%20of%20Binary%20Tree/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(h) - O(log n), O(n)
- **Notes:**
  - Case 1 (no node): if root is None, that side of the tree is empty, so depth = 0.
  - Case 2 (node exists): return 1 (for the current node) plus the max depth of the left and right subtrees.

**Same Tree** *([Problem](https://leetcode.com/problems/same-tree/) | [Solution](../Problems/0100.%20Same%20Tree/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  - Base case: return true if nodes are null
  - Then if both not null and equal, recursively return the comparision of the left and right nodes of both trees
  - Otherwise, false

**Subtree of Another Tree** *([Problem](https://leetcode.com/problems/subtree-of-another-tree/) | [Solution](../Problems/0572.%20Subtree%20of%20Another%20Tree/solution.py))*
- **Time Complexity:** O(nm)
- **Space Complexity:** O(n + m)
- **Notes:**
  - Iterate the tree using a basic stack or recursive call
  - If found subtree, perform same tree check (either recursively with a seperate function or iteratively with a stack)

**Lowest Common Ancestor of a Binary Search Tree** *([Problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [Solution](../Problems/0235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree/solution.py))*
- **Time Complexity:** O(h)
- **Space Complexity:** O(1)
- **Notes:**
  - Case 1: Both nodes are greater than our current node, we go right
  - Case 2: Both nodes are less than our current node, we go left
  - Case 3: This means a split occured (one node is to the left and the other is to the right) or one node equals our current, LCA found

**Binary Tree Level Order Traversal** *([Problem](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Solution](../Problems/0102.%20Binary%20Tree%20Level%20Order%20Traversal/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  - Iterate the tree using a queue while loop
  - Get the amount of nodes at that depth (length of queue)
  - For every node at that depth, pop it (queue.popleft()), and add it to a temp list for that depth if not null
  - If the temp list is not null (meaning nodes were present at that depth, add the temp list to the result list

**Validate Binary Search Tree** *([Problem](https://leetcode.com/problems/validate-binary-search-tree/) | [Solution](../Problems/0098.%20Validate%20Binary%20Search%20Tree/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  - Nested function with 3 parameters (node, left bound, right bound):
  - Our first root node can be in between negative infinity and infinity
  - As we iterate recursively, we must update our left and right bounds accordingly
  - Going left, update right bound to previous nodes value
  - Going right, update left bound to previous nodes value

**Kth Smallest Element In a Bst** *([Problem](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [Solution](../Problems/0230.%20Kth%20Smallest%20Element%20In%20a%20Bst/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  - Inorder Traversal: Loop while stack or node we're looking at is not null
  - Go left as far as possible, pushing nodes onto a stack
  - Then, begin popping the smallest value, decrementing k, and going to that nodes's right child

**Construct Binary Tree From Preorder And Inorder Traversal** *([Problem](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [Solution](../Problems/0105.%20Construct%20Binary%20Tree%20From%20Preorder%20And%20Inorder%20Traversal/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  - Idea: Preorder gives the root; Inorder tells us how to split into subtress
  - Make a Inorder index dictonary to map the inorder values to indices for O(1) loopups
  - Nested recursive function with four pointer parameters: preorder left and right, inorder left and right
  - Base case: Make sure that our left pointers for both preorder and in order do not cross eachother (okay is equal)
  - Root: Always build our root node with the preorder list index at our preorder left pointer
  - Split: We find the index of that value in the preorder list, in the inorder list (rootIndex) using our dictionary
  - Left Size (leftHalf): Compute how many nodes are in the left subtree by subtracting the inorder index (root Index) by our inorder left pointer
  - Recurse Left:
  - preLeft: Move forward by 1 (skip over the root in preorder).
  - preRight: Move our pointer to our current preLeft + the number of nodes in the leftHalf
  - inLeft: Keep the same inLeft
  - inRight: Move our pointer to the middle (rootIndex) - 1 to exclude our current root node (everything to the left of the root in inorder)
  - Recurse Right:
  - preLeft: Move the pointer over by 1 + our current preLeft + the length of the leftHalf
  - preRight: Keep the same preRight
  - inLeft: Move our pointer to the rootIndex + 1 (everything to the right of the root in inorder).
  - inRight: Keep the same inRight
  - Note: Only compare or use index values together if they are part of the same list

**Binary Tree Maximum Path Sum** *([Problem](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [Solution](../Problems/0124.%20Binary%20Tree%20Maximum%20Path%20Sum/solution.py))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(h) or log(n)
- **Notes:**
  - Idea: Recurse through every node and return 2 things:
  - The highest count path you can extend upwards (straight path)
  - We return our current nodes value + either the left path, right path, or 0 (if the left and right path are 0)
  - The best count path you can find anywhere in the tree (split path)
  - We return either our current best count, or our current nodes value + left path + right path
  - Base case: if the node is null, return 0 and -infinity as the best count path (anything is better than a null node)

**Serialize And Deserialize Binary Tree** *([Problem](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [Solution](../Problems/0297.%20Serialize%20And%20Deserialize%20Binary%20Tree/solution.py))*
- _No details provided._

## Backtracking

**Combination Sum** *([Problem](https://leetcode.com/problems/combination-sum/) | [Solution](../Problems/0039.%20Combination%20Sum/solution.py))*
- _No details provided._

**Word Search** *([Problem](https://leetcode.com/problems/word-search/) | [Solution](../Problems/0079.%20Word%20Search/solution.py))*
- _No details provided._

## Tries

**Implement Trie Prefix Tree** *([Problem](https://leetcode.com/problems/implement-trie-prefix-tree/) | [Solution](../Problems/0208.%20Implement%20Trie%20Prefix%20Tree/solution.py))*
- _No details provided._

**Design Add And Search Words Data Structure** *([Problem](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | [Solution](../Problems/0211.%20Design%20Add%20And%20Search%20Words%20Data%20Structure/solution.py))*
- _No details provided._

**Word Search II** *([Problem](https://leetcode.com/problems/word-search-ii/) | [Solution](../Problems/0212.%20Word%20Search%20II/solution.py))*
- _No details provided._

## Graphs

**Number of Islands** *([Problem](https://leetcode.com/problems/number-of-islands/) | [Solution](../Problems/0200.%20Number%20of%20Islands/solution.py))*
- **Time Complexity:** O(n): O(row * col)
- **Space Complexity:** O(n): O(row * col)
- **Notes:**
  - Idea: Iterate through each coordinate (row and col) in grid/matrix and run bfs or dfs every time we see a unvisited island coordinate (not in set)
  - BFS or DFS: Logic works for both below but bfs pops left vs. dfs pops right
  - Add the first coordinate to our visited set and to our queue (collections.deque)
  - While loop as long as we have valid coordinates in our queue
  - For loop to check all directions (left/right/up/down) of our current coordinates, if any of those coordinates:
  - Are within our row and col bounds (0 to the length of 0-indexed range)
  - Is an island in our grid (grid[row][col] == "x")
  - And is not in our visited set
  - Means: we found another valid coordinate a part of this island, and we update our visited set and queue with those coordinates to reiterate
  - Otherwise: we do nothing until the queue is empty

**Clone Graph** *([Problem](https://leetcode.com/problems/clone-graph/) | [Solution](../Problems/0133.%20Clone%20Graph/solution.py))*
- **Time Complexity:** O(V * E)
- **Space Complexity:** O(V)
- **Notes:**
  - Idea: Recursively clone each node using the old node and returning the cloned node (whether it's already cloned or not):
  - 1) If the old node is already in the map, return its clone (because our recursive call takes in the old node)
  - 2) Otherwise, create the clone and update our hashmap (old : new) that the node has been copied.
  - 3) For each neighbor of the old node, get the neighbor’s clone by recursion and append it to the current clone’s neighbors
  - Question: Why the hashmap?
  - Answer: It is both the visited check and the way to fetch the exact clone needed to wire edges (when we are updating neighbors of already cloned nodes)

**Pacific Atlantic Water Flow** *([Problem](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [Solution](../Problems/0417.%20Pacific%20Atlantic%20Water%20Flow/solution.py))*
- _No details provided._

**Course Schedule** *([Problem](https://leetcode.com/problems/course-schedule/) | [Solution](../Problems/0207.%20Course%20Schedule/solution.py))*
- _No details provided._

**Graph Valid Tree** *([Problem](https://leetcode.com/problems/graph-valid-tree/) | [Solution](../Problems/0261.%20Graph%20Valid%20Tree/solution.py))*
- _No details provided._

**Number of Connected Components In An Undirected Graph** *([Problem](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [Solution](../Problems/0323.%20Number%20of%20Connected%20Components%20In%20An%20Undirected%20Graph/solution.py))*
- _No details provided._

## Advanced Graphs

**Alien Dictionary** *([Problem](https://leetcode.com/problems/alien-dictionary/) | [Solution](../Problems/0269.%20Alien%20Dictionary/solution.py))*
- _No details provided._

## 1-D Dynamic Programming

**Climbing Stairs** *([Problem](https://leetcode.com/problems/climbing-stairs/) | [Solution](../Problems/0070.%20Climbing%20Stairs/solution.py))*
- _No details provided._

**House Robber** *([Problem](https://leetcode.com/problems/house-robber/) | [Solution](../Problems/0198.%20House%20Robber/solution.py))*
- _No details provided._

**House Robber II** *([Problem](https://leetcode.com/problems/house-robber-ii/) | [Solution](../Problems/0213.%20House%20Robber%20II/solution.py))*
- _No details provided._

**Longest Palindromic Substring** *([Problem](https://leetcode.com/problems/longest-palindromic-substring/) | [Solution](../Problems/0005.%20Longest%20Palindromic%20Substring/solution.py))*
- _No details provided._

**Palindromic Substrings** *([Problem](https://leetcode.com/problems/palindromic-substrings/) | [Solution](../Problems/0647.%20Palindromic%20Substrings/solution.py))*
- _No details provided._

**Decode Ways** *([Problem](https://leetcode.com/problems/decode-ways/) | [Solution](../Problems/0091.%20Decode%20Ways/solution.py))*
- _No details provided._

**Coin Change** *([Problem](https://leetcode.com/problems/coin-change/) | [Solution](../Problems/0322.%20Coin%20Change/solution.py))*
- _No details provided._

**Maximum Product Subarray** *([Problem](https://leetcode.com/problems/maximum-product-subarray/) | [Solution](../Problems/0152.%20Maximum%20Product%20Subarray/solution.py))*
- _No details provided._

**Word Break** *([Problem](https://leetcode.com/problems/word-break/) | [Solution](../Problems/0139.%20Word%20Break/solution.py))*
- _No details provided._

**Longest Increasing Subsequence** *([Problem](https://leetcode.com/problems/longest-increasing-subsequence/) | [Solution](../Problems/0300.%20Longest%20Increasing%20Subsequence/solution.py))*
- _No details provided._

## 2-D Dynamic Programming

**Unique Paths** *([Problem](https://leetcode.com/problems/unique-paths/) | [Solution](../Problems/0062.%20Unique%20Paths/solution.py))*
- _No details provided._

**Longest Common Subsequence** *([Problem](https://leetcode.com/problems/longest-common-subsequence/) | [Solution](../Problems/1143.%20Longest%20Common%20Subsequence/solution.py))*
- _No details provided._

## Greedy

**Maximum Subarray** *([Problem](https://leetcode.com/problems/maximum-subarray/) | [Solution](../Problems/0053.%20Maximum%20Subarray/solution.py))*
- _No details provided._

**Jump Game** *([Problem](https://leetcode.com/problems/jump-game/) | [Solution](../Problems/0055.%20Jump%20Game/solution.py))*
- _No details provided._

## Intervals

**Insert Interval** *([Problem](https://leetcode.com/problems/insert-interval/) | [Solution](../Problems/0057.%20Insert%20Interval/solution.py))*
- _No details provided._

**Merge Intervals** *([Problem](https://leetcode.com/problems/merge-intervals/) | [Solution](../Problems/0056.%20Merge%20Intervals/solution.py))*
- _No details provided._

**Non Overlapping Intervals** *([Problem](https://leetcode.com/problems/non-overlapping-intervals/) | [Solution](../Problems/0435.%20Non%20Overlapping%20Intervals/solution.py))*
- _No details provided._

**Meeting Rooms** *([Problem](https://leetcode.com/problems/meeting-rooms/) | [Solution](../Problems/0252.%20Meeting%20Rooms/solution.py))*
- _No details provided._

**Meeting Rooms II** *([Problem](https://leetcode.com/problems/meeting-rooms-ii/) | [Solution](../Problems/0253.%20Meeting%20Rooms%20II/solution.py))*
- _No details provided._

## Math & Geometry

**Rotate Image** *([Problem](https://leetcode.com/problems/rotate-image/) | [Solution](../Problems/0048.%20Rotate%20Image/solution.py))*
- _No details provided._

**Spiral Matrix** *([Problem](https://leetcode.com/problems/spiral-matrix/) | [Solution](../Problems/0054.%20Spiral%20Matrix/solution.py))*
- _No details provided._

**Set Matrix Zeroes** *([Problem](https://leetcode.com/problems/set-matrix-zeroes/) | [Solution](../Problems/0073.%20Set%20Matrix%20Zeroes/solution.py))*
- _No details provided._

## Bit Manipulation

**Number of 1 Bits** *([Problem](https://leetcode.com/problems/number-of-1-bits/) | [Solution](../Problems/0191.%20Number%20of%201%20Bits/solution.py))*
- _No details provided._

**Counting Bits** *([Problem](https://leetcode.com/problems/counting-bits/) | [Solution](../Problems/0338.%20Counting%20Bits/solution.py))*
- _No details provided._

**Reverse Bits** *([Problem](https://leetcode.com/problems/reverse-bits/) | [Solution](../Problems/0190.%20Reverse%20Bits/solution.py))*
- _No details provided._

**Missing Number** *([Problem](https://leetcode.com/problems/missing-number/) | [Solution](../Problems/0268.%20Missing%20Number/solution.py))*
- _No details provided._

**Sum of Two Integers** *([Problem](https://leetcode.com/problems/sum-of-two-integers/) | [Solution](../Problems/0371.%20Sum%20of%20Two%20Integers/solution.py))*
- _No details provided._

## Heap

**Find Median From Data Stream** *([Problem](https://leetcode.com/problems/find-median-from-data-stream/) | [Solution](../Problems/0295.%20Find%20Median%20From%20Data%20Stream/solution.py))*
- _No details provided._

## Priority Queue

**Find Median From Data Stream** *([Problem](https://leetcode.com/problems/find-median-from-data-stream/) | [Solution](../Problems/0295.%20Find%20Median%20From%20Data%20Stream/solution.py))*
- _No details provided._