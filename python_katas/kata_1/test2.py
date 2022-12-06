import unittest
import questions
import sys


testers = ["Dean", "bibi", "Arik", "Gad", "Rosin"]

class TestSumOfElements(unittest.TestCase):
    """
    1 Katas
    """

    def test_empty_list(self):
        lst = []
        self.assertEqual(questions.sum_of_element(lst), 0)

        lst = [1, 2, 3, 4, 5]
        self.assertEqual(questions.sum_of_element(lst), 15)

        lst = [1, -6, 7, 0, 99]
        self.assertEqual(questions.sum_of_element(lst), 101)

        lst = [0] * 50000
        self.assertEqual(questions.sum_of_element(lst), 0)

class TestVerbing(unittest.TestCase):
    """
    1 Katas
    """

    def testChars(self):
        shortStringTest = "ha"
        self.assertEqual(questions.verbing(shortStringTest), "ha")

        addIngTest = "spray"
        self.assertEqual(questions.verbing(addIngTest), "spraying")

        addLyTest = "amazing"
        self.assertEqual(questions.verbing(addLyTest), "amazingly")

        testEmptyString = ""
        self.assertEqual(questions.verbing(testEmptyString), "")


class TestWordsConcat(unittest.TestCase):
    """
    1 Katas
    """

    def testSimpleSentence(self):
        testWords = ["take", "on", "me"]
        self.assertEqual(questions.words_concatenation(testWords), "take on me")

        testWords = ["hi", "mom"]
        self.assertEqual(questions.words_concatenation(testWords), "hi mom")

        testWords = []
        self.assertEqual(questions.words_concatenation(testWords), "")

        testWords = 1
        self.assertRaises(TypeError, questions.words_concatenation ,testWords )

    
class TestReverseWordConcat(unittest.TestCase):
    """
    1 Katas
    """

    def testReverseWordsConcatination(self):
        testReverseWord = ["hello", "my", "friend"]
        self.assertEqual(questions.reverse_words_concatenation(testReverseWord), "friend my hello")

        testReverseWord = []
        self.assertEqual(questions.reverse_words_concatenation(testReverseWord), "")

class TestUniqeString(unittest.TestCase):
    """
    2 Katas
    """

    def testIsUniqueString(self):
        testUnique = "abcdef"
        self.assertEqual(questions.is_unique_string(testUnique), True)

class TestDiffList(unittest.TestCase):
    """
    1 Katas
    """
    def testDiffList(self):
        listToDiff = [1, 3, 6, 10, 14, 25]
        self.assertEquals(questions.list_diff(listToDiff), [2, 3, 4, 4, 11])

        listToDiff = [4, 1, 7, 2, 11, 0]
        self.assertEqual(questions.list_diff(listToDiff), [-3, 6, -5, 9, -11])


if __name__ == "__main__":
  suite = unittest.TestLoader().loadTestsFromModule( sys.modules[__name__] )
  unittest.TextTestRunner(verbosity=3).run( suite )