def my(numbers):
    i=0
    min=numbers[0]
    while i<len(numbers):
        if numbers[i]<min:
            min=numbers[i]
        i=i+1
    return min
print(my([8, 6, 4, 8, 4, 50, 2, 7]))


        

        