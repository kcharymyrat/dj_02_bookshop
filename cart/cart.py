from decimal import Decimal


class Cart:
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = request.session["cart"] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, product, product_qty) -> None:
        product_qty = int(product_qty)
        product_id = int(product.id)
        if product_id in self.cart.keys():
            self.cart[product_id]["qty"] = product_qty
        else:
            self.cart[product_id] = {"qty": product_qty, "price": str(product.price)}
        self.save()

    def update(self, product_id, product_qty) -> None:
        pass

    def delete(self, product_id) -> None:
        pass

    def product_sum(self) -> int:
        return sum(product["qty"] for product in self.cart.values())

    def total_price(self):
        pass

    def __iter__(self) -> None:
        pass

    def __str__(self) -> str:
        return f"{self.cart}"
