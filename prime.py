'''
    Unit testing done using unittest library
'''

import unittest as test
from is_prime_resolved import is_prime as check

class TestForPrime(test.TestCase):
    '''
        TestForPrime class will be used to test
    '''
    def test_primes(self):
        '''
            In this function we test for no. that are already Identified as primes, to check for False Negatives
        '''
        for i in [63097, 6761, 85781, 55697, 26881, 94343, 73709, 7507, 42299, 64037]:
            self.assertTrue(check(i))
    def test_non_prime(self):
        '''
            In this function we test for no. that are already Identified as non-primes (All the even numbers), to check for False Positives
        '''
        for i in [40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 1006, 1008, 1010, 1012, 1014, 1016, 1018, 1020, 1022, 1024]:
            self.assertFalse(check(i))


if __name__ == "__main__":
    test.main()
