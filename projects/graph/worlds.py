""" 
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.

Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
beginWord = "hungry"
endWord = "happy"
None
"""

from util import Stack, Queue
#2. Build the graph
# load words friom dictionary
f = open('words.txt','r')
wordslist = f.read().lower().split("\n")
f.close()
def get_neighbor(word):
    """
    get all words thata are one letter away from the given word
    """
    result=[w for w in wordslist if sum(a!=b for a,b in zip(word,w)) == 1 and (len(word)==len(w))]
    return result


#3 Traverse the grapgh (BFS)
def word_ladder(begin_word, end_word):
    # Create a queue
    q = Queue()
    # Enqueue a path to starting word
    q.enqueue( [begin_word] )
    # Create a visited set
    visited = set()
    # While queue is not empty:
    while q.size() > 0:
        # Dequeue path
        path = q.dequeue()
        # Grab the last word from the path
        w = path[-1]
        # Check if it's our target word
        if w == end_word:
            # If so, return path
            return path
        # Check if it's been visited
        # If not, mark as visited
        if w not in visited:
            visited.add(w)
            # Enqueue path to each neighboring word
            for neighbor in get_neighbor(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)

print(word_ladder('sail','boat'))
