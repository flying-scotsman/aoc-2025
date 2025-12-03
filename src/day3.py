from helpers import get_input

def solution(batteries: list, desired_length: int):
    total_joltage = 0
    for bank in batteries:
        highest_digits = ''
        # Need to save position so that the sequence is curtailed during search
        start_position = 0
        for _ in range(desired_length):
            current_highest_digit = (-1, 0)
            for p in range(start_position, len(bank)):
                if len(bank) - p < desired_length - len(highest_digits):
                    break
                if int(bank[p]) == 9:
                    current_highest_digit = (p, int(bank[p]))
                    break
                if int(bank[p]) > current_highest_digit[1]:
                    current_highest_digit = (p, int(bank[p]))
            highest_digits += str(current_highest_digit[1])
            start_position = current_highest_digit[0] + 1
        total_joltage += int(highest_digits)
    return total_joltage

batteries = get_input("inputs/full/day3.txt")
print(f"Part 1: {solution(batteries, 2)}")
print(f"Part 2: {solution(batteries, 12)}")
