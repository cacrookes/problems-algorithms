# HTTPRouter using a Trie




## Data structure

The chosen data structure to represent the Trie was a dictionary. In Python, the dict
data structure is implemented using a hash table. In the average case, this has fast
look up and insert times of `O(1)`. If there are a lot of collisions, in the worst case
look up and insert can take `O(n)`, but collisions should be rare.

## Space complexity

In the worst case, the space complexity of the Trie will be:
- `O(n*M)`
 - `n` is the number of paths
 - `M` is the number of parts in the longest path in the list

The worst case happens when there is minimal overlap between the paths. 

## Time complexity

Below is a description of the time complexities for the major functions implemented.

#### RouteTrieNode insert(path_part, handler)

This is a simple insertion into a dictionary. Usually this will run in `O(1)`, although 
it may run in `O(n)` if there are several collisions, where `n` is the number of 
entries in the dictionary. 

#### RouteTrie insert(path, handler)

Note that `path` is a list of parts that make up the path.

Let `n` be the number of items in the list `path`
Let `m` be the number of nodes in the trie.

The function iterates through each part in the path once, which takes `O(n)` time,
where `n` is the length of the list `path`. Since each part needs to be inserted
into the trie individually, this is the fastest that can be achieved. 

In each iteration of the loop, there are potentially three operations that can happen:
- `if part not in current_node.children:`
 - in the worst case, where all other nodes are children of the root node, this can
   take (m-1) operations, so this is `O(m)`
- insert into dictionary
 - As noted above, the insertion operation itself is expected to take `O(1)` time, however in the worst case it may take `O(m)` time, where `m` is the number of entries in the dictionary.
 - dictionary lookup
  - As with insertion, this is expected to take `O(1)` time, but could take `O(m)` in the worst case.

So at worst, each iteration will take about `3 * m` steps, which is `O(m)`.

So the worst case for this algorithm is `O(n*m)`

#### RouteTrie find(path)

Note that `path` is a list of parts that make up the path.

Let `n` be the number of items in the list `path`
Let `m` be the number of nodes in the trie.

This function is nearly identical in its complexity to the RouteTrie's 
`insert(path, handler)` operation. The may difference is that there is no
insertion. So at worst, each iteration of the loop will take `2 * m`, which is
still `O(m)`.

So the worst case for this algorithm is `O(n*m)`.

#### Router add_handler(path, handler)
This function calls `split_path(path)` and RouteTrie's `insert(path, handler)`

Let n = number of characters in path.
Let p = number of parts in path.
Let m = number of nodes in the trie.

`split_path(path)` runs in `O(n)` (see below).
RouteTrie's `insert(path, handler)` runs in `O(p * m)` (see above)

So add_handler can be thought having `O(n) + O(p * m)` runtime.

Since p <= n, `O(p)` must be bounded to the top by `O(n)`. So 
`O(n) + O(p * m)` simplifies to `O(n) + O(n * m)`, which is just:
```
O(n*m)
```

#### Router lookup(path)

`lookup(path)` is similar to Router's `add_handler(path, handler)` method. The
main difference being it calls RouteTrie's `find(path)` function instead of its
`insert(path, handler)` function.

As detailed above, both `find(path)` and `insert(path, handler)` have the same
time complexity, so Router `lookup(path)` has the same time complexity as Router's
`add_handler(path, handler)` method.

So the runtime complexity is `O(n*m)` where:
n = number of characters in path.
m = number of nodes in the trie.


#### Router split_path(path)
#TODO update this
Let `n` be the number of characters in `path`

This function iterates through each character in `path` one time. This will take
`O(n)` time.

