from random import randint

numero1 = randint(1,45)

numero2 = randint(1,45)
while numero1 == numero2:
    numero2 = randint(1,45)

numero3 = randint(1,45)
while numero1 == numero3 or numero2 == numero3:
    numero3 = randint(1,45)

numero4 = randint(1,45)
while numero1 == numero4 or numero2 == numero4 or numero3 == numero4:
    numero4 = randint(1,45)
    
numero5 = randint(1,45)
while numero1 == numero5 or numero2 == numero5 or numero3 == numero5\
      or numero4 == numero5:
    numero5 = randint(1,45)

numero6 = randint(1,45)
while numero1 == numero6 or numero2 == numero6 or numero3 == numero6\
      or numero4 == numero6 or numero5 == numero6:
    numero6 = randint(1,45)

print('Los números premiados son:')
print(numero1, numero2, numero3, numero4, numero5, numero6)

