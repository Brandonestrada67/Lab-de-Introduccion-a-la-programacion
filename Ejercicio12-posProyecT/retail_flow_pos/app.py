from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import random 

app = Flask(__name__)
app.secret_key = 'retail_flow_secret_uaz_2024'

# 1. Base de datos simulada
PRODUCTS = {
    "PROD-001": {"name": "Aceite de Oliva Extra Virgen 1L", "price": 12.50, "category": "ALIMENTOS", "stock": 12, "min_stock": 20, "status": "Bajo"},
    "PROD-109": {"name": "Detergente Líquido Floral 3L", "price": 15.90, "category": "LIMPIEZA", "stock": 5, "min_stock": 15, "status": "Crítico"},
    "PROD-042": {"name": "Arroz Integral Premium 5kg", "price": 8.20, "category": "ALIMENTOS", "stock": 85, "min_stock": 30, "status": "Óptimo"},
    "PROD-215": {"name": "Pack Leche Entera 6x1L", "price": 6.80, "category": "LÁCTEOS", "stock": 45, "min_stock": 25, "status": "Óptimo"}
}

# 2. Códigos Reales
REAL_LOOKUP = {
    "7501031360128": "Powerade Moras 600ml",
    "7501055300075": "Coca-Cola Original 600ml",
    "7501000111200": "Sabritas Sal 45g",
    "7501025410123": "Gansito Marinela"
}

# VARIABLES GLOBALES PARA COMPARTIR ENTRE CELULAR Y COMPU
SHARED_CART = []
SHARED_HISTORY = []

@app.route('/')
def login():
    global SHARED_CART
    SHARED_CART = []  # Limpia el carrito al iniciar
    return render_template('login.html')

@app.route('/checkout')
def checkout():
    subtotal = sum(item['price'] * item['quantity'] for item in SHARED_CART)
    iva = subtotal * 0.16
    total = subtotal + iva
    return render_template('checkout.html', cart=SHARED_CART, subtotal=subtotal, iva=iva, total=total)

@app.route('/scan', methods=['GET', 'POST'])
def scan():
    global SHARED_CART
    if request.method == 'POST':
        sku = request.form.get('sku', '').strip()
        found = False
        
        for item in SHARED_CART:
            if item['sku'] == sku:
                item['quantity'] += 1
                found = True
                break
        
        if not found:
            if sku in PRODUCTS:
                p = PRODUCTS[sku]
                name, price = p['name'], p['price']
            elif sku in REAL_LOOKUP:
                name = REAL_LOOKUP[sku]
                price = round(random.uniform(20, 100), 2)
            else:
                name = f"Producto {sku}"
                price = round(random.uniform(20, 100), 2)

            SHARED_CART.append({"sku": sku, "name": name, "price": price, "quantity": 1})
        
        return redirect(url_for('checkout'))
    return render_template('scan.html')

@app.route('/payment')
def payment():
    total = sum(item['price'] * item['quantity'] for item in SHARED_CART) * 1.16
    return render_template('payment.html', total=total)

@app.route('/process_payment')
def process_payment():
    global SHARED_CART, SHARED_HISTORY
    if SHARED_CART:
        subtotal = sum(item['price'] * item['quantity'] for item in SHARED_CART)
        total = subtotal * 1.16
        sale = {
            "id": len(SHARED_HISTORY) + 1001,
            "hora": datetime.now().strftime("%H:%M:%S"),
            "items": sum(item['quantity'] for item in SHARED_CART),
            "total": total
        }
        SHARED_HISTORY.insert(0, sale)
        SHARED_CART = [] # Vaciamos el carrito tras pagar
    return redirect(url_for('checkout'))

@app.route('/clear')
def clear_cart():
    global SHARED_CART
    SHARED_CART = []
    return redirect(url_for('checkout'))

# --- RUTAS DE LOS MÓDULOS QUE FALTABAN ---

@app.route('/reports')
def reports():
    total_dia = sum(sale['total'] for sale in SHARED_HISTORY)
    return render_template('reports.html', history=SHARED_HISTORY, total_dia=total_dia)

@app.route('/authorizations')
def authorizations():
    pending = [{"id": 1, "tipo": "Cancelación", "motivo": "Error de cobro", "usuario": "Cajero 02"}]
    return render_template('authorizations.html', pending=pending)

@app.route('/returns', methods=['GET', 'POST'])
def returns():
    ticket_info = None
    error = None
    if request.method == 'POST':
        ticket_id = request.form.get('ticket_id', '').strip().replace('#', '')
        try:
            for sale in SHARED_HISTORY:
                if sale['id'] == int(ticket_id):
                    ticket_info = sale
                    break
            if not ticket_info: error = "Ticket no encontrado."
        except: error = "ID no válido."
    return render_template('returns.html', ticket_info=ticket_info, error=error)

@app.route('/inventory')
def inventory():
    return render_template('inventory.html', products=PRODUCTS)

if __name__ == '__main__':
    # host='0.0.0.0' expone la app a tu Wi-Fi local
    app.run(host='0.0.0.0', port=5000, debug=True)