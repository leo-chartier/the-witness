from elements import Center, EdgeType, IntersectionType, Move, Position
from solution import Solution


class Puzzle:
    intersections: list[list[IntersectionType]]
    horizontal_edges: list[list[EdgeType]]
    vertical_edges: list[list[EdgeType]]
    centers: list[list[Center]]
    symmetry: bool
    # TODO: Background & line colors

    def __init__(
        self,
        intersections: list[list[IntersectionType]],
        horizontal_edges: list[list[EdgeType]],
        vertical_edges: list[list[EdgeType]],
        centers: list[list[Center]],
        symmetry: bool = False
    ) -> None:
        self.intersections = intersections
        self.horizontal_edges = horizontal_edges
        self.vertical_edges = vertical_edges
        self.centers = centers
        self.symmetry = symmetry

        # TODO: Check for invalid puzzles
    
    def find_solution(self) -> Solution:
        starts = [
            Position(x, y)
            for y, row in enumerate(self.intersections)
            for x, intersection in enumerate(row)
            if intersection == IntersectionType.START
        ]
        candidates = [Solution(start, []) for start in starts]

        # TODO: Do better than bruteforce
        while candidates:
            candidate = candidates.pop(0)

            for move in Move:
                new_candidate = Solution(candidate.start, candidate.moves + [move])

                if not self.is_path_valid(new_candidate):
                    continue

                if self.is_solution(new_candidate):
                    return new_candidate
                
                candidates.append(new_candidate)

        raise RuntimeError("No solution found")
    
    def is_path_valid(self, path: Solution) -> bool:
        raise NotImplementedError()
    
    def is_solution(self, path: Solution) -> bool:
        raise NotImplementedError()
