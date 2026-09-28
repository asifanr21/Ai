import time

class EightPuzzle:
    def __init__(self, start_state, goal_state=None):
        self.start = tuple(start_state)
        self.goal = tuple(goal_state) if goal_state else (1, 2, 3, 4, 5, 6, 7, 8, 0)
        self.states_explored = 0

    def print_grid(self, state):
        """Prints the 1D state array as a 3x3 visual grid layout."""
        for i in range(0, 9, 3):
            row = [str(x) if x != 0 else "_" for x in state[i:i+3]]
            print("  [ " + " ".join(row) + " ]")
        print()

    def is_solvable(self, state):
        """
        An 8-puzzle state is solvable if its inversion count is EVEN.
        An inversion is when a tile with a higher number precedes a lower number.
        """
        flat_state = [tile for tile in state if tile != 0]
        inversions = 0
        for i in range(len(flat_state)):
            for j in range(i + 1, len(flat_state)):
                if flat_state[i] > flat_state[j]:
                    inversions += 1
        return inversions % 2 == 0

    def get_neighbors(self, state):
        """Generates valid adjacent states and their moving directions."""
        idx = state.index(0)
        r, c = idx // 3, idx % 3
        neighbors = []
        
      
        moves = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]
        
        for dr, dc, move in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                n_idx = nr * 3 + nc
                new_state = list(state)
                new_state[idx], new_state[n_idx] = new_state[n_idx], new_state[idx]
                neighbors.append((tuple(new_state), move))
        return neighbors

    def _dls(self, state, depth, visited, path):
        """Recursive Depth-Limited Search helper function."""
        self.states_explored += 1
        
        if state == self.goal:
            return path
        if depth <= 0:
            return None
            
        visited.add(state)
        for next_state, move in self.get_neighbors(state):
            if next_state not in visited:
                result = self._dls(next_state, depth - 1, visited, path + [move])
                if result is not None:
                    return result
                    
        visited.remove(state)
        return None

    def solve(self, max_depth=30):
        """Solves the puzzle by progressively deep-searching configurations."""
        print("--- Initializing 8-Puzzle Solver (IDDFS) ---")
        print("Start State:")
        self.print_grid(self.start)
        print("Goal State:")
        self.print_grid(self.goal)

    
        if not self.is_solvable(self.start):
            print("❌ Execution Halted: The provided starting configuration is UNSOLVABLE.")
            return None

        start_time = time.time()
        for depth in range(max_depth):
            visited = set()
            solution_path = self._dls(self.start, depth, visited, [])
            
            if solution_path is not None:
                end_time = time.time()
                self._print_results(solution_path, end_time - start_time)
                return solution_path
                
        print(f"❌ Could not find a solution within a boundary limit of {max_depth} levels.")
        return None

    def _print_results(self, path, elapsed_time):
        """Prints structured summary analytics and execution steps."""
        print("====== SOLUTION FOUND ======")
        print(f"⏱️ Time Taken: {elapsed_time:.4f} seconds")
        print(f"🔄 Total States Visited: {self.states_explored}")
        print(f"📏 Path Length (Optimal Steps): {len(path)}")
        print(f"📋 Step Sequence: {path}\n")
        
        current = self.start
        print("Step-by-Step Playback:")
        print("Start State:")
        self.print_grid(current)
        
        for idx, move in enumerate(path, 1):
            b_idx = current.index(0)
            r, c = b_idx // 3, b_idx % 3
            
            if move == 'Up': n_idx = (r - 1) * 3 + c
            elif move == 'Down': n_idx = (r + 1) * 3 + c
            elif move == 'Left': n_idx = r * 3 + (c - 1)
            elif move == 'Right': n_idx = r * 3 + (c + 1)
            
            temp = list(current)
            temp[b_idx], temp[n_idx] = temp[n_idx], temp[b_idx]
            current = tuple(temp)
            
            print(f"Step {idx} -> Move Blank '{move}':")
            self.print_grid(current)

if __name__ == "__main__":

    easy_puzzle   = [1, 2, 3, 0, 4, 6, 7, 5, 8]
    goal_template = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    puzzle_solver = EightPuzzle(easy_puzzle, goal_template)
    puzzle_solver.solve()
