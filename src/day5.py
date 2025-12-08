from helpers import get_two_sections
import sys

def parse_ranges(ranges: list):
    def parser(range: str):
        numbers = range.split('-')
        return int(numbers[0]), int(numbers[1])
    return list(map(parser, ranges))

def part1(ranges: list, ingredients: list):
    number_of_fresh_ingredients = 0
    for ingredient in ingredients:
        spoiled = True
        for range in ranges:
            if ingredient >= range[0] and ingredient <= range[1]:
                spoiled = False
                break
        if not spoiled:
            number_of_fresh_ingredients += 1
    print(f"Number of fresh ingredients: {number_of_fresh_ingredients}")

def part2(ranges: list):    
    ranges.sort()
    merged = []
    current_lo, current_hi = ranges[0]
    for new_lo, new_hi in ranges[1:]:
        if new_lo <= current_hi + 1:
            # Extend the current range. Since it's sorted we only ever have higher lows
            current_hi = max(current_hi, new_hi)
        else:
            # 'Close' this range and start a new one
            merged.append((current_lo, current_hi))
            current_lo, current_hi = new_lo, new_hi
    merged.append((current_lo, current_hi))

    all_fresh = sum(hi - lo + 1 for lo, hi in merged)
    print(f"Total number of fresh ingredient IDs: {all_fresh}")

input = get_two_sections("inputs/full/day5.txt")
ranges = parse_ranges(input[0])
ingredients = list(map(lambda id: int(id), input[1]))
part1(ranges, ingredients)
part2(ranges)
