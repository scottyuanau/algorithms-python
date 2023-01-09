# Smallest Difference
#
#   Write a function that takes in two non-empty arrays of integers, finds the
#   pair of numbers (one from each array) whose absolute difference is closest to
#   zero, and returns an array containing these two numbers, with the number from
#   the first array in the first position.
#
#
#   Note that the absolute difference of two integers is the distance between
#   them on the real number line. For example, the absolute difference of -5 and 5
#   is 10, and the absolute difference of -5 and -4 is 1.
#
#
#   You can assume that there will only be one pair of numbers with the smallest
#   difference.
#
# Sample Input
# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]
#
# Sample Output
# [28, 26]
#

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    print(arrayOne,'\n',arrayTwo)
    index1, index2, result = 0, 0, {}
    result['min'] = float('inf')  # max number
    while index1 < len(arrayOne) and index2 < len(arrayTwo):
        if arrayOne[index1] == arrayTwo[index2]:
            result['num1'] = arrayOne[index1]
            result['num2'] = arrayTwo[index2]
            return [result['num1'], result['num2']]
        else:
            if arrayOne[index1] < arrayTwo[index2]:
                if abs(arrayOne[index1] - arrayTwo[index2]) < result['min']:
                    result['num1'] = arrayOne[index1]
                    result['num2'] = arrayTwo[index2]
                    result['min'] = abs(arrayOne[index1] - arrayTwo[index2])
                index1 += 1
            else:
                if abs(arrayOne[index1] - arrayTwo[index2]) < result['min']:
                    result['num1'] = arrayOne[index1]
                    result['num2'] = arrayTwo[index2]
                    result['min']= abs(arrayOne[index1] - arrayTwo[index2])
                index2 += 1
    return [result['num1'], result['num2']]
test = {
  "arrayOne": [-1, 5, 10, 20, 3],
  "arrayTwo": [26, 134, 135, 15, 17]
}

print(smallestDifference(test['arrayOne'], test['arrayTwo']))

