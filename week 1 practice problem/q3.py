def getBmiStatus(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def printWellnessReport(heights, weights):
    print("\nPerson | Height | Weight | BMI | Status")

    for i in range(len(heights)):
        bmi = weights[i] / (heights[i] ** 2)
        status = getBmiStatus(bmi)

        print(i + 1, "|", heights[i], "|", weights[i],
              "|", round(bmi, 2), "|", status)


n = int(input("Enter number of people: "))

heights = []
weights = []

for i in range(n):
    print("\nPerson", i + 1)
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kg: "))

    heights.append(height)
    weights.append(weight)

printWellnessReport(heights, weights)