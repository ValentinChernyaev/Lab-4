


file_in = open("c:\sec.in", "r")

count_num=int(file_in.readline())


line=str(file_in.readline())
file_in.close

num=[]
num_swap=[]

num = line.split(' ')
print ("Нужно обработать "+str(count_num)+" чисел")
print ("Полная последовательность чисел:")
print (num)


if count_num%2==0:
    count=int(count_num/2)
    count=int((count_num-1)/2)
for i in range(0,count,1):

  num_swap.append(num[i])
  num_swap.append(num[count_num-i-1])


if count_num%2!=0: num_swap.append(num[count])



print (' '.join(map(str, num_swap)))

output = open('c:\sec.out', 'w')
print (' '.join(map(str, num_swap)), file=output)
output.close()

