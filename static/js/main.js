// Student Marketplace Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('Student Marketplace loaded');
    
    // Fetch and display products
    fetchProducts();
});

/**
 * Fetch products from API
 */
function fetchProducts() {
    fetch('/api/products')
        .then(response => response.json())
        .then(data => {
            console.log('Products:', data);
            displayProducts(data.products || []);
        })
        .catch(error => console.error('Error fetching products:', error));
}

/**
 * Display products in grid
 */
function displayProducts(products) {
    const productsGrid = document.querySelector('.products-grid');
    if (!productsGrid) return;
    
    productsGrid.innerHTML = '';
    
    products.forEach(product => {
        const card = document.createElement('div');
        card.className = 'product-card';
        card.innerHTML = `
            <img src="${product.image_url || 'placeholder.jpg'}" alt="${product.title}" class="product-image">
            <div class="product-info">
                <h3 class="product-title">${product.title}</h3>
                <p>${product.description}</p>
                <p class="product-price">$${product.price}</p>
                <button class="btn btn-primary" onclick="viewProduct('${product.product_id}')">View Details</button>
            </div>
        `;
        productsGrid.appendChild(card);
    });
}

/**
 * View product details
 */
function viewProduct(productId) {
    window.location.href = `/static/product.html?id=${productId}`;
}

/**
 * Create new product listing
 */
function createProduct(formData) {
    fetch('/api/products', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            console.log('Product created:', data);
            alert('Product created successfully!');
            fetchProducts();
        })
        .catch(error => console.error('Error creating product:', error));
}
