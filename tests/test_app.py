
import pytest

from app import create_app
from app.models import db, Product, Order


@pytest.fixture()
def app():
    app = create_app()

    # Use an isolated in-memory database for every test run.
    app.config.update(
        TESTING=True,
        SECRET_KEY="test-secret-key",
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
    )

    with app.app_context():
        db.create_all()

        db.session.add_all([
            Product(
                name="Wireless Headphones",
                price=1499,
                description="Clear sound and comfortable listening.",
                emoji="🎧",
                category="Electronics",
                stock=12,
            ),
            Product(
                name="Smartwatch",
                price=2499,
                description="Track your activity.",
                emoji="⌚",
                category="Electronics",
                stock=8,
            ),
            Product(
                name="Travel Backpack",
                price=999,
                description="A practical travel backpack.",
                emoji="🎒",
                category="Travel",
                stock=20,
            ),
        ])
        db.session.commit()

    yield app

    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


def test_homepage_loads(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Wireless Headphones" in response.data


def test_products_api_returns_three_products(client):
    response = client.get("/products")

    assert response.status_code == 200

    data = response.get_json()
    assert data["count"] == 3
    assert len(data["products"]) == 3


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_add_product_to_cart(client):
    response = client.post("/cart/add/1", follow_redirects=True)

    assert response.status_code == 200
    assert b"Wireless Headphones added to your cart!" in response.data

    with client.session_transaction() as session:
        assert session["cart"]["1"] == 1


def test_checkout_saves_order_and_updates_stock(client, app):
    # Add one pair of headphones to the session cart.
    client.post("/cart/add/1")

    # Submit a demo checkout.
    response = client.post(
        "/checkout",
        data={
            "customer_name": "Test Customer",
            "address": "123 Test Street",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Order placed successfully!" in response.data

    with app.app_context():
        order = db.session.execute(
            db.select(Order)
        ).scalar_one()

        assert order.customer_name == "Test Customer"
        assert order.total_amount == 1499
        assert len(order.items) == 1
        assert order.items[0].quantity == 1
        assert order.items[0].unit_price == 1499

        product = db.session.get(Product, 1)
        assert product.stock == 11

    # The cart should be cleared after a successful order.
    with client.session_transaction() as session:
        assert "cart" not in session


def test_order_history_loads(client):
    response = client.get("/orders")

    assert response.status_code == 200
    assert b"No orders yet" in response.data
