import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

def detect_circle(grid):
    max_radius = ((row ** 2 + col **2) ** 0.5) / 2
    radius = 1
    circle = []
    while radius <= max_radius:
        for y in range(row):
            for x in range(col):
                center_x = grid[j]
                center_y = grid[i]
            for r in range(radius):
                



with open(args.filename) as f:
    lines = f.readlines()
for i, item in enumerate(lines):
    lines[i] = item.strip('\n')
row = len(lines)
col = max(len(line) for line in lines) if row > 0 else 0
matrix = [['' for x in range(col)] for y in range(row)]
for i in range(row):
    for j in range(col):
        try:    
            matrix[i][j] = lines[i][j]
        except IndexError:
            matrix[i][j] = ''
print(matrix)

detect_circle(matrix)

