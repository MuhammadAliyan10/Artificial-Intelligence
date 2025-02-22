import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier:
    def __init__(self):
        self.frontier = []
    def add(self, node):
        self.frontier.append(node)
    def containsState(self, state):
        return any(node.state == state for node in self.frontier)
    def empty(self):
        return len(self.frontier) == 0
    def remove(self):
        if self.empty():
            raise Exception("No nodes in frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("No nodes in frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Maze:
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()
        if contents.count("A") != 1:
            raise Exception("Maze must have exactly one 'A'")
        if contents.count("B") != 1:
            raise Exception("Maze must have exactly one 'B'")
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("#", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbor(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1)),
        ]
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self):
        self.numExplored = 0
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()  # DFS; use QueueFrontier() for BFS
        frontier.add(start)
        self.explored = set()
        while True:
            if frontier.empty():
                raise Exception("No solution")
            node = frontier.remove()
            self.numExplored += 1
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
            self.explored.add(node.state)

            for action, state in self.neighbor(node.state):
                if not frontier.containsState(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    def draw(self):
        CELL_SIZE = 40
        window = tk.Tk()
        window.title("Maze Solver")
        canvas = tk.Canvas(window, width=self.width * CELL_SIZE, height=self.height * CELL_SIZE)
        canvas.pack()

        for i in range(self.height):
            for j in range(self.width):
                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                if self.walls[i][j]:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                elif (i, j) == self.start:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                    canvas.create_text(x1 + CELL_SIZE // 2, y1 + CELL_SIZE // 2, text="A", fill="white")
                elif (i, j) == self.goal:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="red")
                    canvas.create_text(x1 + CELL_SIZE // 2, y1 + CELL_SIZE // 2, text="B", fill="white")
                else:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="white")

        if self.solution:
            for (i, j) in self.solution[1]:
                if (i, j) not in [self.start, self.goal]:
                    x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                    x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                    canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

        window.mainloop()

    def save_image(self, filename="maze_solution.png"):
        CELL_SIZE = 40
        image = Image.new("RGB", (self.width * CELL_SIZE, self.height * CELL_SIZE), "white")
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 20)  # Adjust font size as needed
        except:
            font = ImageFont.load_default()  # Fallback if Arial isn’t available

        for i in range(self.height):
            for j in range(self.width):
                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                if self.walls[i][j]:
                    draw.rectangle([x1, y1, x2, y2], fill="black")
                elif (i, j) == self.start:
                    draw.rectangle([x1, y1, x2, y2], fill="green")
                    draw.text((x1 + CELL_SIZE // 2 - 5, y1 + CELL_SIZE // 2 - 10), "A", fill="white", font=font)
                elif (i, j) == self.goal:
                    draw.rectangle([x1, y1, x2, y2], fill="red")
                    draw.text((x1 + CELL_SIZE // 2 - 5, y1 + CELL_SIZE // 2 - 10), "B", fill="white", font=font)
                else:
                    draw.rectangle([x1, y1, x2, y2], fill="white")

        if self.solution:
            for (i, j) in self.solution[1]:
                if (i, j) not in [self.start, self.goal]:
                    x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                    x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                    draw.rectangle([x1, y1, x2, y2], fill="blue")

        image.save(filename)
        print(f"Image saved as {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python maze.py maze.txt")
    
    try:
        maze = Maze(sys.argv[1])
        print("Maze:")
        maze.print()
        maze.solve()
        print("Solution:")
        maze.print()
        maze.save_image("maze_solution.png")  # Save as PNG
        maze.draw()  # Optional: still shows the GUI
    except FileNotFoundError:
        sys.exit("Error: Maze file not found")
    except Exception as e:
        sys.exit(f"Error: {str(e)}")