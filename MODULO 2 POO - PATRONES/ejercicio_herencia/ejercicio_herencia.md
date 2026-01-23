## Caso
Se requiere el diseño y desarrollo de un sistema de clases para un juego de rol (RPG, por sus siglas en inglés) que incorporará personajes, enemigos y armas. Es esencial aplicar los principios de encapsulamiento y herencia para estructurar el código de forma que resulte eficiente y fácil de mantener.

 

### Instrucciones
[x] Crea tu pequeño entorno de desarrollo con el fin de llevar a cabo esta actividad de la manera correcta.

[x] Crea un archivo en Python llamado `poo_role_play.py`

[x] Define una clase Personaje con atributos como nombre, nivel, y vida. Incluye un método constructor para inicializar estos atributos y métodos para recibir daño o curarse.

[x] Define una clase Enemigo que herede de Personaje y añade atributos específicos como tipo (por ejemplo, zombi, vampiro) y daño.

[x] Asegura que los atributos de las clases estén adecuadamente encapsulados (Define cuáles encapsular y cuáles no). Utiliza modificadores de acceso para controlar la visibilidad de los atributos y métodos, asegurando que la manipulación de los datos solo pueda hacerse a través de métodos públicos (getters y setters).

[x] Crea al menos una subclase de Personaje adicional que represente otro tipo de entidad en el juego, como Aliado, con características únicas.

[x] Implementa métodos que demuestren la reutilización de código a través de la herencia y la especialización de comportamientos.

[x] Define una clase Arma con atributos como nombre y poder. Asocia esta clase con Personaje para que cada personaje pueda tener un arma equipada.

[x] Escribe un pequeño script que cree instancias de tus clases y demuestre la interacción entre ellas, como batallas entre personajes y enemigos utilizando las armas.

[x] Implementa interacciones entre personajes y enemigos usando las armas, por ejemplo, un método atacar que utilice el poder del arma para reducir la vida del enemigo.

[x] Asegúrate de probar todos los métodos y verificaciones de encapsulamiento, especialmente el correcto funcionamiento de getters y setters.