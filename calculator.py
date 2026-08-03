"""Funciones sencillas para el proyecto de práctica."""


def calcular_total(valores, impuesto=0.0, descuento=0.0):
    """Devuelve la suma con el descuento y después aplica el impuesto."""
    if impuesto < 0:
        raise ValueError("El impuesto no puede ser negativo")
    if not 0 <= descuento <= 1:
        raise ValueError("El descuento debe estar entre 0 y 1")
    subtotal = sum(valores)
    subtotal_con_descuento = subtotal * (1 - descuento)
    return round(subtotal_con_descuento * (1 + impuesto), 2)


if __name__ == "__main__":
    ejemplo = calcular_total([100, 50], 0.19)
    print(f"Total: {ejemplo}")
