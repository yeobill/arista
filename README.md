# Arista Coding Question Fall 2017

## The Question
Given a binary tree, sum all of the numbers created by the paths from the root to each leaf.

For example, the tree below has the following paths:

                            1
                          /   \
                         /     \
                        4       5
                       / \  
                      3   7  
                           \
                            9

1->4->3, which creates the number 143
1->4->7->9, which creates the number 1479.
1->5, which creates the number 15.

The sum for this tree is 143 + 1479 + 15 = 1637

## What You'll Do
Your job is to implement the function sumPaths, which given a root to a binary tree, will return the sum of all of the paths. Be sure to write tests.

You may assume all node values will be between 0 and 9.
Return -1 if sumPaths is called on a null tree.

Please implement your solution in C11, Java 8, or Python 2.7 using only the standard library of these languages. There is skeleton code with a simple test case for each of these languages in this repository.

## Getting started
To get started, clone (not fork) this repository. At the top of the README, state which language your solution will be in.

## Submission
When you are finished with your solution, edit this README push it to a private Github repository and add [alexliu](https://github.com/alexaliu), Arista team member, as a collaborator.

You may delete your solution repository once the interview process is over.

If you are unable to create a Github account or are unable to create any more private repositories you may also email your solutions along with your resume and transcript, though we strongly prefer the above repository based workflow.
