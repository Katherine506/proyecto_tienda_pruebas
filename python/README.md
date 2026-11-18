# Tarea 2 - Pruebas unitarias en Python

## Curso

Calidad, Verificación y Validación de Software

## Descripción

Implementación de pruebas unitarias para el motor de backend
de una tienda, utilizando Python y unittest.

El proyecto permite gestionar inventario, procesar carritos,
validar stock, aplicar descuentos y calcular impuestos.

La lógica de negocio original no fue modificada.

## Tecnologías y versiones

- Python: 3.8 o superior.
- Versión utilizada para la verificación: Python 3.13.5.
- Framework: unittest (biblioteca estándar de Python).

## Archivos

- store.py: lógica de negocio original.
- test_store.py: 12 pruebas unitarias independientes.

## Ejecución

Abrir una terminal dentro de la carpeta python.

Verificar Python:

    python --version

Ejecutar las pruebas:

    python -m unittest -v test_store.py

En Windows también se puede utilizar:

    py -m unittest -v test_store.py

No se requieren dependencias adicionales.

## Escenarios de prueba

### Grupo 1: Inventario

1. Registro de producto y verificación del stock inicial.
2. Incremento del inventario existente.

### Grupo 2: Validaciones de venta

3. Rechazo de compra con stock insuficiente.
4. Rechazo de dos códigos de descuento.

### Grupo 3: Cálculos financieros

5. Compra sin descuento: subtotal, impuesto y stock.
6. Compra con descuento: descuento antes del impuesto.

### Casos adicionales

7. Compra exactamente igual al stock disponible.
8. Rechazo de tres códigos de descuento.
9. Carrito multiproducto fallido sin modificar inventario.
10. Producto inexistente.
11. Compra exitosa con varios productos.
12. Compra con impuesto del 0 %.

## Resultados esperados

Para dos productos de precio unitario 100:

Sin descuento:

- Subtotal: 200
- Impuesto (13 %): 26
- Total: 226

Con descuento del 10 %:

- Subtotal: 200
- Descuento: 20
- Base imponible: 180
- Impuesto (13 %): 23.40
- Total: 203.40

## Calidad de las pruebas

Las pruebas utilizan setUp para crear un inventario nuevo
antes de cada ejecución.

Se verifican los resultados esperados, las excepciones y
la conservación del inventario ante operaciones fallidas.

## Resultado de referencia

12 pruebas ejecutadas, 12 aprobadas, 0 fallidas.

La cobertura descrita corresponde a escenarios funcionales,
no a un porcentaje medido de líneas de código.
