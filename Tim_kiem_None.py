print("BAI Tim kiem None")
List_All = [1, 1.1,None, 1.4, None, 1.5, None,2]
List_None = []
for i in range(len(List_All)):
    if (List_All[i] is None):
        List_None.append(i)
print("Vị trí None đầu tiên là: ", List_None[0],end=" - ")
print("Danh sách vị trí có giá trị None là: ", List_None, end='\n\n\n\n')