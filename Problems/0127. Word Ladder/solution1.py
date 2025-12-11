class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adjList = collections.defaultdict(list)

        for word in wordList:
            for char in range(len(word)):
                pattern = word[:char] + "*" + word[char + 1:]
                adjList[pattern].append(word)

        queue = collections.deque([beginWord])
        visited = set()
        result = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                
                if word == endWord:
                    return result

                for char in range(len(word)):
                    pattern = word[:char] + "*" + word[char + 1:]
                    for neighbor in adjList[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            result += 1

        return 0
