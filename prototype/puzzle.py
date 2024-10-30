from elements import Center, EdgeType, IntersectionType, Move, Position
from path import Path


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
    
    def find_solution(self) -> Path:
        starts = [
            Position(x, y)
            for y, row in enumerate(self.intersections)
            for x, intersection in enumerate(row)
            if intersection == IntersectionType.START
        ]
        candidates = [Path(start, []) for start in starts]

        # TODO: Do better than bruteforce
        while candidates:
            candidate = candidates.pop(0)

            for move in Move:
                new_candidate = Path(candidate.start, candidate.moves + [move])

                if not self.is_path_valid(new_candidate):
                    continue

                if self.is_solution(new_candidate):
                    return new_candidate
                
                candidates.append(new_candidate)

        raise RuntimeError("No solution found")
    
    def is_intersection_valid(self, position: Position):
        if position.y not in range(len(self.intersections)):
            return False
        if position.x not in range(len(self.intersections[position.y])):
            return False
        return True
    
    def is_path_valid(self, path: Path) -> bool:
        position = path.start

        # Check if start is correct
        if not self.is_intersection_valid(position):
            return False
        if self.intersections[position.y][position.x] != IntersectionType.START:
            return False
        
        for move in path.moves:
            # Check for bounds
            new_position = position + move.value
            if not self.is_intersection_valid(new_position):
                return False

            # Check if edge is valid
            match move:
                case Move.UP:
                    edge = self.vertical_edges[new_position.y][new_position.x]
                case Move.DOWN:
                    edge = self.vertical_edges[position.y][position.x]
                case Move.LEFT:
                    edge = self.horizontal_edges[new_position.y][new_position.x]
                case Move.RIGHT:
                    edge = self.horizontal_edges[position.y][position.x]
            if edge in (EdgeType.MISSING, EdgeType.BROKEN):
                return False
            
            position = new_position
        
        return True
    
    def is_solution(self, path: Path) -> bool:
        if not self.is_path_valid(path):
            return False

        position = path.start
        for move in path.moves:
            position += move.value
        
        if self.intersections[position.y][position.x] != IntersectionType.END:
            return False
        
        # TODO: Check for features
        return True
