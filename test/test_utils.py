import unittest

from ..main import utils


class GameResourcesTest(unittest.TestCase):

    def test_01_get_new_id(self):
        new_id = utils.GameResources.get_new_id()
        self.assertEqual(new_id, 1)

    def test_02_create_game(self):
        player_id = utils.PlayerResources.save_player(host='localhost', port='12345')
        game_id = utils.GameResources.create_game(player_id, '1x1')
        p = utils.PlayerResources.get_player(player_id)
        g = utils.GameResources.get_game(game_id)
        self.assertEqual(g.game_id, 1)
        self.assertIn(g, g.all_games)  # static
        self.assertIn(p, g.players)
        self.assertIn(g, p.my_games)


def suite():
    s = unittest.TestSuite()
    s.addTest(GameResourcesTest('test_01_get_new_id'))
    s.addTest(GameResourcesTest('test_02_create_game'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
