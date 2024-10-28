from puzzle import Puzzle
from elements import Move, Position


class Solution:
    puzzle: Puzzle
    start: Position
    moves: list[Move]

    def __init__(
        self,
        puzzle: Puzzle,
        start: Position,
        moves: list[Move]
    ) -> None:
        self.puzzle = puzzle
        self.start = start
        self.moves = moves
