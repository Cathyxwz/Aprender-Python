📚 Lo que aprendí
• Indexación y slicing permiten acceder a caracteres específicos o extraer sub-strings de un texto.
• Los métodos de string (upper(), lower(), split(), join(), find(), replace()) facilitan la manipulación de cadenas.
• Las propiedades de strings como concatenar (+), multiplicar (*), usar triple comillas, in y len() amplían su uso.
• Listas [ ] permiten almacenar colecciones ordenadas y modificables, con métodos como .append(), .pop(), .sort(), .reverse().
• Diccionarios { } guardan pares clave-valor y permiten acceder con .keys(), .values(), .items().
• Tuples ( ) son colecciones ordenadas e inmutables, con métodos como .count() y .index().
• Sets { } son colecciones sin repetidos, no ordenadas, con operaciones como .add(), .remove(), .union().
• Booleanos (True/False) se obtienen con operadores de comparación (>, ==, >=, !=) y se usan en lógica de control.

💡 Mini proyecto: Analizador de texto
Descripción:  
El proyecto consistió en crear un programa que analiza un texto ingresado por el usuario y muestra información relevante sobre él.

Explicación:  
• Se pidió al usuario un texto completo con input().
~~• Se normalizó el texto con .lower() para evitar problemas de mayúsculas/minúsculas.
• Se solicitaron tres letras y se contó cuántas veces aparecían con .count().
• Se calculó el número de palabras usando .split() y len().
• Se mostró la primera y última letra del texto con indexación [0] y [-1].
• Se invirtió el orden de las palabras con .reverse() y " ".join().
• Se verificó si la palabra "Python" estaba presente usando el operador in.

✅ Solución~~
El reto pedía analizar un texto y mostrar estadísticas básicas.
La solución fue usar variables, métodos de string, listas y operadores booleanos para procesar la entrada del usuario y devolver resultados claros en pantalla.