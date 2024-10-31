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
    
    def get_edge(self, position: Position, direction: Move):
        new_position = position + direction.value
        match direction:
            case Move.UP:
                return self.vertical_edges[new_position.y][new_position.x]
            case Move.DOWN:
                return self.vertical_edges[position.y][position.x]
            case Move.LEFT:
                return self.horizontal_edges[new_position.y][new_position.x]
            case Move.RIGHT:
                return self.horizontal_edges[position.y][position.x]
    
    def is_path_valid(self, path: Path) -> bool:
        position = path.start
        visited = [position]

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
            
            # Check for overlap
            if new_position in visited:
                return False
            visited.append(position)

            # Check if edge is valid
            edge = self.get_edge(position, move)
            if edge in (EdgeType.MISSING, EdgeType.BROKEN):
                return False
            
            position = new_position
        
        return True
    
    def is_solution(self, path: Path) -> bool:
        # Check path
        if not self.is_path_valid(path):
            return False

        # Check end position
        position = path.start
        for move in path.moves:
            position += move.value
        if self.intersections[position.y][position.x] != IntersectionType.END:
            return False
        
        # Count total dots
        count = 0
        for row in self.intersections:
            for intersection in row:
                if intersection == IntersectionType.DOT:
                    count += 1
        for row in self.horizontal_edges + self.vertical_edges:
            for edge in row:
                if edge == EdgeType.DOT:
                    count += 1

        # Count "eaten" dots
        position = path.start
        for move in path.moves:
            edge = self.get_edge(position, move)
            if edge == EdgeType.DOT:
                count -= 1
            position += move.value
            if self.intersections[position.y][position.x] == IntersectionType.DOT:
                count -= 1
        if count > 0:
            return False

        # TODO: Check for colors
        return True
