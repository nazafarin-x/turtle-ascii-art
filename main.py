import argparse
import turtle


parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

# def draw_circle(center_x, center_y, r):

#     turtle.goto(center_x, center_y)
#     turtle.circle(radius= r)
#     turtle.done()

def detect_circle(grid, center_x, center_y, r, row, col):
    
    circle = []
    scale_x = 0.7
    scale_y = 1.0
    dx = None
    dy = None

    if (center_x - r < 0 or center_x + r >= col or center_y - r < 0 or center_y + r >= row):
        return False
    
    for y in range(row):
        for x in range(col):
            dx = (x - center_x) * scale_x
            dy = (x - center_y) * scale_y
            distance = dx ** 2 + dy ** 2
            if (r - 1) ** 2 <= distance <= (r + 1) ** 2:
                circle.append((x, y))
    
    if not circle:
        return
    
    filled = 0

    for x, y in circle:
        if grid[y][x] != " ":
            filled += 1

    ratio = filled / len(circle)
    print(f"ratio is: {ratio}")
    return ratio >= 0.8
 


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
            matrix[i][j] = ' '
# max_r = min(row, col * 0.5) // 2
# print(max_r)
for i in range(row):
    for j in range(col):
        for radius in range(1, min(row, int(col * 0.7)) // 2 + 1):
            print(f"radius is: {radius}")
            if detect_circle(matrix, j, i, radius, row, col):
                #draw_circle(j, i, radius)
                print(f"circle dtected! center: ({j}, {i}), radius:{radius}")


