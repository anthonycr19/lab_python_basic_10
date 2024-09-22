from funciones import suma as opera_1, multiplica as opera_2

var1 = int(input("Primer valor: "))
var2 = int(input("Segundo valor: "))

sum = opera_1(var1, var2)
print(sum)

mul = opera_2(var1, var2)
print(mul)
