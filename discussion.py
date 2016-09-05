"""
Part I:
Recursion
1. A function that calls itself until a certain condition is met
2. So we don't blow the stack

Graph
1. An abstract data type consisting of nodes and edges and can be directed or undirected
2. Graphs can contain loops and be non-directed while trees can't
3. facebook friends

Performance of different data structures

Data Structure | Index | Search | Add-R | Add-L | Pop-L | Pop-R
List              O(1)     O(n)    O(1)   O(n)     O(n)    O(1)
Linked List       O(n)     O(n)    O(1)   O(1)     O(1)    O(1)
Doubly LL         O(n)     O(n)    O(1)   O(1)     O(1)    O(1)
Queue (as array)   X        X      O(1)     X      O(n)      X
Queue(as LL, DLL)  X        X      O(1)     X      O(1)      X
Stack              X        X      O(1)     X       X      O(1)
Deque (as DLL)     X        X      O(1)   O(1)     O(1)    O(1)


Data Structure     | Get | Add | Delete | Iterate | Memory
Set                  O(1)  O(1)   O(1)     O(n)     medium
Binary Search Tree  log(n) O(?)   O(?)     O(?)       ?
tree                 O(n)  O(1)   O(1)     O(n)       ?

Sorting
1. Repeatedly iterate over the list looking at pairs of elements and swap the pairs if needed so that the larger one is to the right of the smaller one. The larger numbers bubble to the right.
2. Splits a list into halves until you have a list of one element then the smaller sorted lists are combined into larger sorted lists
3. There is a pivot and all the numbers smaller than the pivot are moved to the left of the pivot and all the numbers larger are moved to the right of the pivot.

Git Branching
1. Rewriting code to incorporate a framework you recently learned about
2. A request to merge work done on your branch with another branch



"""
