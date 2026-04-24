# **LAB  Trabajando con la función print()**

## Escenario

El comando **`print()`**, el cual es una de las directivas más sencillas de Python, simplemente imprime una línea de texto en la pantalla.

En tu primer laboratorio:

- Utiliza la función **`print()`** para imprimir la linea **`¡Hola, Mundo!`** en la pantalla. Usa comillas dobles alrededor de la cadena.
    *   **Resultado:** Se ejecutó correctamente usando `print ("¡Hola, Mundo!")`.

- Habiendo hecho eso, usa la función **`print()`** nuevamente, pero esta vez imprime tu nombre.
    *   **Resultado:** Se imprimió el nombre correctamente (ej. `print ("Santiago")`).

- Elimina las comillas dobles y ejecuta tu código. Mira la reacción de Python. ¿Qué tipo de error arroja?
    *   **Observación:** Python registra que el nombre no está definido (ej. `"Arthur" no está definido`). Esto genera un `NameError` ya que interpreta el texto como una variable no declarada.

- Luego, elimina los paréntesis, vuelve a colocar las comillas dobles y ejecuta tu código nuevamente. ¿Qué tipo de error arroja esta vez?
    *   **Observación:** Se genera un error de sintaxis. Python indica que las declaraciones deben ir separadas por nuevas líneas o punto y coma.

- Experimenta todo lo que puedas. Cambia las comillas dobles a comillas simples, usa múltiples funciones **`print()`** en la misma línea, y luego en diferentes líneas. Mira qué pasa.
    *   **Comillas simples:** Funcionan igual que las dobles (ej. `print ('Hola Mundo')`).
    *   **Múltiples funciones en una línea:** 
        *   Si se intentan poner sin separación válida, arroja error de sintaxis.
        *   Si se separan por una coma (ej. `print ("..."), print ("...")`), se ejecutan ambas funciones en la misma línea de código sin errores.

## Evidencias
Se adjuntan las capturas `1.png` y `2.png` que muestran los errores y pruebas descritas anteriormente.
