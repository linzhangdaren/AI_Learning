import numpy as np

vector1 = np.array([[3,2,1],[1, 2, 3],[2, 1, 0]])
vector2=np.array([[4,5,6],[2, 2, 1],[5, 1, 3]])

#计算点积
result_dot=np.dot(vector1,vector2)
print(result_dot)