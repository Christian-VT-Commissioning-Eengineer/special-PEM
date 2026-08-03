"""Funciones sencillas para el proyecto de práctica."""


def calcular_total(valores, impuesto=0.0):
    """Devuelve la suma de los valores con el impuesto indicado."""
    if impuesto < 0:
        raise ValueError("El impuesto no puede ser negativo")
    subtotal = sum(valores)
    return round(subtotal * (1 + impuesto), 2)


if __name__ == "__main__":
    ejemplo = calcular_total([100, 50], 0.19)
    print(f"Total: {ejemplo}")

