#formatação
a = 1
b = 2
c = 3

#exemplo 1
string = "a={} b={} c={}"          # segue a ordem dentro
format = string .format(a, b, c)   # dos parênteses
#print(format)

#exemplo 2
string1 = "a={0} b={1} c={2}"     #índice começa no 0
format1 = string1 .format(a, b, c)
#print(format1)

#exemplo 3
string2 = "a={name2} b={name3} c={name1}"       
format2 = string2 .format(name1=a, name2=b, name3=c)  #names= parâmetro
print(format2)                                        #a, b, c= argumentos










a ='oi'
b ='tudo bem?'
c ='yes'
oi = '{}, {} {}'
formato = oi .format( a, b, c)
#print(formato)