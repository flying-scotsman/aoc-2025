from helpers import Grid
from functools import cache

def find_starting_cell(grid: Grid):
    for r in range(grid.num_rows):
        for c in range(grid.num_cols):
            if grid[(r, c)] == "S":
                return r, c
            
@cache
def get_number_of_possible_paths(grid: Grid, cell: tuple):
    """Cached function - I have the starting cell and repeat the same path over and over again."""
    number_of_possible_paths = 0
    while cell[0] < grid.num_rows-1:
        if grid[(cell[0]+1, cell[1])] == "|":
            cell = cell[0]+1, cell[1]
            continue
        elif grid[(cell[0]+1, cell[1])] == ".":
            grid[(cell[0]+1, cell[1])] = "|"
            cell = cell[0]+1, cell[1]
            continue
        grid[(cell[0]+1, cell[1]-1)] = "|"
        grid[(cell[0]+1, cell[1]+1)] = "|"
        number_of_possible_paths += get_number_of_possible_paths(grid, (cell[0]+1, cell[1]-1))
        number_of_possible_paths += get_number_of_possible_paths(grid, (cell[0]+1, cell[1]+1))
        break
    return 1 if not number_of_possible_paths else number_of_possible_paths

def part1(grid: Grid):
    starting_cell = find_starting_cell(grid)
    # Could use a graph and DFS? I think I'd prefer a grid and just roll out the policy then repaint the grid
    # We will progress through the grid row by row
    tachyon_beams = {(starting_cell)}
    num_splits = 0
    for _ in range(grid.num_rows):
        new_tachyon_beams = set()
        for beam_r, beam_c in tachyon_beams:
            if grid[(beam_r+1, beam_c)] == "|":
                # No-op
                continue
            elif grid[(beam_r+1, beam_c)] == ".":
                # Beam continues
                grid[(beam_r+1, beam_c)] = "|"
                new_tachyon_beams.add((beam_r+1, beam_c))
            elif grid[(beam_r+1, beam_c)] == "^":
                # Beam splits
                # I could check if it's already been modified
                grid[(beam_r+1, beam_c-1)] = "|"
                grid[(beam_r+1, beam_c+1)] = "|"
                new_tachyon_beams.add((beam_r+1, beam_c-1))
                new_tachyon_beams.add((beam_r+1, beam_c+1))
                num_splits += 1
        tachyon_beams = new_tachyon_beams
    print(f"Number of splits: {num_splits}")

def part2(grid: Grid):
    starting_cell = find_starting_cell(grid)
    print(f"Number of possible paths: {get_number_of_possible_paths(grid, starting_cell)}")

grid = Grid.from_filename("inputs/full/day7.txt")
# part1(grid)
part2(grid)

# Part 2 is really nice - many worlds interpretation. I need to traverse the grid and instead of counting the splits I count the number of possible paths.
# Can I use recursion? Or is it easier to use iteration? Recursion feels more natural. At each split I call the function number_of_possible_paths