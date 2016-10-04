delta=1000000
delta_now=1000000

file_in = open("c:\sec.in", "r")

N=int(file_in.readline())


line=str(file_in.readline())




file_in.close

Ryad=[]

Ryad= line.split(' ')
print ("Нужно обработать "+str(N)+" чисел")
print ("Последовательность:")
print (' '.join(map(str, Ryad)))
len_ryad=len(Ryad)

for i in range(0,len_ryad,1): Ryad[i]=int(Ryad[i])



max=max(Ryad)
min=min(Ryad)
mediana=int((min+max)/2)

i=0

for i in range(0,len_ryad,1):
    if Ryad[i]==mediana:
        index=i
        break
    else:
     if Ryad[i]<mediana:
       delta_now=mediana-Ryad[i]
     else:
      delta_now=Ryad[i]-mediana

     if delta_now<delta:
        delta=delta_now
        index=i
    i+=1





print ("Медиана (значение, индекс):")
print (Ryad[index], index)

output = open('c:\sec.out', 'w')
print (Ryad[index], file=output)
output.close()

