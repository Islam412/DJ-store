# utils.py (create a new file or add this function to an existing one)
import json

def serialize_cart_items(cart_items):
    serialized_items = []
    for cart_item in cart_items:
        serialized_item = {
            'product_name': cart_item.product.Name,
            'quantity': cart_item.quantity,
            'price': cart_item.Product.Price,
            # Add more fields as needed
        }
        serialized_items.append(serialized_item)
    return json.dumps(serialized_items)
