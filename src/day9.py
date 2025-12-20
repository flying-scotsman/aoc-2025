from helpers import get_input

def get_enclosing_space(red_tiles: list):
    r_lo, r_hi, c_lo, c_hi = len(red_tiles), 0, len(red_tiles), 0
    for tile in red_tiles:
        if tile[0] < c_lo:
            c_lo = tile[0]
        if tile[0] > c_hi:
            c_hi = tile[0]
        if tile[1] < r_lo:
            r_lo = tile[1]
        if tile[1] > r_hi:
            r_hi = tile[1]
    return r_lo, r_hi, c_lo, c_hi

def get_rectangle_area(tile1: tuple, tile2: tuple):
    return (1 + abs(tile1[0] - tile2[0])) * (1 + abs(tile1[1] - tile2[1]))

def part1(red_tiles: list):
    max_rectangle_area = 0
    for i in range(len(red_tiles)):
        for j in range(i+1, len(red_tiles)):
            if i == j:
                continue
            rectangle_area = get_rectangle_area(red_tiles[i], red_tiles[j])
            if rectangle_area > max_rectangle_area:
                max_rectangle_area = rectangle_area
    print(f"Largest possible rectangle area: {max_rectangle_area}")

def part2(red_tiles: list):
    # Should I draw in the green tiles? We really need 3 corners as red tiles now.
    pass

red_tiles = get_input("inputs/full/day9.txt")
red_tiles = [(int(el.split(",")[0]), int(el.split(",")[1])) for el in red_tiles]
part1(red_tiles)