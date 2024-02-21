import unittest


class OutcomesTest(unittest.TestCase):

    def testPass(self):
        return

    def testFail(self):
        self.assertFalse(True, 'intentionally made to fail')

    def testError(self):
        raise RuntimeError('Test error!')
