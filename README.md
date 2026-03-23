# Student Marketplace

A peer-to-peer marketplace platform designed specifically for students to buy and sell textbooks, notes, and study materials.

## Features

- 📚 Browse and list products
- 💳 Secure transactions with escrow simulation
- 👤 User profiles and ratings
- 🔍 Search and filter products
- 💬 Direct messaging between buyers and sellers
- ⭐ Product reviews and seller ratings

## Project Structure

```
student-marketplace/
│
├── app/                        # Flask backend
│   ├── __init__.py             # Initialize Flask app
│   ├── routes.py               # API endpoints (products, users, transactions)
│   ├── models.py               # Database models
│   ├── utils.py                # Helper functions (like escrow simulation)
│   └── config.py               # Config for Supabase keys & Flask
│
├── static/                     # Frontend static files
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
│
├── templates/                  # HTML pages
│   ├── index.html              # Homepage
│   ├── login.html
│   ├── dashboard.html          # Marketplace dashboard
│   └── product.html
│
├── requirements.txt            # Python dependencies
├── run.py                      # Run Flask server
└── README.md                   # This file
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd student-marketplace
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   Create a `.env` file in the root directory with:
   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   SUPABASE_JWT_SECRET=your_jwt_secret
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

The application will be available at `http://localhost:5000`

## API Endpoints

### Products
- `GET /api/products` - Get all products
- `GET /api/products/<id>` - Get specific product
- `POST /api/products` - Create new product

### Users
- `GET /api/users/<id>` - Get user profile

### Transactions
- `POST /api/transactions` - Create transaction
- `GET /api/transactions/<id>` - Get transaction status

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: Supabase (PostgreSQL)
- **Authentication**: Supabase Auth

## Future Enhancements

- [ ] Payment gateway integration
- [ ] Real-time chat functionality
- [ ] Advanced search and filters
- [ ] User reviews and ratings system
- [ ] Mobile app
- [ ] Admin dashboard
- [ ] Email notifications

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Support

For issues or questions, please create an issue in the repository.
