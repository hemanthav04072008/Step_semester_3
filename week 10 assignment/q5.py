def busiestRow(grid):
    best_row = 0
    best_total = sum(grid[0])

    for i in range(1, len(grid)):
        total = sum(grid[i])

        if total > best_total:
            best_total = total
            best_row = i

    return best_row, best_total


grid = [
    [2, 0, 1],
    [3, 3, 1],
    [1, 1, 1]
]

row, total = busiestRow(grid)

print(f"Row {row}, Total {total}")