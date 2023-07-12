list = [100, 200, 300, 400, 500]
print("La lista inicial es: ", list)
list.reverse()
print("La lista luego de voltear es: ", list)

print("=============================1=============================")

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [ f"{list1[x]}{list2[x]}" for x in range(len(list1) if len(list1) < len(list2) else len(list2)) ]
print("La lista final es: ", list3)

print("=============================2==============================")

numbers = [1, 2, 3, 4, 5, 6, 7]
print("Numeros antes de aplicar el cuadrado: ", numbers)
print("numeros luego de aplicar el cuadrado: ", [ x**3 for x in numbers ])

print("=============================3==============================")

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [ f"{a1}{b1}" for a1 in list1 for b1 in list2 ]
print("La lista resultante es: ", list3)

print("=============================4==============================")

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list3 = [ (list1[x], list2[len(list2)-1-x]) for x in range(len(list1) if len(list1) < len(list2) else len(list2)) ]
print("La lista resultante es: ", list3)

print("=============================5==============================")

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2 = filter(None, list1)
print("La lista resultante es: ", [x for x in list2] )

print("=============================9=============================")

list1 = [5, 10, 15, 20, 25, 50, 20]
list1[list1.index(20)] = 200

print("La lista resultante es: ", list1 )

print("=============================10============================")

list1 = [5, 10, 15, 20, 25, 50, 20]
while list1.count(20) > 0:
    list1.pop(list1.index(20))

print("La lista resultante es: ", list1 )

print("=============================12============================")

a,b,c,d = (10, 20, 30, 40)
print(a) # debe mostrar 10
print(b) # debe mostrar 20
print(c) # debe mostrar 30
print(d) # debe mostrar 40

print("=============================13============================")

tuple1 = (11, 22)
tuple2 = (99, 88)
print("tuple1 =  ", tuple1 )
print("tuple2 =  ", tuple2 )

tuple1, tuple2 = tuple2, tuple1
print("tuple1 =  ", tuple1 )
print("tuple2 =  ", tuple2 )

print("=============================15============================")

tuple1 = (50, 10, 60, 70, 50)
print("La cantidad de veces que aparece el 50 es: ", tuple1.count(50) )
