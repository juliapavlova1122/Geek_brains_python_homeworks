# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

identity = True
for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            print(f'{x = } {y = } {z = }         result: {not(x or y or z) == (not x and not y and not z)}')
print(f'{identity = }')

