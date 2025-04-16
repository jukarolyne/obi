v = int(input("digite uma conta"))
a = int(input("digite uma conta"))
f = int(input("digite uma conta"))
p = int(input("digite uma conta"))

contas_pagas=0

if v>=a:
   contas_pagas+=1
   v-=a
if v>=f:
   contas_pagas+=1
   v-=f
if v>=p:
   contas_pagas+=1
   v-=p
print(contas_pagas)