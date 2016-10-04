

file_in = open("c:\sec.in", "r")


line=str(file_in.readline())



jumps=int(file_in.readline())

file_in.close

Ryad=[]

Ryad= line.split(' ')
print ("Нужно обработать "+str(jumps)+" секунд(ы)")
print ("Последовательность расстановки кузнечиков до прыжков:")
print (' '.join(map(str, Ryad))) # Переделать в формат без запятых


len_ryad=len(Ryad)


for i in range(1,jumps+1,1):
  jump=int(Ryad.pop())
  Ryad.insert((len_ryad-1-jump), jump)
#------------------------------------------------------------------


print ("Последовательность расстановки кузнечиков после прыжков:")
print (' '.join(map(str, Ryad)))

output = open('c:\sec.out', 'w')
print (' '.join(map(str, Ryad)), file=output)
output.close()

