from elements import Move, Position


class Path:
    start: Position
    moves: list[Move]

    def __init__(
        self,
        start: Position,
        moves: list[Move]
    ) -> None:
        self.start = start
        self.moves = moves
