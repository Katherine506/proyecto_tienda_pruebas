# Tarea 2 - Pruebas unitarias en Node.js

## Curso

Calidad, Verificación y Validación de Software

## Descripción

Implementación de pruebas unitarias para un motor de backend
de una tienda utilizando JavaScript y Node.js.

Se verifica la gestión del inventario, validaciones de venta,
descuentos, impuestos y actualización del stock.

La lógica de negocio original no fue modificada.

## Tecnologías y versiones

- Lenguaje: JavaScript.
- Node.js: versión 18 o superior.
- Versión utilizada para la verificación: Node.js 20.12.2.
- Framework: node:test (integrado en Node.js).
- Aserciones: node:assert/strict.

## Archivos

- store.js: lógica de negocio original.
- store.test.js: 12 pruebas unitarias independientes.

## Ejecución

Abrir una terminal dentro de la carpeta nodejs.

Verificar la instalación:

    node --version

Ejecutar las pruebas:

    node --test store.test.js

No se requiere npm install ni instalar Jest.

## Escenarios de prueba

### Grupo 1: Inventario

1. Registro de un producto nuevo y stock inicial.
2. Incremento de unidades de un producto existente.

### Grupo 2: Validaciones de venta

3. Compra con stock insuficiente: error y stock intacto.
4. Compra con dos descuentos: error y stock intacto.

### Grupo 3: Cálculos financieros

5. Compra sin descuento: subtotal, impuestos y stock.
6. Compra con descuento: precedencia matemática correcta.

### Casos adicionales

7. Compra de la cantidad exacta disponible.
8. Intento de aplicar tres descuentos.
9. Carrito con varios productos y stock insuficiente.
10. Producto inexistente.
11. Compra exitosa de varios productos.
12. Impuesto del 0 %.

## Resultados esperados

Para un producto de precio 100 y cantidad 2:

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

Cada caso crea una instancia nueva de Store para mantener
independencia entre las pruebas.

Se utiliza assert.throws para verificar las excepciones,
assert.equal para comprobar inventario y una tolerancia
numérica para verificar los cálculos financieros.

## Resultado de referencia

12 pruebas ejecutadas, 12 aprobadas, 0 fallidas.

La cobertura corresponde a los escenarios funcionales,
no a un porcentaje medido de líneas de código.
