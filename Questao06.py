num=int(input("Tabuada do numero: "))

print("Multiplicação")
for x in range(10):
    print("%d x %d = %d" % (num, x+1, num*(x+1)) )
    
print("Soma")
for y in range(10):    
    print("%d + %d = %d" % (num, y+1, num+(y+1)) )
    
print("Subtração") 
for w in range(10):     
    print("%d - %d = %d" % (num, w+1, num-(w+1)) )
    
print("Divisão")
for i in range(1, 11):
        print(f"{num} ÷ {i} = {num/i}")