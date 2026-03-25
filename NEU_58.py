height_weight_age = [70, # inches,
 170, # pounds,
40 ] # years

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

a = [20, 30, 40]
b = [30, 40, 50]

print(vector_add(a, b))

A = [[1, 2, 3], # A has 2 rows and 3 columns
 [4, 5, 6]]
B = [[1, 2], # B has 3 rows and 2 columns
 [3, 4],
 [5, 6]]

def shape(A):
 num_rows = len(A)
 num_cols = len(A[0]) if A else 0 # number of elements in first row
 return num_rows, num_cols

print(shape(A))

print("_________")

def make_matrix(num_rows, num_cols, entry_fn):
 """returns a num_rows x num_cols matrix
 whose (i,j)th entry is entry_fn(i, j)"""
 return [[entry_fn(i, j) # given i, create a list
 for j in range(num_cols)] # [entry_fn(i, 0), ... ]
 for i in range(num_rows)] # create one list for each i


def is_diagonal(i, j):
 """1's on the 'diagonal', 0's everywhere else"""
 return 2 if i == j else 0
print(is_diagonal(5,5))

identity_matrix = make_matrix(5, 5, is_diagonal)
print(identity_matrix)

