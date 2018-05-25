import unittest

from ..main import utils


class GameResourcesTest(unittest.TestCase):

    def test_get_new_id(self):
        new_id = utils.GameResources.get_new_id()
        self.assertEqual(new_id, 1)


if __name__ == '__main__':
    unittest.main()
