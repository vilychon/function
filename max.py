def my(numbers):
    i=0
    max=numbers[0]
    while i<len(numbers):
        if numbers[i]>max:
            max=numbers[i]
        i=i+1
    return max
print(my([3,5,7,34,2,89,2,5]))