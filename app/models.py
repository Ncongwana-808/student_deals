"""Database models for Student Marketplace"""

class User:
    """User model"""
    def __init__(self, user_id, email, name, avatar_url=None):
        self.user_id = user_id
        self.email = email
        self.name = name
        self.avatar_url = avatar_url


class Product:
    """Product model"""
    def __init__(self, product_id, title, description, price, seller_id, category, image_url=None):
        self.product_id = product_id
        self.title = title
        self.description = description
        self.price = price
        self.seller_id = seller_id
        self.category = category
        self.image_url = image_url


class Transaction:
    """Transaction model for purchases"""
    def __init__(self, transaction_id, buyer_id, seller_id, product_id, amount, status='pending'):
        self.transaction_id = transaction_id
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.product_id = product_id
        self.amount = amount
        self.status = status  # pending, completed, cancelled
