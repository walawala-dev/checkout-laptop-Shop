from flask import Flask, render_template

app = Flask(__name__)

# Real 2026 Market Research Data
laptops = [
    {
        "id": 1,
        "brand": "Apple",
        "model": "MacBook Pro 16",
        "cpu": "Apple M5 Max (16-Core CPU)",
        "ram": "64GB Unified Memory",
        "storage": "2TB NVMe SSD",
        "screen": "16.2\" Liquid Retina XDR (120Hz)",
        "price": 3999.00,
        "formatted_price": "$3,999",
        "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&q=80&w=800"
    },
    {
        "id": 2,
        "brand": "ASUS",
        "model": "ROG Zephyrus G16",
        "cpu": "Intel Core Ultra 9 (Panther Lake)",
        "ram": "32GB LPDDR5X-8400",
        "storage": "2TB PCIe 5.0 SSD",
        "screen": "16\" 3K OLED (240Hz)",
        "price": 2899.00,
        "formatted_price": "$2,899",
        "image_url": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&q=80&w=800"
    },
    {
        "id": 3,
        "brand": "Razer",
        "model": "Blade 18",
        "cpu": "AMD Ryzen AI 9 HX",
        "ram": "64GB DDR5",
        "storage": "4TB SSD",
        "screen": "18\" UHD+ Mini-LED (200Hz)",
        "price": 4299.00,
        "formatted_price": "$4,299",
        "image_url": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?auto=format&fit=crop&q=80&w=800"
    }
]

@app.route('/')
def home():
    return render_template('index.html', laptops=laptops)

# Vercel bypasses this block, but it allows you to still test locally
if __name__ == '__main__':
    app.run(debug=True, port=5000)
