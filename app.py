from flask import Flask, render_template

# Initialize the Flask application
# IMPORTANT: Vercel requires this variable to be named exactly 'app'
app = Flask(__name__)

# Dummy data for your premium laptops
# We are using high-res Unsplash images for that "Tech-Minimalist" feel
laptop_data = [
    {
        "id": 1,
        "brand": "Apple",
        "model": "MacBook Pro 16\"",
        "cpu": "M4 Max",
        "ram": "64GB Unified",
        "price": "$3,499",
        "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 2,
        "brand": "Dell",
        "model": "XPS 15",
        "cpu": "Intel Core Ultra 9",
        "ram": "32GB DDR5",
        "price": "$2,499",
        "image_url": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 3,
        "brand": "Razer",
        "model": "Blade 16 Gaming",
        "cpu": "Intel Core i9-14900HX",
        "ram": "64GB DDR5",
        "price": "$3,799",
        "image_url": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=800&q=80"
    }
]

# Define the main route for your homepage
@app.route('/')
def home():
    # This sends the 'laptop_data' list to your index.html file
    # Inside index.html, the {% for laptop in laptops %} loop will read this data
    return render_template('index.html', laptops=laptop_data)

# This block allows you to test the app locally before pushing to GitHub
if __name__ == '__main__':
    # Runs on http://127.0.0.1:5000/
    app.run(debug=True, port=5000)
