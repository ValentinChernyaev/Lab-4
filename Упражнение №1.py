print ("Упражнение №1(1)")
A = [1, 2, 3, 4, 5]
#         0-старт len(A)-стоп 2- шаг
for i in range(0,len(A),2):print(A[i])

print ("Упражнение №1(2)")
A=[]
A = [1, 2, 3, 2, 1]
# максимум A, индекс первого элемента равного макс.
print(max(A),A.index(max(A)))

print ("Упражнение №1(3)")
A=[]
A = [1, 2, 3, 4, 5]
#         len(A)-старт   0-стоп -1- шаг
for i in range(len(A),0,-1):print(A[i-1])

print ("Упражнение №2(1)")
A=[]
A = [1, 2, 3, 4, 5]
for i  in range(0,len(A),1):
    # Для чётных
    if i % 2:A[i], A[i-1] = A[i-1], A[i]
print(A)


print ("Упражнение №2(2) полный сдвиг")
A=[]
A = [1, 2, 3, 4, 5]
for i  in range(0,len(A)-1,1):A.insert(0,(A.pop()))
print(A)

print ("Упражнение №2(2) единичный сдвиг")
A=[]
A = [1, 2, 3, 4, 5]
A.insert(0,(A.pop()))
print(A)
