# Autocomplete with Tries

The Jupyter Notebook for this project is `problem_5.ipynd`. You can find an `.py` download of the notebook contents in `problem_5.py`, and a Markdown version of the notebook in `problem_5.md`.

The purpose of the project is, given a prefix, find all of the suffixes in the trie. For example, if a trie contained the words `("trie", "trigger", "trigonometry", "tripod")`, then given a prefix of `trig`, the returned suffixes should be:
```
"ger", "onometry"
```


## Data structure

The chosen data structure to represent the Trie was a dictionary. In Python, the dict
data structure is implemented using a hash table. In the average case, this has fast
look up and insert times of `O(1)`. If there are a lot of collisions, in the worst case
look up and insert can take `O(n)`, but collisions should be rare.

## Space complexity

In the worst case, the space complexity of the Trie will be:
- `O(n*M)`
 - `n` is the number of words in the list
 - `M` is the number of characters in the longest word in the list

The worst case happens when there is minimal overlap between the words. For example,
if each word started with a unique first character, each word would have its own path
in the tree. 

## Time complexity

Below is a description of the time complexities for the major functions implemented.

#### TrieNode insert(char)

This is a simple insertion into a dictionary. Usually this will run in `O(1)`, although 
it may run in `O(n)` if there are several collisions, where `n` is the number of 
entries in the dictionary. 

#### TrieNode suffixes(suffix)

This function recurses through the trie to return each suffix. In the worst case, such as
when every word in the Trie starts with the same letter, but the second letter in each word
is different, there will be about `n` recursions. In this case `n` is the number of nodes in
the Trie. Each node will also need to be looked up. On average, in a Python dictionary this
takes `O(1)` time. If the hash function is poor and there are a lot of collisions, this can
take `O(n)` time in the worst case.

Therefore this function is expected to run in `O(n)` time, but in the rare worst case, it
could take `O(n^2)`


#### Trie insert(word)

The function iterates through each character in the word once, which takes `O(n)` time,
where `n` is the length of the word. Since each character needs to be inserted in to 
the trie individually, this is the fastest we can achieve. 

The `if char not in current_node.children:` operation will need to look through all of the 
children in the node. Assuming that we are only storing lowercase letters, a node can have a 
maximum of 26 children, so at most this will be 26 operations, which is `O(1)`

As noted above, the insertion operation itself is expected to take `O(1)` time, however
in the worst case it may take `O(m)` time, where `m` is the number of entries in the dictionary.
Through each iteration through the loop, there is also a lookup call to navigate to the next node. 
As with insertion, this is expected to take `O(1)` time, but could take `O(m)` in the worst case.
So each iteration through the loop is expected to run in `O(1)`, but could take `O(2m)`, which
can be simplified to `O(m)`.

So we can reasonably expect this function to run in `O(n)` time, although in the case of 
a poor hashing function for inserting into the dictionary, it could be as much as `O(n*m)`.

#### Trie find(prefix)

This function will iterate through each character in the prefix that is passed in. This
will take `n` iterations through the loop, where `n` is the length of the prefix.

This function is nearly identical in complexity to the Trie classes `insert(word)` method.
The only difference is there is no insert call. We only have the look up to find the next
node, which is expected to take `O(1)` time but can be as much as `O(m)` in the worst case,
where `m` is the number of nodes in the trie.

So we can reasonably expect this function to run in `O(n)` time, although in the case of 
a poor hashing function for inserting into the dictionary, it could be as much as `O(n*m)`.
