print("Amstrong")
def Amstrong(a):
    sum = 0
    order = len(str(a))
    temp = a
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if a == sum:
        return True
    return False

list = [130, 270, 153, 407, 177, 371, 1000, 1634, 370]
list = [i for i in range (130, 1635) if Amstrong(i)]
print(list , end="\n\n\n\n")



