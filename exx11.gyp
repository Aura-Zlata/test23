n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
# if n<10:
for i in range(0,n):
    x=int(input('Dati elementul='))
    a.extend([x])
print(a)

print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
print(a[:5])

print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')
print(a[::-1])

print('c)  sortează componentele tabloului în ordine descrescătoare;')

b=sorted(a)
b.sort(reverse=True)
print(b)

print('d)  afişează pe ecran doar componentele pare;')
q=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        q.extend([y])
print(q)

print('e)  afişează pe ecran media aritmetică a componentelor pare;')
print(sum(q)/len(q))

print('f)  afişează pe ecran doar componentele impare;')
ih=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        y=a[i]
        ih.extend([y])
print(ih)

print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x=int(input(' x = '))
y=int(input(' y = '))
k=[]
for i in a:
    if ((i>x) and (i%y!=0)):
        r=i
        k.extend([r])
print(k)

print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
x1=int(input('valoarea x= '))
y1=int(input('valoarea y= '))
s=[]
for i in range(0,len(a)):
    if ((a[i]>x) and (a[i]<y)):
        w=a[i]
        s.extend([w])
print(s)

print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
t=[]
for i in ih:
    if i<0:
        t.extend([a.index(i)])
print(t)        

print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
for i in a:
    if (i < 100 and i>9) or (i > -100 and i <9):
        print(a.index(i))

print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
j=a.copy()
j[0]=min(j)
print(j)

print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
o=a.copy()
o[o.index(min(o))]=o[0]

print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
print('q=',q) 

print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
p=[]
for i in a:
    if i%3==0:
        p.append(i)
print(p)

print('o)  creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori.')