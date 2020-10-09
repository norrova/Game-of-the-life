import unittest
import app

class AppTest(unittest.TestCase):
    
    def setUp(self):
        self.game_setting = {
            "size_map" : 40,
            "rules" : {
                "alive": [2, 3],
                "birth": [3]
            },
            "generation" : 1
        }
        self.cells = [[1,4],[1,5],[1,6]]

    def test_get_next_generation(self):
        result = [[0,5],[1,5],[2,5]]
        entry = app.get_next_generation(self.cells[0], self.cells, [], self.game_setting)
        self.assertEqual(entry, result)

    def test_around_cells(self):
        result = [
            [0,4], [0,5], [0,6], 
            [1,4], [1,5], [1,6],
            [2,4], [2,5], [2,6]
        ]
        self.assertEqual(app.get_around_cells(self.cells[1], self.game_setting["size_map"]), result)
        result = [
            [0,4], [0,5], [0,6], 
            [1,4], [1,5], [1,6]
        ]
        cell = [0,5]
        self.assertEqual(app.get_around_cells(cell, self.game_setting["size_map"]), result)
        result = [
            [0,0], [0,1], 
            [1,0], [1,1],
        ]
        cell = [0,0]
        self.assertEqual(app.get_around_cells(cell, self.game_setting["size_map"]), result)

    def test_get_neighbor(self):
        self.assertEqual(app.get_neighbor(self.cells[0], self.cells, self.game_setting["size_map"]), 1)
        self.assertEqual(app.get_neighbor(self.cells[1], self.cells, self.game_setting["size_map"]), 2)
        self.assertEqual(app.get_neighbor(self.cells[2], self.cells, self.game_setting["size_map"]), 1)

    def test_can_alive(self):
        # Alive
        neighbors = [2,3]
        for neighbor in neighbors:
            self.assertTrue(app.can_alive(neighbor, self.game_setting["rules"], True))

        neighbors = [1,4,5,6,7,8]
        for neighbor in neighbors:
            self.assertFalse(app.can_alive(neighbor, self.game_setting["rules"], True))

        # Death
        self.assertTrue(app.can_alive(3, self.game_setting["rules"], False))

        neighbors = [1,2,4,5,6,7,8]
        for neighbor in neighbors:
            self.assertFalse(app.can_alive(neighbor, self.game_setting["rules"], False))