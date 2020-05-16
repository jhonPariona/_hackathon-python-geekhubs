precio = 3.49
descuento = 0.6

barras_vendidas = input("Introduce el numero de barras vendidas \n")
barras_no_frescas = input(
    "Introduce el numero de barras que no sean frescas \n")

precio_habitual = int(barras_vendidas) * precio

precio_descuento = precio_habitual - \
    (precio*descuento*int(barras_no_frescas))

print("precio habitual", precio_habitual)
print("precio descuento", precio_descuento)
