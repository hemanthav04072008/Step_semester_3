def busiestRow(grid):
    best_row = 0
    max_total = -1

    for i in range(len(grid)):
        total = sum(grid[i])

        if total > max_total:
            max_total = total
            best_row = i

    return best_row, max_total


grid = [
    [2, 0, 1],
    [3, 3, 1],
    [1, 1, 1]
]

row, total = busiestRow(grid)
print("Row", row, "Total", total)