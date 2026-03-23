"""Helper functions for Student Marketplace"""

def simulate_escrow_transfer(buyer_id, seller_id, amount):
    """
    Simulate escrow transaction
    In a real application, this would interact with a payment processor
    """
    # TODO: Implement escrow logic
    return {
        'status': 'success',
        'transaction_id': 'txn_' + str(hash((buyer_id, seller_id, amount)))[:10],
        'amount': amount
    }


def validate_product_data(data):
    """Validate product creation data"""
    required_fields = ['title', 'description', 'price', 'category']
    return all(field in data for field in required_fields)


def validate_user_data(data):
    """Validate user data"""
    required_fields = ['email', 'name']
    return all(field in data for field in required_fields)
