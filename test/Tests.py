import os
import unittest

suite = unittest.TestLoader().discover(os.path.dirname(os.path.abspath(__file__)), pattern='*Test.py')
runner = unittest.TextTestRunner().run(suite)
