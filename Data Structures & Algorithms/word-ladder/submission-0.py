class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbor = {}
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                if pattern in neighbor:
                    neighbor[pattern].append(word)
                else:
                    neighbor[pattern] = [word]
        print(neighbor)
        pass
        res = 1
        q = deque([beginWord])
        visit = set([beginWord])
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in neighbor[pattern]:                   
                        if neiWord not in visit:
                            q.append(neiWord)
                            visit.add(neiWord)
            res+=1
        return 0

