import doctest
import unittest

import doctest_testmod

suite = unittest.TestSuite()
suite.addTest(doctest.DocTestSuite(doctest_testmod))
suite.addTest(doctest.DocFileSuite('doctest_in_help.txt'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
