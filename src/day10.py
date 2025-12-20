from helpers import get_input
import re
import z3
from collections import defaultdict

def parse_input(line: str):
    a = re.match(r"(\[.+\])(.+)(\{.+\})", line)
    indicators = [i for i in a.group(1)[1:-1]]
    buttons = [el for el in a.group(2).split(" ") if el]
    buttons = [[int(i) for i in re.findall(r"[0-9]", button)] for button in buttons]
    joltage = [int(i) for i in a.group(3)[1:-1].split(",")]
    return indicators, buttons, joltage

def press_button(indicators: list, button: list):
    for digit in button:
        if indicators[digit] == ".":
            indicators[digit] = "#"
        else:
            indicators[digit] = "."
    return indicators

def breadth_first_search(desired_indicators: list, current_indicators: list, buttons: list):
    queue = list(zip([current_indicators]*len(buttons), buttons, [0]*len(buttons)))
    observed_patterns = set()
    while queue:
        # print(f"Queue length: {len(queue)}")
        current_indicators, button, number_of_presses = queue.pop(0)
        new_current_indicators = press_button(current_indicators.copy(), button)
        number_of_presses += 1
        if new_current_indicators == desired_indicators:
            break
        for button in buttons:
            if (tuple(new_current_indicators), tuple(button)) not in observed_patterns:
                queue.append((new_current_indicators, button, number_of_presses))
                observed_patterns.add((tuple(new_current_indicators), tuple(button)))
    return number_of_presses

def get_constraints(buttons: list, joltage: list):
    constraints = defaultdict(list)
    for slot in range(len(joltage)):
        for pos, button in enumerate(buttons):
            if slot in button:
                constraints[slot].append(pos)
    return constraints

def part1(inputs: list):
    number_of_presses = []
    for indicators, buttons, _ in inputs:
        number_of_presses.append(breadth_first_search(indicators, ["."]*len(indicators), buttons))
    print(f"Total fewest number of presses: {sum(number_of_presses)}")

def part2(inputs: list):
    number_of_presses = []
    for _, buttons, joltage in inputs:
        # Use z3.Optimize to find the smallest number of button presses including all the constraints
        # First construct the variables to be optimized - one per button
        button_presses = [z3.Int(f"b{i}") for i in range(len(buttons))]
        # Then construct the equations using the joltages - only the variables that contribute to a certain voltage count
        # Sum a list of contributing coefficients in the constraint
        constraints = get_constraints(buttons, joltage)
        op = z3.Optimize()
        for i, slot in enumerate(joltage):
            sliced_button_presses = (button_presses[j] for j in constraints[i])
            op.add(sum(sliced_button_presses) == slot)
        for b in button_presses:
            op.add(b >= 0)
        op.minimize(sum(button_presses))
        if op.check() == z3.sat:
            out = op.model()
            number_of_presses.append(sum(out[b].py_value() for b in button_presses))
    print(f"Total fewest number of presses: {sum(number_of_presses)}")

inputs = get_input("inputs/full/day10.txt")
inputs = [parse_input(line) for line in inputs]
part2(inputs)