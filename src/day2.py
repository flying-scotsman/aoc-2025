def split_range(range: str):
    numbers = range.split("-")
    return (int(numbers[0]), int(numbers[1]))

def parse_input_into_ranges(input_path: str):
    """Takes the raw input and provides a list of tuple of start and end values."""
    with open(input_path, "r") as f:
        inputs = f.read()
    ranges_str = inputs.split(",")
    return list(map(split_range, ranges_str))

def solution(ranges: list, part1 = True):
    """I need to add stubs of any length now and search through the range.
    
    So I gather stubs up to the halfway point and check if they fit in to the range"""
    # Question: What if IDs are repeated in multiple ranges?
    # Answer: Only count them once
    invalid_ids = set()
    for start, end in ranges:
        stubs = set()
        matched_stubs = set()
        for current in range(start, end+1):
            if len(str(current)) == 1:
                continue
            for i in range(int(len(str(current))/2)):
                potential_stub = str(current)[:i+1]
                if int(potential_stub+potential_stub) <= end and potential_stub not in matched_stubs:
                    stubs.add(potential_stub)
            for stub in stubs:
                multiplier = len(str(current)) / len(stub)
                if not int(multiplier) == multiplier or multiplier == 1:
                    continue
                if part1 and multiplier != 2:
                    continue
                if int(multiplier) * stub == str(current):
                    invalid_ids.add(current)
                    # Avoid reading the stub later
                    matched_stubs.add(stub)
            # Can't modify the set while reading from it so modify it once at the end
            stubs -= matched_stubs
    print(f"Sum of invalid IDs: {sum(id for id in invalid_ids)}")

ranges = parse_input_into_ranges("inputs/full/day2.txt")
solution(ranges, False)