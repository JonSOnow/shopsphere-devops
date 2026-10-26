
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    session,
    flash,
    request,
)
from sqlalchemy import select

from app.models import db, Product, Order, OrderItem

main = Blueprint("main", __name__)


def get_product(product_id):
    return db.session.get(Product, product_id)


@main.app_context_processor
def inject_cart_count():
    cart = session.get("cart", {})
    return {"cart_count": sum(cart.values())}


@main.route("/")
def home():
    products = Product.query.order_by(Product.id).all()
    return render_template("index.html", products=products)


@main.route("/products")
def product_catalog():
    products = Product.query.order_by(Product.id).all()
    return {
        "count": len(products),
        "products": [product.to_dict() for product in products],
    }, 200


@main.route("/cart")
def view_cart():
    cart = session.get("cart", {})
    items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_product(int(product_id))

        if product and quantity > 0:
            subtotal = product.price * quantity
            items.append({
                **product.to_dict(),
                "quantity": quantity,
                "subtotal": subtotal,
            })
            total += subtotal

    return render_template("cart.html", items=items, total=total)


@main.route("/cart/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    product = get_product(product_id)

    if not product:
        flash("Product not found.", "error")
        return redirect(url_for("main.home"))

    cart = session.get("cart", {})
    key = str(product_id)
    current_quantity = cart.get(key, 0)

    if current_quantity >= product.stock:
        flash("You have reached the available stock limit.", "error")
    else:
        cart[key] = current_quantity + 1
        session["cart"] = cart
        session.modified = True
        flash(f"{product.name} added to your cart!", "success")

    return redirect(url_for("main.home"))


@main.route("/cart/remove/<int:product_id>", methods=["POST"])
def remove_from_cart(product_id):
    cart = session.get("cart", {})
    cart.pop(str(product_id), None)
    session["cart"] = cart
    session.modified = True

    flash("Item removed from your cart.", "success")
    return redirect(url_for("main.view_cart"))


@main.route("/cart/clear", methods=["POST"])
def clear_cart():
    session.pop("cart", None)
    flash("Your cart has been cleared.", "success")
    return redirect(url_for("main.view_cart"))


@main.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart = session.get("cart", {})

    if not cart:
        flash("Your cart is empty.", "error")
        return redirect(url_for("main.view_cart"))

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_product(int(product_id))

        if product and quantity > 0:
            subtotal = product.price * quantity
            cart_items.append({
                "product": product,
                "quantity": quantity,
                "subtotal": subtotal,
            })
            total += subtotal

    if not cart_items:
        session.pop("cart", None)
        flash("Your cart has no valid products. Please shop again.", "error")
        return redirect(url_for("main.home"))

    if request.method == "POST":
        customer_name = request.form.get("customer_name", "").strip()
        address = request.form.get("address", "").strip()

        if not customer_name or not address:
            flash("Please enter your name and delivery address.", "error")
            return render_template(
                "checkout.html",
                items=cart_items,
                total=total,
            )

        # Re-check stock at checkout; do not trust the session alone.
        for item in cart_items:
            if item["quantity"] > item["product"].stock:
                flash(
                    f"Not enough stock for {item['product'].name}. "
                    "Please update your cart.",
                    "error",
                )
                return redirect(url_for("main.view_cart"))

        try:
            order = Order(
                customer_name=customer_name,
                address=address,
                total_amount=total,
                status="Confirmed",
            )
            db.session.add(order)
            db.session.flush()

            for item in cart_items:
                product = item["product"]
                quantity = item["quantity"]

                db.session.add(
                    OrderItem(
                        order_id=order.id,
                        product_id=product.id,
                        product_name=product.name,
                        unit_price=product.price,
                        quantity=quantity,
                        subtotal=item["subtotal"],
                    )
                )
                product.stock -= quantity

            db.session.commit()
            order_id = order.id

        except Exception:
            db.session.rollback()
            flash("We couldn't place your order. Please try again.", "error")
            return redirect(url_for("main.checkout"))

        session.pop("cart", None)
        return redirect(url_for("main.order_confirmation", order_id=order_id))

    return render_template("checkout.html", items=cart_items, total=total)


@main.route("/orders")
def order_history():
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template("orders.html", orders=orders)


@main.route("/orders/<int:order_id>")
def order_confirmation(order_id):
    order = db.session.get(Order, order_id)

    if order is None:
        flash("Order not found.", "error")
        return redirect(url_for("main.order_history"))

    return render_template("order_confirmation.html", order=order)


@main.route("/health")
def health():
    return {"status": "healthy"}, 200
