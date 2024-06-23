print('TimKeo')
def maxKeo(candies, extraCandies):
    result = []
    for i in candies:
        if((i+extraCandies)>= max(candies)):
            result.append('true')
        else:
            result.append('false')
    return result
print(maxKeo([12, 1, 12], 3), end='\n\n\n\n')