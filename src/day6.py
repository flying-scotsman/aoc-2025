from helpers import get_input
import re
from collections import defaultdict
import operator

def get_columns(input):
    columns = defaultdict(list)
    for line in input:
        items = re.split(r'\s+', line.strip())
        for row, item in enumerate(items):
            typecast = int if line != input[-1] else str
            columns[row].append(typecast(item))
    return columns

def get_columns_with_spaces(input: str):
    columns = []
    # First pad the lines with spaces up to the longest
    length = max(len(l) for l in input)
    for i in range(len(input)):
        input[i] += " " * (length - len(input[i]))
    counter = 0
    last_save = 0  # This means I don't have to delete the input
    while counter < length:
        if counter == length - 1:
            columns.append([line[last_save:] for line in input])
            break
        spacer = True
        for line in input:
            if line[counter] != " ":
                spacer = False
                break
        if not spacer:
            counter += 1
            continue
        # Cut off the input up to this point and add it to a new column
        columns.append([line[last_save:counter] for line in input])
        counter += 1
        last_save = counter
    return columns


def part1(path: str):
    columns = get_columns(get_input(path))
    total = 0
    for column in columns.values():
        if column[-1] == "*":
            op = operator.mul
        elif column[-1] == "+":
            op = operator.add
        else:
            RuntimeError("Operator not supported!")
        subtotal = column[0]
        for num in column[1:-1]:
            subtotal = op(subtotal, num)
        total += subtotal
    print(f"Cephalopod total: {total}")

def get_operands(column: str):
    # Multiplication and addition are commutative so I don't need to be concerned about order
    operands = []
    for i in range(len(column[0])):
        operands.append(int("".join([el[i] for el in column])))
    return operands

def part2(path: str):
    columns = get_columns_with_spaces(get_input(path))
    total = 0
    for column in columns:
        if column[-1].strip() == "*":
            subtotal = 1
            op = operator.mul
        elif column[-1].strip() == "+":
            subtotal = 0
            op = operator.add
        else:
            RuntimeError("Operator not supported!")
        operands = get_operands(column[:-1])
        for num in operands:
            subtotal = op(subtotal, num)
        total += subtotal
    print(f"True cephalopod total: {total}")

part2("inputs/full/day6.txt")
