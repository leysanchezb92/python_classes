# Sistema de gestión de medios de comunicación

Se requiere diseñar y desarrollar una jerarquía de clases que represente diferentes tipos de medios de comunicación. Utilizarás el polimorfismo para permitir la interacción uniforme con todos los tipos de medios a través de una interfaz común, y aplicarás la abstracción para definir una clase base que encapsule las características comunes de estos medios.

 

## Instrucciones
[x] Crea un archivo llamado `medios.py` en el cual estarás trabajando esta actividad

[] Luego, crea una clase abstracta llamada Medio que incluya atributos comunes como título, autor, y fecha de publicación. Además, define un método abstracto describir() que las subclases deberán implementar para proporcionar detalles específicos sobre el medio.

- Implementación de clases Hijas:

[x] Clase Libro: Deriva de Medio e implementa el método describir() para incluir detalles como género y número de páginas.

[x] Clase Revista: Deriva de Medio y añade atributos como tema y periodicidad. Su implementación de describir() debe manejar estos nuevos atributos.

[x] Clase Periódico: Similar a Revista, pero debe diferenciarse en cómo presenta su descripción, enfocando en noticias y la frecuencia diaria o semanal.

[x] Asegúrate de que se pueda utilizar el método describir() polimórficamente en un contexto donde no se conozca el tipo específico de medio de comunicación, como en un array de Medio.

[x] Escribe un script que cree instancias de cada tipo de medio, las agregue a una lista y luego itere sobre esa lista invocando el método describir() para demostrar el polimorfismo.