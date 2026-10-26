
from app.models import db, Product


INITIAL_PRODUCTS = [
    {
        "name": "Wireless Headphones",
        "price": 1499,
        "description": "Enjoy clear sound and comfortable listening.",
        "emoji": "🎧",
        "category": "Electronics",
        "stock": 12,
    },
    {
        "name": "Smartwatch",
        "price": 2499,
        "description": "Track your activity and stay connected.",
        "emoji": "⌚",
        "category": "Electronics",
        "stock": 8,
    },
    {
        "name": "Travel Backpack",
        "price": 999,
        "description": "A practical backpack for everyday adventures.",
        "emoji": "🎒",
        "category": "Travel",
        "stock": 20,
    },
]


def initialize_database():
    db.create_all()

    for item in INITIAL_PRODUCTS:
        existing = Product.query.filter_by(name=item["name"]).first()
        if existing is None:
            db.session.add(Product(**item))

    db.session.commit()
