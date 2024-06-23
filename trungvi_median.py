print("Median")
def trungVi(a):
    median = 0
    if (len(a)%2==0):
        median = (a[len(a)//2-1]+a[len(a)//2])/2
    else:
        median = a[(len(a)+1)//2-1]
    return median

def odd(a):
    b = []
    for i in a:
        if(i %2 != 0):
            b.append(i)
    return list(b)

print(trungVi([1,2,3,4,5,6,7,8,9,10]))
print(odd([9, 7, 5, 3, 1]),end='\n\n\n\n')