import unittest

from elements import *
from puzzle import Puzzle
from path import Path



class TestSolver(unittest.TestCase):

    # TODO: Check for puzzle validity

    def test_simple_line(self):
        puzzle = Puzzle(
            intersections=[
                [IntersectionType.START, IntersectionType.END]
            ],
            horizontal_edges=[
                [EdgeType.NORMAL]
            ],
            vertical_edges=[],
            centers=[]
        )
        expected = Path(Position(0, 0), [Move.RIGHT])
        result = puzzle.find_solution()
        self.assertEqual(expected.start, result.start)
        self.assertListEqual(expected.moves, result.moves)

    def test_simple_3x3_grid(self):
        puzzle = Puzzle(
            intersections=[
                [IntersectionType.START,  IntersectionType.NORMAL, IntersectionType.NORMAL],
                [IntersectionType.NORMAL, IntersectionType.NORMAL, IntersectionType.NORMAL],
                [IntersectionType.NORMAL, IntersectionType.NORMAL, IntersectionType.END],
            ],
            horizontal_edges=[
                [EdgeType.NORMAL, EdgeType.NORMAL],
                [EdgeType.NORMAL, EdgeType.NORMAL],
                [EdgeType.NORMAL, EdgeType.NORMAL],
            ],
            vertical_edges=[
                [EdgeType.NORMAL, EdgeType.NORMAL, EdgeType.NORMAL],
                [EdgeType.NORMAL, EdgeType.NORMAL, EdgeType.NORMAL],
            ],
            centers=[
                [Center(), Center()],
                [Center(), Center()],
            ]
        )
        expected = Path(Position(0, 0), [Move.RIGHT, Move.RIGHT, Move.DOWN, Move.DOWN])
        result = puzzle.find_solution()
        self.assertEqual(expected.start, result.start)
        self.assertCountEqual(expected.moves, result.moves)

    def test_broken_edges(self):
        puzzle = Puzzle(
            intersections=[
                [IntersectionType.START,  IntersectionType.NORMAL, IntersectionType.NORMAL],
                [IntersectionType.NORMAL, IntersectionType.NORMAL, IntersectionType.NORMAL],
                [IntersectionType.NORMAL, IntersectionType.NORMAL, IntersectionType.END],
            ],
            horizontal_edges=[
                [EdgeType.BROKEN, EdgeType.NORMAL],
                [EdgeType.BROKEN, EdgeType.BROKEN],
                [EdgeType.NORMAL, EdgeType.BROKEN],
            ],
            vertical_edges=[
                [EdgeType.NORMAL, EdgeType.NORMAL, EdgeType.NORMAL],
                [EdgeType.NORMAL, EdgeType.NORMAL, EdgeType.NORMAL],
            ],
            centers=[
                [Center(), Center()],
                [Center(), Center()],
            ]
        )
        expected = Path(Position(0, 0), [Move.DOWN, Move.DOWN, Move.RIGHT, Move.UP, Move.UP, Move.RIGHT, Move.DOWN, Move.DOWN])
        result = puzzle.find_solution()
        self.assertEqual(expected.start, result.start)
        self.assertListEqual(expected.moves, result.moves)

    def test_dots_on_intersections(self):
        puzzle = Puzzle(
            intersections=[
                [IntersectionType.START,  IntersectionType.DOT],
                [IntersectionType.NORMAL, IntersectionType.NORMAL],
                [IntersectionType.DOT,    IntersectionType.END],
            ],
            horizontal_edges=[
                [EdgeType.NORMAL],
                [EdgeType.NORMAL],
                [EdgeType.NORMAL],
            ],
            vertical_edges=[
                [EdgeType.NORMAL, EdgeType.NORMAL],
                [EdgeType.NORMAL, EdgeType.NORMAL],
            ],
            centers=[
                [Center()],
                [Center()],
            ]
        )
        expected = Path(Position(0, 0), [Move.RIGHT, Move.DOWN, Move.LEFT, Move.DOWN, Move.RIGHT])
        result = puzzle.find_solution()
        self.assertEqual(expected.start, result.start)
        self.assertListEqual(expected.moves, result.moves)

    def test_simple_colors(self):
        puzzle = Puzzle(
            intersections=[
                [IntersectionType.NORMAL, IntersectionType.NORMAL, IntersectionType.END],
                [IntersectionType.NORMAL, IntersectionType.NORMAL, IntersectionType.NORMAL],
                [IntersectionType.START,  IntersectionType.NORMAL, IntersectionType.NORMAL],
            ],
            horizontal_edges=[
                [EdgeType.NORMAL, EdgeType.NORMAL],
                [EdgeType.NORMAL, EdgeType.NORMAL],
                [EdgeType.NORMAL, EdgeType.NORMAL],
            ],
            vertical_edges=[
                [EdgeType.NORMAL, EdgeType.NORMAL, EdgeType.NORMAL],
                [EdgeType.NORMAL, EdgeType.NORMAL, EdgeType.NORMAL],
            ],
            centers=[
                [CenterColor(Color.BLACK), CenterColor(Color.BLACK)],
                [CenterColor(Color.BLACK), CenterColor(Color.WHITE)],
            ]
        )
        expected = Path(Position(0, 2), [Move.RIGHT, Move.UP, Move.RIGHT, Move.UP])
        result = puzzle.find_solution()
        self.assertEqual(expected.start, result.start)
        self.assertListEqual(expected.moves, result.moves)



if __name__ == "__main__":
    unittest.main()
