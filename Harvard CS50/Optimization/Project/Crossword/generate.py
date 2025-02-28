import sys

from crossword import Variable, Crossword


class CrosswordCreator:
    def __init__(self, crossword):
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy() for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        from PIL import Image, ImageDraw, ImageFont

        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size, self.crossword.height * cell_size),
            "black",
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                rect = [
                    (j * cell_size + cell_border, i * cell_size + cell_border),
                    (
                        (j + 1) * cell_size - cell_border,
                        (i + 1) * cell_size - cell_border,
                    ),
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (
                                rect[0][0] + ((interior_size - w) / 2),
                                rect[0][1] + ((interior_size - h) / 2) - 10,
                            ),
                            letters[i][j],
                            fill="black",
                            font=font,
                        )

        img.save(filename)

    def solve(self):
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        for var in self.crossword.variables:
            words_to_remove = set()
            for word in self.domains[var]:
                if len(word) != var.length:
                    words_to_remove.add(word)
            self.domains[var] -= words_to_remove

    def revise(self, x, y):
        revised = False
        overlap = self.crossword.overlaps[x, y]
        if overlap is None:
            return False
        i, j = overlap
        words_to_remove = set()
        for x_word in self.domains[x]:
            match_found = False
            for y_word in self.domains[y]:
                if x_word[i] == y_word[j]:
                    match_found = True
                    break
            if not match_found:
                words_to_remove.add(x_word)
                revised = True
        if revised:
            self.domains[x] -= words_to_remove
        return revised

    def ac3(self, arcs=None):
        if arcs is None:
            queue = set()
            for x in self.crossword.variables:
                for y in self.crossword.neighbors(x):
                    if x != y:
                        queue.add((x, y))
        else:
            queue = set(arcs)
        while queue:
            x, y = queue.pop()
            if self.revise(x, y):
                if not self.domains[x]:
                    return False
                for z in self.crossword.neighbors(x):
                    if z != y and z != x:
                        queue.add((z, x))
        return True

    def assignment_complete(self, assignment):
        return len(assignment) == len(self.crossword.variables)

    def consistent(self, assignment):
        values = list(assignment.values())
        if len(values) != len(set(values)):
            return False
        for x, y in self.crossword.overlaps:
            if x in assignment and y in assignment:
                overlap = self.crossword.overlaps[x, y]
                if overlap is not None:
                    i, j = overlap
                    if assignment[x][i] != assignment[y][j]:
                        return False
        return True

    def order_domain_values(self, var, assignment):
        unassigned_neighbors = [
            n for n in self.crossword.neighbors(var) if n not in assignment
        ]
        constraint_counts = {}
        for value in self.domains[var]:
            total_eliminated = 0
            for neighbor in unassigned_neighbors:
                overlap = self.crossword.overlaps[var, neighbor]
                if overlap is not None:
                    i, j = overlap
                    for neighbor_value in self.domains[neighbor]:
                        if value[i] != neighbor_value[j]:
                            total_eliminated += 1
            constraint_counts[value] = total_eliminated
        return sorted(self.domains[var], key=lambda value: constraint_counts[value])

    def select_unassigned_variable(self, assignment):
        unassigned = [var for var in self.crossword.variables if var not in assignment]
        if not unassigned:
            return None
        return min(
            unassigned,
            key=lambda var: (
                len(self.domains[var]),
                -len(self.crossword.neighbors(var)),
            ),
        )

    def backtrack(self, assignment):
        if self.assignment_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        if var is None:
            return None
        for value in self.order_domain_values(var, assignment):
            new_assignment = assignment.copy()
            new_assignment[var] = value
            if self.consistent(new_assignment):
                result = self.backtrack(new_assignment)
                if result is not None:
                    return result
        return None


def main():
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
