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

1->4->3, which creates the number 143.
1->4->7->9, which creates the number 1479.
1->5, which creates the number 15.

The sum for this tree is 143 + 1479 + 15 = 1637.

## What You'll Do
Your job is to implement the function sumPaths, which given a root to a binary tree, will return the sum of all of the paths. Be sure to write additional tests.

You may assume all node values will be between 0 and 9.

Please implement your solution in C11, Java 8, or Python 2.7 using only the standard library of these languages. There is skeleton code with a simple test case for each of these languages in this repository.

## Getting started
To get started, **clone** (not fork) this repository. At the top of the README, state which language your solution will be in.

We're expecting the question to take 30 minutes to an hour. We don't want you to waste a bunch of time finding a perfect solution to this, so if you're finding that it's taking much longer than that, please feel welcome to submit a non-complete solution. If you do so, please do include pseudocode and comments explaining your thoughts and ideas, and expected test cases/edge cases.

## Submission
When you are finished with your solution, edit this README, and push it to a private Github repository. As a student, you are eligible for the [Github Student Developer Pack](https://education.github.com/pack), which includes unlimited private repositories.

Once you've pushed to your private repository, add [alexaliu](https://github.com/alexaliu) and [jasonewang](https://github.com/jasonewang) as collaborators. **Fill out [this Google Form](https://goo.gl/forms/pUmsvijPrkdpLKg32) when you're finished, attaching your resume and transcript.**

You may delete your solution repository once the interview process is over.

If you are ineligible for the student pack and don't have any available private repositories, then creating a public repository is OK.

## Deadline
The deadline for submission is **Wednesday, September 20th 11:59PM PDT**. If we decide to move forward with your application, we will schedule on campus interviews on Monday, September 25th or phone interviews over the next few weeks.

