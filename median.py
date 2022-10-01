"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        if len(numbers) % 2 ==0:
            index = (len(numbers)/2)-1
            index2 = index + 1
            avg = (numbers[int(index)] + numbers[int(index2)])/2
            print(avg)

        else:
            index = int((len(numbers)-1)/2)
            print(numbers[index])

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

