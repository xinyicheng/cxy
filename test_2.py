$DEFAULT_CONTENT
# -*- coding: utf-8 -*-
import unittest
from lookup_phone import Phone_msg  

class TestPhone(unittest.TestCase):

      def setUp(self):
          self.phone_msg = Phone_msg()

      def tearDown(self):
          pass

      def test_area_code(self):
          phone_num = [str(n) for n in phone_list.keys()]
          for i in range (0,len(phone_num)):
              self.assertEquals(self.phone_msg.get_area_code(phone_num[i]),area_list   [phone_list[phone_num[i]][0]][0])

      def test_province(self):
          phone_num = [str(n) for n in phone_list.keys()]
          for i in range (0,len(phone_num)):
              self.assertEquals(self.phone_msg.get_province(phone_num[i]),area_list[phone_list[phone_num[i]][0]][1])

      def test_city(self):
          phone_num = [str(n) for n in phone_list.keys()] 
          for i in range (0,len(phone_num)): 
              self.assertEquals(self.phone_msg.get_city(phone_num[i]),area_list [phone_list[phone_num[i]][0]][2])

      def test_zip_code(self):
          phone_num = [str(n) for n in phone_list.keys()]  
          for i in range (0,len(phone_num)):  
              self.assertEquals(self.phone_msg.get_zip_code(phone_num[i]),area_list[phone_list[phone_num[i]][0]][3])

      def test_phone_type(self):
          phone_num = [str(n) for n in phone_list.keys()] 
          for i in range (0,len(phone_num)):
              self.assertEquals(self.phone_msg.get_phone_type(phone_num[i]),phone_list[phone_num[i]][1])

if __name__ == "__main__":
    f = open("area_list.txt","r")
    area_list = {}
    for line in f:
        a = line.strip().split(":")
        b = a[1].strip().split("|")
        area_list[a[0]] = tuple(b)
    f.close()

    f = open("phone_list.txt","r")
    phone_list = {}
    for line in f:
        a = line.strip().split(":")
        b = a[1].strip().split("|")
        phone_list[a[0]] = tuple(b)
    f.close()
    unittest.main()
    
