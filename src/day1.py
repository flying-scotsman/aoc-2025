from helpers import get_input
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def parse_instruction(instruction: str) -> int:
    """Assumes the first character is L or R and the rest can be converted to a number."""
    number = int(instruction[1:])
    if instruction[0] == "L":
        return -number
    return number

def part1(instructions: list):
    """Counts the number of times the dial points at zero after any given rotation."""
    raw_cumsum = np.cumsum(instructions_num)
    zeroes = 0
    for i in range(len(instructions)-1):
        if (raw_cumsum[i] + instructions[i+1]) % 100 == 0:
            zeroes += 1
    logger.info(f"Number of zeroes: {zeroes}")

def number_of_crosses(i0: int, i1: int) -> int:
    """Determines the number of times that the dial crosses zero on a rotation.
    
    Assumes that i0 is mod 100."""
    # Conditions for crossing zero:
    # - If the quotient of the absolute sum is r then r times 
    # - If n0 is negative and n1 is more positive, then an extra time
    # - If n0 is positive and n1 is more negative, then an extra time
    number_of_crosses = 0
    instruction_sum = i0 + i1
    number_of_crosses += abs(instruction_sum) // 100
    if (i0 * i1 < 0 and abs(i1) > abs(i0)) or instruction_sum == 0:
        number_of_crosses += 1
    return number_of_crosses

def part2(instructions: list):
    """Counts the number of times the dial passes 0."""
    raw_cumsum = np.cumsum(instructions_num)
    zero_crosses = 0
    for i in range(len(instructions)-1):
        # This time take the modulo first before determining the number of crosses
        zero_crosses += number_of_crosses(raw_cumsum[i] % 100, instructions[i+1])
    logger.info(f"Number of zero crosses: {zero_crosses}")

if __name__ == "__main__":
    instructions = get_input("inputs/full/day1.txt")
    instructions_num = [parse_instruction(i) for i in instructions]
    instructions_num.insert(0, 50)
    part2(instructions_num)