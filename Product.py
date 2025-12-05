Catalog = {
    'items': 2,
    'Products': [
        {'product_id': 101, 'product_name': 'Laptop', 'price': 999.99, 'stock': True},
        {'product_id': 102, 'product_name': 'Smartphone', 'price': 499.99, 'stock': False}
    ]
}
print("product details:")
for product in Catalog['Products']:
    status = "In_stock" if product['stock'] else "Out of stock"
    print(product['product_id'], product['product_name'], status)