# Calculadora de Compras para Pausa Activa

Programa simple en Python para calcular el costo total de una compra con descuento condicional.

---

## 1. Entradas, Proceso y Salida

- **Entradas:**
  * Botella de agua: $2.500 c/u.
  * Fruta: $1.800 c/u.
  * Descuento: $1.000 de descuento si el subtotal es de $10.000 o más.
- **Proceso:**
  * `subtotal = (water_qty * 2500) + (fruit_qty * 1800)`
  * `discount = 1000` si `subtotal >= 10000`, de lo contrario `0`
  * `total = subtotal - discount`
- **Salida:** Monto total a pagar.

---

## 2. Pasos de Ejecución

1. Definir o ingresar las cantidades de agua y fruta.
2. Definir los precios unitarios y las reglas de descuento.
3. Calcular los subtotales de cada producto.
4. Sumar ambos valores para obtener el subtotal general.
5. Verificar si el subtotal es >= $10.000 para aplicar el descuento de $1.000.
6. Restar el descuento al subtotal.
7. Mostrar el total final en pantalla.

---

## 3. Variables Utilizadas

- `WATER_PRICE`: $2.500 (Precio unitario del agua)
- `FRUIT_PRICE`: $1.800 (Precio unitario de la fruta)
- `DISCOUNT_THRESHOLD`: $10.000 (Monto mínimo para descuento)
- `DISCOUNT_AMOUNT`: $1.000 (Valor del descuento)
- `water_qty`: Cantidad de botellas de agua
- `fruit_qty`: Cantidad de frutas
- `subtotal`: Costo antes del descuento
- `discount`: Descuento aplicado ($0 o $1.000)
- `total`: Monto final a pagar

---

## 4. Caso de Prueba 1 (Enunciado del Problema)

- **Carrito:** 3 aguas, 2 frutas
- **Subtotal:** (3 × 2.500) + (2 × 1.800) = 7.500 + 3.600 = $11.100
- **Descuento:** $1.000 (dado que $11.100 >= $10.000)
- **Total:** $10.100

---

## 5. Caso de Prueba 2 (Prueba Alternativa)

- **Carrito:** 2 aguas, 1 fruta
- **Subtotal:** (2 × 2.500) + (1 × 1.800) = 5.000 + 1.800 = $6.800
- **Descuento:** $0 (dado que $6.800 < $10.000)
- **Total:** $6.800

---

## 6. Pregunta sobre Ambigüedad

> *"¿El descuento de $1.000 se aplica solo una vez por compra, o es acumulable por cada $10.000 gastados (por ejemplo, $2.000 de descuento si el subtotal alcanza $20.000)?"*

---

## Cómo Ejecutar

```bash
python3 market.py
