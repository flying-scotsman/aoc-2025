# Feels like a graph problem. I think I have to compute the distance between all junction boxes pairwise, this is expensive.
from helpers import get_input, Graph
import math

def euclidean_distance(a, b):
    """Determines the Euclidean distance between two 3d vectors."""
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def get_all_euclidean_distances(junction_boxes: list):
    euclidean_distances = dict()
    for i in range(len(junction_boxes)):
        for j in range(i + 1, len(junction_boxes)):
            if i == j:
                continue
            euclidean_distances[(i, j)] = euclidean_distance(junction_boxes[i], junction_boxes[j])

    return euclidean_distances

def part1(junction_boxes: list, junction_box_graph: Graph, all_euclidean_distances: list):
    
    for con in range(1000):
        junction_box_graph.add(junction_boxes[all_euclidean_distances[con][0][0]], junction_boxes[all_euclidean_distances[con][0][1]])  

    largest_circuits = sorted(junction_box_graph.find_connected_components(), key = lambda x: len(x), reverse=True)
    print(f"Answer: {len(largest_circuits[0]) * len(largest_circuits[1]) * len(largest_circuits[2])}")

def part2(junction_boxes: list, junction_box_graph: Graph, all_euclidean_distances: list):
    con = -1
    while len(junction_box_graph.dfs(junction_boxes[0])) != len(junction_boxes):
        con += 1
        box1 = junction_boxes[all_euclidean_distances[con][0][0]]
        box2 = junction_boxes[all_euclidean_distances[con][0][1]]
        junction_box_graph.add(box1, box2)
    print(f"Length for extension cable: {box1[0] * box2[0]}")



junction_boxes = list(map(lambda x: tuple(int(el) for el in x.split(",")), get_input("inputs/full/day8.txt")))
junction_box_graph = Graph()
for box in junction_boxes:
    junction_box_graph.add_node(box)    
all_euclidean_distances = get_all_euclidean_distances(junction_boxes)
all_euclidean_distances = [(k, v) for k, v in sorted(all_euclidean_distances.items(), key=lambda item: item[1])]    

part2(junction_boxes, junction_box_graph, all_euclidean_distances)
