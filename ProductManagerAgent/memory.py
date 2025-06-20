

product_catalog = {}

def add_product(name, price):
    product_catalog[name.lower()] = {"name": name, "price": price}
    return f"Added product: {name} at {price}"

def update_product(name, price):
    if name.lower() in product_catalog:
        product_catalog[name.lower()]["price"] = price
        return f"Updated price of {name} to {price}" 
    return f"Product {name} not found"

def delete_product(name):
    if name.lower() in product_catalog:
        del product_catalog[name.lower()]
        return f"Deleted product: {name}"
    return f"Product {name} not found."

def list_products():
    if not product_catalog:
        return "No products found"
    return "\n".join([f"{p['name']} : {p['price']}" for p in product_catalog.values()])