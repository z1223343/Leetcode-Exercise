"""
2 level solution:
1. BFS: Breadth First Search
2. Bidirectional BFS

    time           space
1.  O(M**2*N)    O(M**2*N)
2.  O(M**2*N)    O(M**2*N)
"""

# solution 1
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if (endWord not in wordList):
            return 0

        L = len(beginWord)

        # define all_words_intermedium_dict
        all_comb_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_comb_dict[word[:i] + '*' + word[i + 1:]].append(word)

        # define the queue
        queue = [(beginWord, 1)]
        visited = [beginWord]

        while queue:
            curr_word, level = queue.pop(0)
            for i in range(L):
                for word in all_comb_dict[curr_word[:i] + '*' + curr_word[i + 1:]]:
                    if word == endWord:
                        return level + 1
                    elif word not in visited:
                        queue.append((word, level + 1))
                        visited.append(word)
                all_comb_dict[curr_word[:i] + '*' + curr_word[i + 1:]] = []
        return 0

# 改良版： （我透！我把visted从list改为dict,运行时间之间从 ~2000s -> ~100s. 我尼玛）
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if (endWord not in wordList):
            return 0

        L = len(beginWord)

        # define all_words_intermedium_dict
        all_comb_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_comb_dict[word[:i] + '*' + word[i + 1:]].append(word)

        # define the queue
        queue = [(beginWord, 1)]
        visited = {beginWord: True} # 关键是这里

        while queue:
            curr_word, level = queue.pop(0)
            for i in range(L):
                intermediate_word = curr_word[:i] + '*' + curr_word[i + 1:]  # 这个改不改，实测，无所谓
                for word in all_comb_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    elif word not in visited:
                        queue.append((word, level + 1))
                        visited[word] = True
                all_comb_dict[intermediate_word] = []
        return 0
"""

"""