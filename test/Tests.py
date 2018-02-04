import os
import unittest

suite = unittest.TestLoader().discover(os.getcwd(), pattern='*Test.py')
runner = unittest.TextTestRunner().run(suite)
