"""

"""


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

"""

"""