# -*- coding: UTF-8 -*-
class TestVideoCollection:
    @classmethod
    def setup_class(cls):
        print("setup_class")

    @classmethod
    def teardown_class(cls):
        print("teardown_class")

    def setup_method(self,method):
        print("setup_method")

    def teardown_method(self,method):
        print("teardown_method")
    
    def test_douban(self):
        print("test_douban")

    def test_live(self):
        print("test_live")

    def test_cloudmusic(self):
        print("test_cloudmusic")
