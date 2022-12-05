import unittest
import questions
import sys


testers = ['']

class TestSumOfElements(unittest.TestCase):
    """
    1 Katas
    """

    def test_empty_list(self):
        lst = []
        self.assertEqual(questions.sum_of_element(lst), 0)


    def test_integers_list(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(questions.sum_of_element(lst), 15)

    def test_negative_numbers(self):
        lst = [1, -6, 7, 0, 99]
        self.assertEqual(questions.sum_of_element(lst), 101)

    def test_all_zeros(self):
        lst = [0] * 50000
        self.assertEqual(questions.sum_of_element(lst), 0)

class TestVerbing(unittest.TestCase):
    """
    1 Katas
    """

    def testSmallChar(self):
        shortStringTest = "ha"
        self.assertEqual(questions.verbing(shortStringTest), "ha")

    def testAddIng(self):
        addIngTest = "spray"
        self.assertEqual(questions.verbing(addIngTest), "spraying")
    
    def testAddLy(self):
        addLyTest = "amazing"
        self.assertEqual(questions.verbing(addLyTest), "amazingly")
    
    def testEmptyString(self):
        testEmptyString = ""
        self.assertEqual(questions.verbing(testEmptyString), "")


class TestWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """

    def testSimpleSentence(self):
        testThreeWords = ["take", "me", "home"]
        self.assertEqual(questions.words_concatenation(testThreeWords), "take me home")

    

if __name__ == "__main__":
  suite = unittest.TestLoader().loadTestsFromModule( sys.modules[__name__] )
  unittest.TextTestRunner(verbosity=3).run( suite )