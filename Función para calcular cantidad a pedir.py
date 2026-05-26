# Función para calcular cantidad a pedir
#Jhon Roa 
#Grupo:213022A 2201 
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Inventario de productos tecnológicos (10 productos)
inventario = [
    ["T001", "Laptop", 3, 10],
    ["T002", "Mouse", 25, 20],
    ["T003", "Teclado", 5, 15],
    ["T004", "Monitor", 8, 8],
    ["T005", "Impresora", 2, 6],
    ["T006", "Tablet", 4, 10],
    ["T007", "Disco Duro", 12, 10],
    ["T008", "Memoria USB", 30, 25],
    ["T009", "Audífonos", 6, 12],
    ["T010", "Cámara Web", 1, 5]
]

print("=== LISTA DE PEDIDOS TECNOLÓGICOS ===\n")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print(f"Código: {codigo} | Producto: {nombre} | Pedido: {cantidad_pedir}")