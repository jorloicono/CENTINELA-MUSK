import json
import sys

UMBRAL_BARATO = 15

UMBRAL_CARO = 5

with open("./servidor/datos/catalogo.json", encoding="utf-8") as f:
    articulos = json.load(f)["articulos"]

entrada = input("Introduce el id del artículo (por ejemplo ART-0043): ")

codigo = entrada.strip().upper()    

numero = codigo.removeprefix("ART-")

if not codigo.startswith("ART-") or not numero.isdigit():
    sys.exit("El código de artículo no es válido. Debe tener el formato ART-XXXX, donde XXXX son dígitos.")

posicion = int(numero) - 1

if not (0 <= posicion < len(articulos)):
    sys.exit("El código de artículo no es válido. No existe un artículo con ese código.")

articulo = articulos[posicion]

nombre = articulo["nombre"]
precio = articulo["precio"]
referencia = articulo["precio_referencia"]

stock = articulo["stock"]

descuento = (1 - precio / referencia) * 100

print(f"Artículo: {nombre}")
print(f"Precio: {precio:.2f} €")
print(f"Precio de referencia: {referencia:.2f} €")
print(f"Descuento: {descuento:.2f} %")

if descuento >= UMBRAL_BARATO:
    print("¡Este artículo es barato!")

elif descuento <= UMBRAL_CARO:
    print("¡Este artículo es caro!")

else:
    print("Este artículo tiene un precio normal.")

disponibilidad = "disponible" if stock > 0 else "agotado"
print(f"Disponibilidad: {disponibilidad}")


objetivo_texto = input("Introduce el precio objetivo para " \
"este artículo (por ejemplo 12.50), si no quieres, da enter: ").strip()


if objetivo_texto:
    objetivo = float(objetivo_texto.replace(",", "."))
    if precio <= objetivo and stock > 0: 
        print(f"¡El artículo está por debajo de tu precio objetivo de {objetivo:.2f} € y está disponible!")
    elif precio <= objetivo and stock == 0:
        print(f"El artículo está por debajo de tu precio objetivo de {objetivo:.2f} €, pero está agotado.")
    else: 
        print(f"El artículo está por encima de tu precio objetivo de {objetivo:.2f} €.")