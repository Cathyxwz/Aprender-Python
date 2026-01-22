# Operadores lógicos en Python

# AND → devuelve True solo si ambas condiciones son verdaderas
mi_bool = (4 < 5) and (5 > 6)   
print(mi_bool)   # False, porque la segunda condición es falsa

# OR → devuelve True si al menos una condición es verdadera
mi_bool2 = (10 == 10) or (3 == 3) 
print(mi_bool2)  # True, porque ambas condiciones son verdaderas

# NOT → invierte el valor lógico (True → False, False → True)
mi_bool3 = not 'a' == 'a'        
print(mi_bool3)  # False, porque 'a' == 'a' es True y NOT lo invierte
