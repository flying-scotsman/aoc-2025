from helpers import Grid

def get_reachable_rolls(grid: Grid):
    # Brute force is to check every single cell individually and accrue the list of valid positions this way
    # This is O(8*N) - if I then have to check more than 8 in part 2 it's no good
    # How can we accumulate the information of the ones we've checked?
    # Let's brute force it for now. Turns out there's nothing better for this problem.
    reachable_rolls = []
    for r in range(grid.num_rows):
        for c in range(grid.num_cols):
            cell = (r, c)
            if grid[cell] != '@':
                continue
            # Check all round this cell - 8 cells to check
            number_of_adjacent_rolls = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if (dr == 0 and dc == 0) or r+dr < 0 or c+dc < 0:
                        continue
                    if grid[(r+dr, c+dc)] == '@':
                        number_of_adjacent_rolls += 1
            if number_of_adjacent_rolls < 4:
                reachable_rolls.append(cell)
    print(f"Number of reachable rolls: {len(reachable_rolls)}")
    return reachable_rolls

def part2(grid: Grid):
    reachable_rolls = get_reachable_rolls(grid)
    total_rolls_removed = 0
    while len(reachable_rolls) > 0:
        for roll in reachable_rolls:
            grid[roll] = 'x'
        total_rolls_removed += len(reachable_rolls)
        reachable_rolls = get_reachable_rolls(grid)
    print(f"Total rolls removed: {total_rolls_removed}")

grid = Grid.from_filename("inputs/full/day4.txt")
part2(grid)