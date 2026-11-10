print(2+3*4)
print((2+3)*4)

print("Merhaba")
print("Nasılsın")
print("Merhaba") ; print("Nasılsın")

print("Selam", end="-") #end ile printten sonra alt satıra geçme işini iptal edebiliriz. Default değeri end="\n" dir.
print("Nasılsın", end="")
print("Merhaba")
print("Ankara","İstanbul","İzmir",sep="--") # sep ile parametreler arasında neler olacağını gösteririz. Default değeri sep=" " dur.

3+5
2+3
print("Ankara "*5)
print("-"*30,"╗")
print("-"*30,"╗",sep="")

print(7+8)
print(len("Ankara "))
print(str(len("Ankara "))+str(len("İzmir")))
print(str(len("Ankara "))*len("İzmir"))
print(range(10))
print(*range(10))
print(["Maydonoz","Tere"])
print(*["Maydonoz","Tere"])
print(*["Maydonoz","Tere"],sep=",")

a = 5 ; print(a)
a += 5 ; print(a)
a *= 5 ; print(a)
a -= 5 ; print(a)
a /= 3 ; print(a)


print("a" in "Ankara")
print("i" in "Ankara")
print("tere" in["maydonoz","tere"])
print("Tere".lower() in["maydonoz","tere"])

#for a in range(10):
    #print(a)

#for a in range(10): print(a,".sayı")
#for a in range(5,10): print(a,".sayı")
#for a in range(10,20,2): print(a,".sayı")
for a in range(80,40,-5): print(a,".sayı")
