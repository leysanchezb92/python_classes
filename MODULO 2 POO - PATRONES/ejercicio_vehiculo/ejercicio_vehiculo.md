# Ejercicio de POO en Python: Simulación de Vehículos
Este ejercicio tiene como objetivo poner en práctica los cuatro pilares de la Programación Orientada a Objetos (POO): Herencia, Encapsulación, Abstracción y Polimorfismo.

## Descripción del Ejercicio
El proyecto consiste en simular una pequeña flota de vehículos, demostrando cómo cada concepto de la POO se aplica en un escenario práctico.

### Paso 1: Configuración (Abstracción)
- [x] Crea una clase base abstracta llamada Vehiculo que no se pueda instanciar directamente.

- [x] Esta clase debe tener los siguientes atributos en su constructor (__init__):

- [x] marca (string)

- [x] modelo (string)

- [x] Define un atributo protegido llamado _velocidad_actual que inicie en 0.

- [x] Crea un método abstracto llamado consumir_combustible(). Este método no debe tener una implementación en la clase Vehiculo.

### Paso 2: Herencia y Encapsulación
- [x] Crea una clase Auto que herede de Vehiculo.

- [x] Añade un atributo de instancia combustible que inicie en 100.

- [ ] Implementa el método consumir_combustible(): su lógica debe ser que por cada 10 km que se desplaza, consume 2 unidades de combustible.

- [ ] Crea un método público llamado acelerar(kilometro) que incremente la _velocidad_actual y, a su vez, llame al método consumir_combustible() para reflejar el gasto.

### Paso 3: Herencia y Polimorfismo
- [ ] Crea una clase Bicicleta que también herede de Vehiculo.

- [ ] En esta clase, no necesitas un atributo de combustible.

- [ ] Implementa el método consumir_combustible() para que devuelva un mensaje que indique que la bicicleta no usa combustible.

- [ ] Implementa el método acelerar(kilometro) de manera diferente: que incremente la velocidad de la bicicleta y muestre un mensaje que refleje que es impulsada por la fuerza humana.

### Paso 4: Demostración (Polimorfismo en Acción)
- [ ] Instancia tres objetos de las clases que creaste: un objeto Auto, un objeto Moto (puedes crearlo para practicar más) y un objeto Bicicleta.

- [ ] Guarda estos tres objetos en una lista.

- [ ] Recorre la lista con un bucle for y, en cada iteración, llama al método acelerar() en cada objeto. Observa cómo cada objeto responde de manera diferente a la misma llamada de método.