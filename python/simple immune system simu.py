import random
import time
import os
import io

class Cell:
    def __init__(self, cell_type, x, y):
        self.type = cell_type
        self.x = x
        self.y = y
        self.is_alive = True
        self.has_virus = False
        self.cloaked = True
        self.age = 0
        
    def move(self, width, height):
        # FIX: Ensure X checks against width, and Y checks against height!
        self.x = max(0, min(width - 1, self.x + random.choice([-1, 0, 1])))
        self.y = max(0, min(height - 1, self.y + random.choice([-1, 0, 1])))
        self.age += 1

class BufferedSimulation:
    def __init__(self, width=25, height=12):
        self.width = width
        self.height = height
        self.cells = []
        self.log_message = "System running smoothly."
        self.initialize_population()
        
    def initialize_population(self):
        for _ in range(50): self.cells.append(Cell("Healthy", random.randint(0, self.width-1), random.randint(0, self.height-1)))
        for _ in range(4):  self.cells.append(Cell("T-Cell", random.randint(0, self.width-1), random.randint(0, self.height-1)))
        for _ in range(2):  self.cells.append(Cell("Virus", random.randint(0, self.width-1), random.randint(0, self.height-1)))

    def update(self):
        # Use height and width parameters correctly during movement
        for cell in [c for c in self.cells if c.is_alive]:
            cell.move(self.width, self.height)
            if cell.type == "Healthy" and cell.age > 45: cell.is_alive = False

        living = [c for c in self.cells if c.is_alive]
        for c1 in living:
            for c2 in living:
                if c1 == c2 or c1.x != c2.x or c1.y != c2.y: continue
                if c1.type == "Virus" and c2.type == "Healthy":
                    c2.type, c2.has_virus = "Cancer", True
                    c1.is_alive = False
                if c1.type == "T-Cell" and c2.type == "Cancer":
                    c2.is_alive = False
                    self.log_message = "Immune T-Cell destroyed a tumor!"

        self.cells = [c for c in self.cells if c.is_alive]

    def render_with_buffer(self):
        grid = [["·" for _ in range(self.width)] for _ in range(self.height)]
        for cell in self.cells:
            if cell.type == "Healthy": grid[cell.y][cell.x] = "H"
            elif cell.type == "Cancer": grid[cell.y][cell.x] = "C"
            elif cell.type == "T-Cell": grid[cell.y][cell.x] = "T"
            elif cell.type == "Virus": grid[cell.y][cell.x] = "V"

        buffer = io.StringIO()
        buffer.write("=== BUFFERED IMMUNE SYSTEM SIMULATOR ===\n")
        buffer.write("Legend: H = Healthy  T = T-Cell  C = Cancer  V = Virus\n\n")
        
        for row in grid:
            buffer.write(" ".join(row) + "\n")
            
        buffer.write(f"\n[Status Log]: {self.log_message}\n")
        buffer.write(f"Total Cells Active in Tissue Matrix: {len(self.cells)}\n")
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(buffer.getvalue())
        buffer.close()

# Run Loop
sim = BufferedSimulation()
try:
    for step in range(100):
        sim.update()
        sim.render_with_buffer()
        time.sleep(0.3)
except KeyboardInterrupt:
    print("\nSimulation halted.")