from elements import Center, EdgeType, IntersectionType


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
