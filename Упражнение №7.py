


num=0
summa=0
srednee=0


file_in = open("c:\sec.in", "r")

line=str(file_in.readline())
file_in.close


Ryad=[]

Ryad= line.split(' ')

print ("Нужно обработать "+str(len(Ryad))+" оценок")
print ("Последовательность:")
print (' '.join(map(str, Ryad)))

len_ryad=len(Ryad)
for i in range(0,len_ryad,1): Ryad[i]=int(Ryad[i])

summa=Ryad[0]
num=1

for i in range(1,len_ryad,1):
 summa+=Ryad[i]
 num+=1
 if ( Ryad[i-1]==2) and ( Ryad[i])>2:
       summa=summa-Ryad[i-1]
       num-=1

#------------------ВЫВОД--------------------------

srednee=int(summa/num)


print ("Оценка за четверть:")
print (srednee)

output = open('c:\sec.out', 'w')
print (srednee, file=output)
output.close()

