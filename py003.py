#! /usr/bin/env python
import unittest
from cxytest1 import*
class Test001(unittest.TestCase):
  def test_cxy1(self):
    self.assertEquals(Dowork(4,6,7),(23,2))
  def test_cxy2(self):
    self.assertEquals(Dowork(1,2,13),(0,0))
