import numpy as np
n=np.random.randint(10,size=(2,2))
print(n)

print("determinant")
print(np.linalg.det(n))

print("inverse")
print(np.linalg.inv(n))

print("matrix Rank")
print(np.linalg.matrix_rank(n))

------------
output

[[3 9]
 [1 4]]
determinant
3.0000000000000004
inverse
[[ 1.33333333 -3.        ]
 [-0.33333333  1.        ]]
matrix Rank
2
