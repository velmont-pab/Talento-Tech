monto_compra=0
stock_disponible=0
cliente_activo=True
vale_promocional=True

venta_valida=((monto_compra>0 and stock_disponible>0) and cliente_activo) or vale_promocional
if venta_valida:
    print("Venta realizada") 
if ((monto_compra>0 and stock_disponible>0) and cliente_activo) or vale_promocional:
    print("Venta realizada")