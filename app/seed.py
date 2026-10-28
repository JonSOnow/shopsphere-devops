
from app.models import db, Product


PRODUCTS = [
    # Electronics
    {
        "name": "Wireless Headphones",
        "description": "Enjoy clear sound and comfortable listening.",
        "price": 1499,
        "category": "Electronics",
        "emoji": "🎧",
        "stock": 25,
    },
    {
        "name": "Smartwatch",
        "description": "Track your activity and stay connected.",
        "price": 2499,
        "category": "Electronics",
        "emoji": "⌚",
        "stock": 20,
    },
    {
        "name": "Bluetooth Speaker",
        "description": "Portable speaker with powerful sound.",
        "price": 1299,
        "category": "Electronics",
        "emoji": "🔊",
        "stock": 30,
    },
    {
        "name": "Wireless Mouse",
        "description": "Comfortable wireless mouse for work and study.",
        "price": 699,
        "category": "Electronics",
        "emoji": "🖱️",
        "stock": 35,
    },
    {
        "name": "USB-C Charger",
        "description": "Compact charger for compatible devices.",
        "price": 899,
        "category": "Electronics",
        "emoji": "🔌",
        "stock": 28,
    },
    {
        "name": "Mechanical Gaming Keyboard",
        "description": "RGB backlit keyboard for gaming and productivity.",
        "price": 1899,
        "category": "Electronics",
        "emoji": "⌨️",
        "stock": 25,
    },
    {
        "name": "Power Bank 20000mAh",
        "description": "High-capacity portable charging for your devices.",
        "price": 1599,
        "category": "Electronics",
        "emoji": "🔋",
        "stock": 30,
    },
    {
        "name": "HD Webcam",
        "description": "HD webcam for meetings, classes, and streaming.",
        "price": 1199,
        "category": "Electronics",
        "emoji": "📷",
        "stock": 18,
    },
    {
        "name": "Wireless Earbuds",
        "description": "Compact wireless earbuds for everyday listening.",
        "price": 999,
        "category": "Electronics",
        "emoji": "🎧",
        "stock": 35,
    },
    {
        "name": "Laptop Stand",
        "description": "Adjustable stand for a comfortable desk setup.",
        "price": 799,
        "category": "Electronics",
        "emoji": "💻",
        "stock": 22,
    },

    # Travel
    {
        "name": "Travel Backpack",
        "description": "Spacious backpack for trips and daily use.",
        "price": 999,
        "category": "Travel",
        "emoji": "🎒",
        "stock": 20,
    },
    {
        "name": "Travel Neck Pillow",
        "description": "Soft neck pillow for comfortable journeys.",
        "price": 499,
        "category": "Travel",
        "emoji": "🛫",
        "stock": 25,
    },
    {
        "name": "Insulated Water Bottle",
        "description": "Reusable bottle for keeping drinks at temperature.",
        "price": 599,
        "category": "Travel",
        "emoji": "🧴",
        "stock": 32,
    },
    {
        "name": "Cabin Trolley Bag",
        "description": "Lightweight cabin luggage for short trips.",
        "price": 2499,
        "category": "Travel",
        "emoji": "🧳",
        "stock": 15,
    },
    {
        "name": "Travel Organizer Set",
        "description": "Packing cubes to organize clothes and accessories.",
        "price": 499,
        "category": "Travel",
        "emoji": "🧳",
        "stock": 40,
    },
    {
        "name": "Compact Travel Umbrella",
        "description": "Foldable umbrella for travel and daily commutes.",
        "price": 399,
        "category": "Travel",
        "emoji": "☂️",
        "stock": 28,
    },
    {
        "name": "Digital Luggage Scale",
        "description": "Portable scale to check luggage weight before flights.",
        "price": 599,
        "category": "Travel",
        "emoji": "⚖️",
        "stock": 20,
    },

    # Fashion
    {
        "name": "Classic Sneakers",
        "description": "Everyday sneakers with a versatile design.",
        "price": 1799,
        "category": "Fashion",
        "emoji": "👟",
        "stock": 18,
    },
    {
        "name": "Everyday Backpack",
        "description": "Practical backpack for work, college, and outings.",
        "price": 1199,
        "category": "Fashion",
        "emoji": "🎒",
        "stock": 22,
    },
    {
        "name": "Classic Denim Jacket",
        "description": "Versatile denim jacket for casual outfits.",
        "price": 1599,
        "category": "Fashion",
        "emoji": "🧥",
        "stock": 16,
    },
    {
        "name": "Everyday Analog Watch",
        "description": "Minimal analog watch for everyday wear.",
        "price": 1299,
        "category": "Fashion",
        "emoji": "⌚",
        "stock": 24,
    },
    {
        "name": "Canvas Sneakers",
        "description": "Comfortable sneakers for casual everyday use.",
        "price": 899,
        "category": "Fashion",
        "emoji": "👟",
        "stock": 32,
    },
    {
        "name": "Classic Sunglasses",
        "description": "Everyday sunglasses with a timeless design.",
        "price": 699,
        "category": "Fashion",
        "emoji": "🕶️",
        "stock": 27,
    },

    # Home & Living
    {
        "name": "Desk Lamp",
        "description": "Practical lamp for reading and working.",
        "price": 799,
        "category": "Home & Living",
        "emoji": "💡",
        "stock": 24,
    },
    {
        "name": "Coffee Mug",
        "description": "Reusable mug for your favourite hot drinks.",
        "price": 299,
        "category": "Home & Living",
        "emoji": "☕",
        "stock": 40,
    },
    {
        "name": "Electric Kettle",
        "description": "Convenient kettle for tea, coffee, and hot water.",
        "price": 999,
        "category": "Home & Living",
        "emoji": "🫖",
        "stock": 21,
    },
    {
        "name": "Cushion Set",
        "description": "Decorative cushions for sofas and beds.",
        "price": 799,
        "category": "Home & Living",
        "emoji": "🛋️",
        "stock": 19,
    },
    {
        "name": "Storage Organizer",
        "description": "Practical organizer for household items.",
        "price": 499,
        "category": "Home & Living",
        "emoji": "🗃️",
        "stock": 26,
    },
    {
        "name": "LED Desk Light",
        "description": "Energy-efficient light for reading and studying.",
        "price": 699,
        "category": "Home & Living",
        "emoji": "💡",
        "stock": 23,
    },
]


def initialize_database():
    """Create database tables and add any missing seed products."""
    db.create_all()

    existing_names = {
        name for (name,) in db.session.query(Product.name).all()
    }

    added_count = 0

    for product_data in PRODUCTS:
        if product_data["name"] not in existing_names:
            db.session.add(Product(**product_data))
            existing_names.add(product_data["name"])
            added_count += 1

    db.session.commit()
    print(
        f"Database initialization complete. "
        f"Added {added_count} products; "
        f"{len(existing_names)} products currently exist."
    )
