#📝 Planteamiento del Problema
Crear una clase CuentaBancaria con atributos para titular y saldo. Debe tener métodos para depositar y retirar dinero.

💡 Pseudocódigo Sugerido:

```
CLASE CuentaBancaria
  ATRIBUTOS: titular, saldo
  METODO depositar(cantidad)
    saldo = saldo + cantidad
  FIN METODO
  METODO retirar(cantidad)
    SI cantidad <= saldo ENTONCES
      saldo = saldo - cantidad
    SINO
      IMPRIMIR 'Fondos insuficientes'
    FIN SI
  FIN METODO
FIN CLASE
```

##✅ Tareas

- [ ] Implementar la solución en Python.

- [ ] Añadir pruebas unitarias.

- [ ] Documentar el código.
