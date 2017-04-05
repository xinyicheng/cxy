#! /usr/bin/env python
import unittest
import cxytest
class Test001(unittest.TestCase):
  def test_cxy1(self):
    self.assertEquals(cxytest.Dowork(4,6,7),(23,2))
  def test_cxy2(self):
    self.assertEquals(cxytest.Dowork(1,2,13),(0,0))
