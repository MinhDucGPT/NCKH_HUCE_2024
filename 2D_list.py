print('2D list')
List_2D = [[1,2,3],[4,5,6],[7,8,9]]
lst_sub_data = []
for i in range(len(List_2D)):
    lst_sub_data.append([List_2D[i][0],List_2D[i][2]])
print(lst_sub_data,end='\n\n\n\n')