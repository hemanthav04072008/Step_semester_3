def analyzeInventory(sectionA, sectionB):
    totalA = 0
    totalB = 0

    for quantity in sectionA:
        totalA += quantity

    for quantity in sectionB:
        totalB += quantity

    if totalA == totalB:
        status = "Balanced"
    else:
        status = "Not Balanced"

    maxQuantity = sectionA[0]
    section = "Section A"
    index = 0

    for i in range(len(sectionA)):
        if sectionA[i] > maxQuantity:
            maxQuantity = sectionA[i]
            section = "Section A"
            index = i

    for i in range(len(sectionB)):
        if sectionB[i] > maxQuantity:
            maxQuantity = sectionB[i]
            section = "Section B"
            index = i

    print("Section A Total:", totalA,
          "| Section B Total:", totalB,
          "| Status:", status)

    print("Highest Quantity:", maxQuantity,
          "(" + section + ", Item", index + 1, ")")


sectionA = list(map(int, input("Enter Section A quantities: ").split()))
sectionB = list(map(int, input("Enter Section B quantities: ").split()))

if len(sectionA) == len(sectionB) and len(sectionA) > 0:
    analyzeInventory(sectionA, sectionB)
else:
    print("Enter arrays of equal, non-zero length.")