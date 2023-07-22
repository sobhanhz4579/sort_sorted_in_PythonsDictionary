d={'d':14,'b':10,'a':59}


dNeu1=list(d.keys())
dNeu1.sort()
print(dNeu1)

##############################

dNeu2=list(d.keys(),reverse=True)
dNeu2.sort()
print(dNeu2)

##############################

dNeu4=list(d.keys(),reverse=False)
dNeu4.sort()
print(dNeu4)

###############################



dNeu5=list(d.values())
dNeu5.sort()
print(dNeu5)

###############################

dNeu6=list(d.values(),reverse=True)
dNeu6.sort()
print(dNeu6)

###############################

dNeu7=list(d.values(),reverse=False)
dNeu7.sort()
print(dNeu7)

###############################


dNeu8=list(d.items())
dNeu8.sort()
print(dNeu8)

################################

dNeu9=list(d.items(),reverse=True)
dNeu9.sort()
print(dNeu9)

#################################

dNeu10=list(d.items(),reverse=False)
dNeu10.sort()
print(dNeu10)

#---------------------------------------------

k=sorted(d.keys())
print(k)

#----------------------------------------

v=sorted(d.values())
print(v)

#-----------------------------------------

z=sorted(d.items())
print(z)

#------------------------------------------

s=sorted(d)
print(s)

#-------------------------------------------

neu=sorted(d.items(),key=lambda x:x[0],reverse=False)
print(neu)


for i in neu:
    print(i[0],i[1])

#--------------------------------------------

neu2=sorted(d.items(),key=lambda x:x[0],reverse=True)

for i in neu2:
    print(i[0],i[1])

#-------------------------------------------

neu3=sorted(d.items(),key=lambda x:x[1],reverse=False)

for i in neu3:
    print(i[0],i[1])

#------------------------------------------

neu4=sorted(d.items(),key=lambda x:x[1],reverse=True)

for i in neu4:
    print(i[0],i[1])

#------------------------------------------

c=[(key,value) for (key,value) in sorted(d.items(),key=lambda x:x[1])]
print(c)

#------------------------------------------

c2=[(key,value) for (key,value) in sorted(d.items(),key=lambda x:x[1],reverse=True)]
print(c2)