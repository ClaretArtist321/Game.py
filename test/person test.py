import unittest
from Person import Person

class PersonTests(unittest.TestCase):
    def test_Person(self):
        person = Person(1)
        self.assertEqual(person.score, 1)



if __name__ == '__main__':
    unittest.main()