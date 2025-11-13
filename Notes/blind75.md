# Blind 75 Notes

<!-- AUTO-GENERATED FILE. DO NOT EDIT MANUALLY. -->
*Last updated: 2025-11-13 13:28 UTC*

[Source spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vRw_Ro70SyoCP4FIHwwfkDdwVhXWU_lKwfl6Rw3tXlD1nFD5gfPVk1B0SufuQATexITGzPiwNmeUav0/pub?output=csv
)

## Array & Hashing

**Contains Duplicate** *([Problem](https://leetcode.com/problems/contains-duplicate/) | [Solution](../Problems/0217.%20Contains%20Duplicate))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:** Hashset, check if the value is in seen otherwise, add it to seen

**Encode and Decode Strings** *([Problem](https://leetcode.com/problems/encode-and-decode-strings/) | [Solution](../Problems/0271.%20Encode%20and%20Decode%20Strings))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n + m)
- **Notes:**
  <ul>
    <li>Encode saving the new string as (length, unique char, string)</li>
    <li>Decode Looping until we hit our right bound, using pointers front, middle, and end
      <ul>
        <li>Front points to our first number for our string length</li>
        <li>Middle points to our unique char</li>
        <li>End points to the end of our string</li>
      </ul>
    </li>
  </ul>

**Group Anagrams** *([Problem](https://leetcode.com/problems/group-anagrams/) | [Solution](../Problems/0049.%20Group%20Anagrams))*
- **Time Complexity:** O(nm)
- **Space Complexity:** O(nm)
- **Notes:**
  <ul>
    <li>Loop through strings storing list of counts as the key and string as value (defaultdict(list))</li>
    <li>ASCII values for count</li>
  </ul>

**Longest Consecutive Sequence** *([Problem](https://leetcode.com/problems/longest-consecutive-sequence/) | [Solution](../Problems/0128.%20Longest%20Consecutive%20Sequence))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Use a set to iterate quickly</li>
    <li>Loop over every unique number
      <ul>
        <li>Check if it is a start of a sequence</li>
        <li>If it is, continue to check the numbers after if it is a sequence
          <ul>
            <li>Then compare it to the length of the max</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

**Product of Array Except Self** *([Problem](https://leetcode.com/problems/product-of-array-except-self/) | [Solution](../Problems/0238.%20Product%20of%20Array%20Except%20Self))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n)
- **Notes:**
  <ul>
    <li>Result list</li>
    <li>Prefix, equal first then multiply update</li>
    <li>Postfix, multiply first then multiply update</li>
  </ul>

**Top K Frequent Elements** *([Problem](https://leetcode.com/problems/top-k-frequent-elements/) | [Solution](../Problems/0347.%20Top%20K%20Frequent%20Elements))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Hashmap for count and dict of lists per number in input list storing count as key and number as values</li>
    <li>Loop to get count of each number</li>
    <li>Loop to store each number and its count in dict</li>
    <li>Return the k most frequent numbers</li>
  </ul>

**Two Sum** *([Problem](https://leetcode.com/problems/two-sum/) | [Solution](../Problems/0001.%20Two%20Sum))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Loop through every value
      <ul>
        <li>If our target - the value we are looking at is in our hashmap of seen values, return them</li>
        <li>Otherwise, add it to our hashmap</li>
      </ul>
    </li>
  </ul>

**Valid Anagram** *([Problem](https://leetcode.com/problems/valid-anagram/) | [Solution](../Problems/0242.%20Valid%20Anagram))*
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two ways to solve this:
      <ol type="1">
        <li>Hashmaps to keep track of char count and then compare</li>
        <li>ASCII values list, adding count of 1 and subtracting count of 2, at the end, the list should have counts of all 0s</li>
      </ol>
    </li>
  </ul>

## Two Pointers

**Container With Most Water** *([Problem](https://leetcode.com/problems/container-with-most-water/) | [Solution](../Problems/0011.%20Container%20With%20Most%20Water))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two pointers</li>
    <li>Loop through ends (pointers)</li>
    <li>Calculate area</li>
    <li>Update pointers based on which value is smaller</li>
  </ul>

**Three Sum** *([Problem](https://leetcode.com/problems/3sum/) | [Solution](../Problems/0015.%20Three%20Sum))*
- **Time Complexity:** O(n^2)
- **Space Complexity:** O(1) or O(n)
- **Notes:**
  <ul>
    <li>Result list and sort the input list
      <ul>
        <li>Enumerate though each value in the list</li>
        <li>Check if the smallest value is greater than target</li>
        <li>After the first iteration, check if prev value is the same as current value</li>
        <li>Loop through pointers which are the ends after the value we enumerate</li>
        <li>Calculate threeSum, and update pointers based on whether equal, greater or less than target
          <ul>
            <li>When equal, update both pointers and duplicate check</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

**Two Sum II Input Array Is Sorted** *([Problem](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Solution](../Problems/0167.%20Two%20Sum%20II%20Input%20Array%20Is%20Sorted))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Loop 2 pointers
      <ul>
        <li>Calculate twoSum, and update pointers based on whether greater or less than target</li>
      </ul>
    </li>
  </ul>

**Valid Palindrome** *([Problem](https://leetcode.com/problems/valid-palindrome/) | [Solution](../Problems/0125.%20Valid%20Palindrome))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Loop through Two pointers
      <ul>
        <li>Increment/decrement whether pointer value is within ascii values to avoid non numeric values</li>
        <li>Compare characters at pointer values</li>
        <li>Update pointers</li>
      </ul>
    </li>
  </ul>

## Sliding Window

**Best Time to Buy and Sell Stock** *([Problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Solution](../Problems/0121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two pointers
      <ul>
        <li>Loop until our sell pointer crosses input array bounds</li>
        <li>If sell is greater than buy, get the max of our old and current profit</li>
        <li>Otherwise, this means we have a new low buy, so update pointers accordingly</li>
      </ul>
    </li>
  </ul>

**Longest Repeating Character Replacement** *([Problem](https://leetcode.com/problems/longest-repeating-character-replacement/) | [Solution](../Problems/0424.%20Longest%20Repeating%20Character%20Replacement))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(m)
- **Notes:**
  <ul>
    <li>Dictionary to store unique letters as keys and counts as values</li>
    <li>Two pointers, loop with right pointer, update counts and max length
      <ul>
        <li>While the most frequency letter plus k is less than the length of the string
          <ul>
            <li>Update the letters count and left pointer</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

**Longest Substring Without Repeating Characters** *([Problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Solution](../Problems/0003.%20Longest%20Substring%20Without%20Repeating%20Characters))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(m)
- **Notes:**
  <ul>
    <li>Hashmap to store char as key and its index as the value</li>
    <li>Two pointers
      <ul>
        <li>Loop through our right pointer, adding them to hashmap</li>
        <li>If duplicate (already in seen) & last seen duplicate char index greater than our left pointer</li>
        <li>Update left pointer to last seen duplicate char index + 1 (to skip it)</li>
      </ul>
    </li>
  </ul>

**Minimum Window Substring** *([Problem](https://leetcode.com/problems/minimum-window-substring/) | [Solution](../Problems/0076.%20Minimum%20Window%20Substring))*
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(m)
- **Notes:**
  <ul>
    <li>Check if are target substring is empty else continue</li>
    <li>Hashmaps for window and target substring</li>
    <li>Two pointers, loop until our right pointer hits the right bound (end of input string)
      <ul>
        <li>Continously add unique char and their count to our window</li>
        <li>If we have the count for all the unique letters we need save it if is it smaller than our old substring</li>
        <li>Update our left pointer and decrease the count until we don't have what we need anymore</li>
      </ul>
    </li>
  </ul>

## Stack

**Valid Parentheses** *([Problem](https://leetcode.com/problems/valid-parentheses/) | [Solution](../Problems/0020.%20Valid%20Parentheses))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Stack and Hashmap to map parentheses
      <ul>
        <li>Loop through every char and check if it is open or close, add opens as needed and check stack if looking at close</li>
        <li>Return whether we have no more opens in our stack or if we run into the wrong close</li>
      </ul>
    </li>
  </ul>

## Binary Search

**Binary Search** *([Problem](https://leetcode.com/problems/binary-search/) | [Solution](../Problems/0704.%20Binary%20Search))*
- **Time Complexity:** O(logn)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two pointers and loop until they cross, it's okay if they're equal
      <ul>
        <li>If the middle pointer is less than target, update right pointer</li>
        <li>Else means middle pointer is greater than target, update left pointer</li>
      </ul>
    </li>
  </ul>

**Find Minimum In Rotated Sorted Array** *([Problem](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Solution](../Problems/0153.%20Find%20Minimum%20In%20Rotated%20Sorted%20Array))*
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two pointers, loop until they cross
      <ul>
        <li>If our middle pointer is less than our right, its impossible to have a smaller number than middle</li>
        <li>Else means it is greater and our right subarray has the smaller value than our middle</li>
        <li>Last case, middle and left pointer will be the same, and if it's greater than our right, l = m + 1 = r, next iteration pointers cross</li>
      </ul>
    </li>
  </ul>

**Koko Eating Bananas** *([Problem](https://leetcode.com/problems/koko-eating-bananas/) | [Solution](../Problems/0875.%20Koko%20Eating%20Bananas))*
- **Time Complexity:** O(lognm)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two pointers, between values 1 and max rate per hour
      <ul>
        <li>Loop until pointers cross, it's okay if they're equal</li>
        <li>Calculate total hours it takes to eat all bananas with middle rate (math.ceil(float(x) / m))</li>
        <li>If valid, update right pointer</li>
        <li>Else this means we didn't finish eating in time, update left (to eat more per hour)</li>
      </ul>
    </li>
  </ul>

**Search a 2D Matrix** *([Problem](https://leetcode.com/problems/search-a-2d-matrix/) | [Solution](../Problems/0074.%20Search%20a%202D%20Matrix))*
- **Time Complexity:** O(lognm)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Four pointers, 2 for rows top and bottom, 2 for columns left and right
      <ul>
        <li>Loop until the row pointers cross, it's okay if they're equal, get middle row</li>
        <li>If the first value in the middle row is less than target, update bottom row</li>
        <li>If the last value in the middle row is greater than target, update top row</li>
        <li>Else, means target must be in row and perform traditional binary search</li>
      </ul>
    </li>
  </ul>

**Search In Rotated Sorted Array** *([Problem](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Solution](../Problems/0033.%20Search%20In%20Rotated%20Sorted%20Array))*
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two pointers and loop until they cross, it's okay if they're equal
      <ul>
        <li>If our middle is the target, return, otherwise, two subcases</li>
        <li>Elif middle is greater than our left pointer (left side is sorted)
          <ul>
            <li>And If our target is greater than our middle pointer or less than our left pointer (meaning it's not in our sorted side), update left</li>
            <li>Else, our target is in our sorted side and update right</li>
          </ul>
        </li>
        <li>Else, meaning our right side is sorted
          <ul>
            <li>And our target is less than our middle pointer but greater than our right pointer (meaning it's not in our sorted sid), update right</li>
            <li>Else, our target is in our sorted side and update left</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

## Linked List

**Linked List Cycle** *([Problem](https://leetcode.com/problems/linked-list-cycle/) | [Solution](../Problems/0141.%20Linked%20List%20Cycle))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Slow/fast pointers
      <ul>
        <li>Loop until fast and its next are None constantly checking if the pointers nodes are ever equal</li>
      </ul>
    </li>
  </ul>

**Merge K Sorted Lists** *([Problem](https://leetcode.com/problems/merge-k-sorted-lists/) | [Solution](../Problems/0023.%20Merge%20K%20Sorted%20Lists))*
- **Time Complexity:** O(n log k)
- **Space Complexity:** O(log k)
- **Notes:**
  <ul>
    <li>Two pointers, Divide and conquer (recursive)
      <ul>
        <li>Divide: Get the range of lists, divide until we only look at 1 which is sorted (pointers are same)</li>
        <li>Two pointers/conquer: Used to look at two nodes from divide and begin merging sorted lists into 1 sorted list</li>
      </ul>
    </li>
    <li>Key: Recursivly divide until we only have a list from both left and right halves, then slowly merge them until we have 1 resulting list</li>
  </ul>

**Merge Two Sorted Lists** *([Problem](https://leetcode.com/problems/merge-two-sorted-lists/) | [Solution](../Problems/0021.%20Merge%20Two%20Sorted%20Lists))*
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>1) Edge case, 2) determine head node, 3) merge loop, 4) attach rest
      <ul>
        <li>Edge case if lists are None</li>
        <li>Compare list.val and set as head and tail, move to next node in list we took node from</li>
        <li>Loop while both lists have nodes, attaching smaller node to tail.next and updating tail to tail.next</li>
        <li>Tail.next is the node that is not None</li>
      </ul>
    </li>
  </ul>

**Remove Nth Node From End of List** *([Problem](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [Solution](../Problems/0019.%20Remove%20Nth%20Node%20From%20End%20of%20List))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Slow/fast pointers, slow = head, fast = n
      <ul>
        <li>If n is the size of the list (meaning fast is None) return the next node after the head</li>
        <li>Else we loop until the node after fast is None (because we want slow to point to the node before our nth end node)
          <ul>
            <li>Then, redirect links</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

**Reorder List** *([Problem](https://leetcode.com/problems/reorder-list/) | [Solution](../Problems/0143.%20Reorder%20List))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Slow/fast pointers, reverse second half, merge lists:
      <ul>
        <li>Slow/fast pointers to find second half, slow.next is our start second half, fast to find our end bound</li>
        <li>Then we need to reverse the links so we start at the end and point to the middle (second half points backwards)</li>
        <li>While second, save next nodes, change the nodes our currents point to, update our current nodes to temps</li>
      </ul>
    </li>
  </ul>

**Reverse Linked List** *([Problem](https://leetcode.com/problems/reverse-linked-list/) | [Solution](../Problems/0206.%20Reverse%20Linked%20List))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Think of creating a new List starting with None, and redirecting every node to point to that new list 1 by 1
      <ul>
        <li>Update our current nodes next to point to our previous</li>
        <li>Change our prevous pointer to be our current node (to continue iterating)</li>
        <li>Change our old current nodes next (before we changed it) to be our new current</li>
      </ul>
    </li>
  </ul>

## Trees

**Binary Tree Level Order Traversal** *([Problem](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Solution](../Problems/0102.%20Binary%20Tree%20Level%20Order%20Traversal))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Iterate the tree using a queue while loop
      <ul>
        <li>Get the amount of nodes at that depth (length of queue)</li>
        <li>For every node at that depth, pop it (queue.popleft()), and add it to a temp list for that depth if not null</li>
        <li>If the temp list is not null (meaning nodes were present at that depth, add the temp list to the result list</li>
      </ul>
    </li>
  </ul>

**Binary Tree Maximum Path Sum** *([Problem](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [Solution](../Problems/0124.%20Binary%20Tree%20Maximum%20Path%20Sum))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(h) or log(n)
- **Notes:**
  <ul>
    <li>Idea: Recurse through every node and return 2 things:
      <ul>
        <li>The highest count path you can extend upwards (straight path)
          <ul>
            <li>We return our current nodes value + either the left path, right path, or 0 (if the left and right path are 0)</li>
          </ul>
        </li>
        <li>The best count path you can find anywhere in the tree (split path)
          <ul>
            <li>We return either our current best count, or our current nodes value + left path + right path</li>
          </ul>
        </li>
      </ul>
    </li>
    <li>Base case: if the node is null, return 0 and -infinity as the best count path (anything is better than a null node)</li>
  </ul>

**Construct Binary Tree From Preorder And Inorder Traversal** *([Problem](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [Solution](../Problems/0105.%20Construct%20Binary%20Tree%20From%20Preorder%20And%20Inorder%20Traversal))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Idea: Preorder gives the root; Inorder tells us how to split into subtress
      <ul>
        <li>Make a Inorder index dictonary to map the inorder values to indices for O(1) loopups</li>
        <li>Nested recursive function with four pointer parameters: preorder left and right, inorder left and right
          <ul>
            <li>Base case: Make sure that our left pointers for both preorder and in order do not cross eachother (okay is equal)</li>
            <li>Root: Always build our root node with the preorder list index at our preorder left pointer</li>
            <li>Split: We find the index of that value in the preorder list, in the inorder list (rootIndex) using our dictionary</li>
            <li>Left Size (leftHalf): Compute how many nodes are in the left subtree by subtracting the inorder index (root Index) by our inorder left pointer</li>
          </ul>
        </li>
      </ul>
    </li>
    <li>Recurse Left:
      <ul>
        <li>preLeft: Move forward by 1 (skip over the root in preorder).</li>
        <li>preRight: Move our pointer to our current preLeft + the number of nodes in the leftHalf</li>
        <li>inLeft: Keep the same inLeft</li>
        <li>inRight: Move our pointer to the middle (rootIndex) - 1 to exclude our current root node (everything to the left of the root in inorder)</li>
      </ul>
    </li>
    <li>Recurse Right:
      <ul>
        <li>preLeft: Move the pointer over by 1 + our current preLeft + the length of the leftHalf</li>
        <li>preRight: Keep the same preRight</li>
        <li>inLeft: Move our pointer to the rootIndex + 1 (everything to the right of the root in inorder).</li>
        <li>inRight: Keep the same inRight</li>
      </ul>
    </li>
    <li>Note: Only compare or use index values together if they are part of the same list</li>
  </ul>

**Invert Binary Tree** *([Problem](https://leetcode.com/problems/invert-binary-tree/) | [Solution](../Problems/0226.%20Invert%20Binary%20Tree))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:** 1) Edge case, 2) swap left and right nodes, 3) Recursively call on both left and right nodes (the ones we changed)

**Kth Smallest Element In a Bst** *([Problem](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [Solution](../Problems/0230.%20Kth%20Smallest%20Element%20In%20a%20Bst))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Inorder Traversal: Loop while stack or node we're looking at is not null
      <ul>
        <li>Go left as far as possible, pushing nodes onto a stack</li>
        <li>Then, begin popping the smallest value, decrementing k, and going to that nodes's right child</li>
      </ul>
    </li>
  </ul>

**Lowest Common Ancestor of a Binary Search Tree** *([Problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [Solution](../Problems/0235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree))*
- **Time Complexity:** O(h)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Case 1: Both nodes are greater than our current node, we go right</li>
    <li>Case 2: Both nodes are less than our current node, we go left</li>
    <li>Case 3: This means a split occured (one node is to the left and the other is to the right) or one node equals our current, LCA found</li>
  </ul>

**Maximum Depth of Binary Tree** *([Problem](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Solution](../Problems/0104.%20Maximum%20Depth%20of%20Binary%20Tree))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(h) - O(log n), O(n)
- **Notes:**
  <ul>
    <li>Case 1 (no node): if root is None, that side of the tree is empty, so depth = 0.</li>
    <li>Case 2 (node exists): return 1 (for the current node) plus the max depth of the left and right subtrees.</li>
  </ul>

**Same Tree** *([Problem](https://leetcode.com/problems/same-tree/) | [Solution](../Problems/0100.%20Same%20Tree))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Base case: return true if nodes are null
      <ul>
        <li>Then if both not null and equal, recursively return the comparision of the left and right nodes of both trees</li>
        <li>Otherwise, false</li>
      </ul>
    </li>
  </ul>

**Serialize And Deserialize Binary Tree** *([Problem](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [Solution](../Problems/0297.%20Serialize%20And%20Deserialize%20Binary%20Tree))*
- _No details provided._

**Subtree of Another Tree** *([Problem](https://leetcode.com/problems/subtree-of-another-tree/) | [Solution](../Problems/0572.%20Subtree%20of%20Another%20Tree))*
- **Time Complexity:** O(nm)
- **Space Complexity:** O(n + m)
- **Notes:**
  <ul>
    <li>Iterate the tree using a basic stack or recursive call
      <ul>
        <li>If found subtree, perform same tree check (either recursively with a seperate function or iteratively with a stack)</li>
      </ul>
    </li>
  </ul>

**Validate Binary Search Tree** *([Problem](https://leetcode.com/problems/validate-binary-search-tree/) | [Solution](../Problems/0098.%20Validate%20Binary%20Search%20Tree))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Nested function with 3 parameters (node, left bound, right bound):
      <ul>
        <li>Our first root node can be in between negative infinity and infinity</li>
        <li>As we iterate recursively, we must update our left and right bounds accordingly
          <ul>
            <li>Going left, update right bound to previous nodes value</li>
            <li>Going right, update left bound to previous nodes value</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

## Backtracking

**Combination Sum** *([Problem](https://leetcode.com/problems/combination-sum/) | [Solution](../Problems/0039.%20Combination%20Sum))*
- _No details provided._

**Word Search** *([Problem](https://leetcode.com/problems/word-search/) | [Solution](../Problems/0079.%20Word%20Search))*
- _No details provided._

## Tries

**Design Add And Search Words Data Structure** *([Problem](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | [Solution](../Problems/0211.%20Design%20Add%20And%20Search%20Words%20Data%20Structure))*
- _No details provided._

**Implement Trie Prefix Tree** *([Problem](https://leetcode.com/problems/implement-trie-prefix-tree/) | [Solution](../Problems/0208.%20Implement%20Trie%20Prefix%20Tree))*
- _No details provided._

**Word Search II** *([Problem](https://leetcode.com/problems/word-search-ii/) | [Solution](../Problems/0212.%20Word%20Search%20II))*
- _No details provided._

## Graphs

**Clone Graph** *([Problem](https://leetcode.com/problems/clone-graph/) | [Solution](../Problems/0133.%20Clone%20Graph))*
- **Time Complexity:** O(V * E)
- **Space Complexity:** O(V)
- **Notes:**
  <ul>
    <li>Idea: Recursively clone each node using the old node and returning the cloned node (whether it's already cloned or not):
      <ol type="1">
        <li>If the old node is already in the map, return its clone (because our recursive call takes in the old node)</li>
        <li>Otherwise, create the clone and update our hashmap (old : new) that the node has been copied.</li>
        <li>For each neighbor of the old node, get the neighbor’s clone by recursion and append it to the current clone’s neighbors</li>
      </ol>
    </li>
    <li>Question: Why the hashmap?</li>
    <li>Answer: It is both the visited check and the way to fetch the exact clone needed to wire edges (when we are updating neighbors of already cloned nodes)</li>
  </ul>

**Course Schedule** *([Problem](https://leetcode.com/problems/course-schedule/) | [Solution](../Problems/0207.%20Course%20Schedule))*
- **Time Complexity:** O(V * E)
- **Space Complexity:** O(V * E)
- **Notes:**
  <ul>
    <li>Idea: Map course to its prerequisites, and run dfs on each prerequiste keeping track of the path
      <ol type="1">
        <li>Data structures: adjacency map (course to prerequisites); path set (path in our DFS process)</li>
        <li>Iteration: Run DFS on every course; If any returns false, return false.</li>
        <li>DFS:
          <ul>
            <li>Base case 1) If a course is already on our path (cycle), return false</li>
            <li>Base case 2) If a course has no prerequsites (completed), return true</li>
            <li>Otherwise: Add the course to our path and DFS on all prerequisites and:
              <ul>
                <li>If any of the DFS on prerequistes return false, return false</li>
                <li>Else memoize and remove all the prerequisites for that course</li>
              </ul>
            </li>
          </ul>
        </li>
      </ol>
    </li>
  </ul>

**Graph Valid Tree** *([Problem](https://leetcode.com/problems/graph-valid-tree/) | [Solution](../Problems/0261.%20Graph%20Valid%20Tree))*
- **Time Complexity:** O(V * E)
- **Space Complexity:** O(V * E)
- **Notes:**
  <ul>
    <li>Base Check: If the number of edges isn’t equal to the number of nodes minus one, the graph can’t be a valid tree</li>
    <li>Reason: After the first node, each added node needs exactly one new edge to connect them to be a valid tree
      <ol type="1">
        <li>Data Structures:
          <ul>
            <li>Adjacency List: Map nodes to neighbors and back</li>
            <li>Visited Set: Store every node visited for iteration/recursion using dfs/bfs</li>
          </ul>
        </li>
        <li>Run DFS on any node passing a current node and previous node as parameters:
          <ul>
            <li>Base case: Check if node is in visited</li>
            <li>For every neighbor the current node has, i
              <ul>
                <li>If the neighbor is the previous node, skip it</li>
                <li>If the DFS call on the neighbor nodes is false, return false (caught a cycle)</li>
              </ul>
            </li>
            <li>If the for loop preformed without failing, return True</li>
          </ul>
        </li>
        <li>Return the boolean result of both (and):
          <ul>
            <li>The DFS call</li>
            <li>Whether or not the number of visited nodes equals the total number of nodes (n)</li>
          </ul>
        </li>
      </ol>
    </li>
  </ul>

**Number of Connected Components In An Undirected Graph** *([Problem](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [Solutions](../Problems/0323.%20Number%20of%20Connected%20Components%20In%20An%20Undirected%20Graph))*
- **Time Complexity:** O(V * E)
- **Space Complexity:** O(V * E)
- **Notes:**
  <ol type="1">
    <li>Data Structures:
      <ul>
        <li>Adjacency List: Map nodes to neighbors and back</li>
        <li>Visited Set: Store every node visited for iteration/recursion dfs/bfs</li>
        <li>Components Count: Store amount of components detected</li>
      </ul>
    </li>
    <li>Linear Iteration:
      <ul>
        <li>For each node in the graph
          <ul>
            <li>If we have not visitied yet, mark it as visited, run DFS, and increment our components counter</li>
          </ul>
        </li>
      </ul>
    </li>
    <li>DFS:
      <ul>
        <li>For every neighbor the passed node has
          <ul>
            <li>If the neighbor is not in visited, mark it as visited and run DFS</li>
          </ul>
        </li>
      </ul>
    </li>
  </ol>

**Number of Islands** *([Problem](https://leetcode.com/problems/number-of-islands/) | [Solution](../Problems/0200.%20Number%20of%20Islands))*
- **Time Complexity:** O(n): O(row * col)
- **Space Complexity:** O(n): O(row * col)
- **Notes:**
  <ul>
    <li>Idea: Iterate through each coordinate (row and col) in grid/matrix and run bfs or dfs every time we see a unvisited island coordinate (not in set)</li>
    <li>BFS or DFS: Logic works for both below but bfs pops left vs. dfs pops right
      <ul>
        <li>Add the first coordinate to our visited set and to our queue (collections.deque)</li>
        <li>While loop as long as we have valid coordinates in our queue</li>
        <li>For loop to check all directions (left/right/up/down) of our current coordinates, if any of those coordinates:
          <ul>
            <li>Are within our row and col bounds (0 to the length of 0-indexed range)</li>
            <li>Is an island in our grid (grid[row][col] == "x")</li>
            <li>And is not in our visited set</li>
          </ul>
        </li>
        <li>Means: we found another valid coordinate a part of this island, and we update our visited set and queue with those coordinates to reiterate</li>
        <li>Otherwise: we do nothing until the queue is empty</li>
      </ul>
    </li>
  </ul>

**Pacific Atlantic Water Flow** *([Problem](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [Solution](../Problems/0417.%20Pacific%20Atlantic%20Water%20Flow))*
- **Time Complexity:** O(n): O(row * col)
- **Space Complexity:** O(n): O(row * col)
- **Notes:**
  <ul>
    <li>Idea: Iterate through top/bottom, left/right sides and recursively dfs go inward storing valid coordinates in sets (coordinates that are in a path to ocean)
      <ol type="1">
        <li>Top/Bottom: Iterate through cols and recursive dfs on every coordinate on the top and bottom row (0, rows -1)</li>
        <li>Left/Right: Iterate through rows and recursive dfs on every coordinate on the left and right cols (0, cols - 1)</li>
        <li>DFS: If the row/col is within bounds, the coordinate has a equal or greater height than our old, and is not already marked reachable:
          <ul>
            <li>Mark it as reachable for that respective ocean</li>
            <li>Recursively check all 4 directions</li>
          </ul>
        </li>
        <li>Result: Iterate over one ocean’s reachable set and add any cell that also appears in the other ocean’s set to the result</li>
      </ol>
    </li>
  </ul>

## Advanced Graphs

**Alien Dictionary** *([Problem](https://leetcode.com/problems/alien-dictionary/) | [Solution](../Problems/0269.%20Alien%20Dictionary))*
- _No details provided._

## 1-D Dynamic Programming

**Climbing Stairs** *([Problem](https://leetcode.com/problems/climbing-stairs/) | [Solution](../Problems/0070.%20Climbing%20Stairs))*
- _No details provided._

**Coin Change** *([Problem](https://leetcode.com/problems/coin-change/) | [Solution](../Problems/0322.%20Coin%20Change))*
- _No details provided._

**Decode Ways** *([Problem](https://leetcode.com/problems/decode-ways/) | [Solution](../Problems/0091.%20Decode%20Ways))*
- _No details provided._

**House Robber II** *([Problem](https://leetcode.com/problems/house-robber-ii/) | [Solution](../Problems/0213.%20House%20Robber%20II))*
- _No details provided._

**House Robber** *([Problem](https://leetcode.com/problems/house-robber/) | [Solution](../Problems/0198.%20House%20Robber))*
- _No details provided._

**Longest Increasing Subsequence** *([Problem](https://leetcode.com/problems/longest-increasing-subsequence/) | [Solution](../Problems/0300.%20Longest%20Increasing%20Subsequence))*
- _No details provided._

**Longest Palindromic Substring** *([Problem](https://leetcode.com/problems/longest-palindromic-substring/) | [Solution](../Problems/0005.%20Longest%20Palindromic%20Substring))*
- _No details provided._

**Maximum Product Subarray** *([Problem](https://leetcode.com/problems/maximum-product-subarray/) | [Solution](../Problems/0152.%20Maximum%20Product%20Subarray))*
- _No details provided._

**Palindromic Substrings** *([Problem](https://leetcode.com/problems/palindromic-substrings/) | [Solution](../Problems/0647.%20Palindromic%20Substrings))*
- _No details provided._

**Word Break** *([Problem](https://leetcode.com/problems/word-break/) | [Solution](../Problems/0139.%20Word%20Break))*
- _No details provided._

## 2-D Dynamic Programming

**Longest Common Subsequence** *([Problem](https://leetcode.com/problems/longest-common-subsequence/) | [Solution](../Problems/1143.%20Longest%20Common%20Subsequence))*
- _No details provided._

**Unique Paths** *([Problem](https://leetcode.com/problems/unique-paths/) | [Solution](../Problems/0062.%20Unique%20Paths))*
- _No details provided._

## Greedy

**Jump Game** *([Problem](https://leetcode.com/problems/jump-game/) | [Solution](../Problems/0055.%20Jump%20Game))*
- _No details provided._

**Maximum Subarray** *([Problem](https://leetcode.com/problems/maximum-subarray/) | [Solution](../Problems/0053.%20Maximum%20Subarray))*
- _No details provided._

## Intervals

**Insert Interval** *([Problem](https://leetcode.com/problems/insert-interval/) | [Solution](../Problems/0057.%20Insert%20Interval))*
- _No details provided._

**Meeting Rooms II** *([Problem](https://leetcode.com/problems/meeting-rooms-ii/) | [Solution](../Problems/0253.%20Meeting%20Rooms%20II))*
- _No details provided._

**Meeting Rooms** *([Problem](https://leetcode.com/problems/meeting-rooms/) | [Solution](../Problems/0252.%20Meeting%20Rooms))*
- _No details provided._

**Merge Intervals** *([Problem](https://leetcode.com/problems/merge-intervals/) | [Solution](../Problems/0056.%20Merge%20Intervals))*
- _No details provided._

**Non Overlapping Intervals** *([Problem](https://leetcode.com/problems/non-overlapping-intervals/) | [Solution](../Problems/0435.%20Non%20Overlapping%20Intervals))*
- _No details provided._

## Math & Geometry

**Rotate Image** *([Problem](https://leetcode.com/problems/rotate-image/) | [Solution](../Problems/0048.%20Rotate%20Image))*
- _No details provided._

**Set Matrix Zeroes** *([Problem](https://leetcode.com/problems/set-matrix-zeroes/) | [Solution](../Problems/0073.%20Set%20Matrix%20Zeroes))*
- _No details provided._

**Spiral Matrix** *([Problem](https://leetcode.com/problems/spiral-matrix/) | [Solution](../Problems/0054.%20Spiral%20Matrix))*
- _No details provided._

## Bit Manipulation

**Counting Bits** *([Problem](https://leetcode.com/problems/counting-bits/) | [Solution](../Problems/0338.%20Counting%20Bits))*
- _No details provided._

**Missing Number** *([Problem](https://leetcode.com/problems/missing-number/) | [Solution](../Problems/0268.%20Missing%20Number))*
- _No details provided._

**Number of 1 Bits** *([Problem](https://leetcode.com/problems/number-of-1-bits/) | [Solution](../Problems/0191.%20Number%20of%201%20Bits))*
- _No details provided._

**Reverse Bits** *([Problem](https://leetcode.com/problems/reverse-bits/) | [Solution](../Problems/0190.%20Reverse%20Bits))*
- _No details provided._

**Sum of Two Integers** *([Problem](https://leetcode.com/problems/sum-of-two-integers/) | [Solution](../Problems/0371.%20Sum%20of%20Two%20Integers))*
- _No details provided._

## Heap

**Find Median From Data Stream** *([Problem](https://leetcode.com/problems/find-median-from-data-stream/) | [Solution](../Problems/0295.%20Find%20Median%20From%20Data%20Stream))*
- _No details provided._