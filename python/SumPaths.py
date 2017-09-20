#!/usr/bin/env python

import unittest

class TestSumPaths(unittest.TestCase):

  def testSanity(self):
    n1 = Node(value=1)
    self.assertEqual(n1.sumPaths(), 1)

  # Write some more test cases
  def test2(self):
    n6 = Node(value=9)
    n5 = Node(value=7, right=n6)
    n4 = Node(value=3)
    n3 = Node(value=5)
    n2 = Node(value=4, left=n4, right=n5)
    n1 = Node(value=1, left=n2, right=n3)
    self.assertEqual(n1.sumPaths(), 1637)

class Node:
  def __init__(self, value=0, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value
    self.result = 0

  def sumPaths(self):
    # IMPLEMENT ME
    def helper(node, result):
      if node == None:
        return 0

      result = 10*result + node.value

      if node.left == None and node.right == None:
        return result
      total = helper(node.left, result) + helper(node.right, result)
      return total

    self.result = helper(self, self.result)
    
    return self.result

if __name__ == "__main__":
  unittest.main()
