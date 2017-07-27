#! /usr/bin/env python
import unittest
from cxytest import*
class Test001(unittest.TestCase):
  def test_cxy1(self):
    self.assertEquals(Dowork(2,6,7),(23,1))
  def test_cxy2(self):
    self.assertEquals(Dowork(1,2,13),(0,0))
if __name__ =="__main__":
   unittest.main()
