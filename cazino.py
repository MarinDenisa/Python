n = int(input())
carti = ()
lista=[]
ok=0
for x in range(n):
    nr, stema =input().split()
    list1 =(nr, stema)
    lista.append(list1)
carti =tuple(lista)
for i in range(len(carti)): #parcurgem elem listei
   j=i+1
   ok=0
   for j in range(len(carti)):
       if carti[i][1]== carti[j][1] and carti[i][0]== carti[j][0] :
           ok=ok+1
   if ok>= 3:
       print(carti[i])
       break
 
if ok < 3:
   print("JOC OK")
            

    
