from flask import Flask, render_template

app = Flask(__name__)

laptops = [
    {
        "brand": "Apple",
        "model": "MacBook Pro 16\" M3 Max",
        "cpu": "Apple M3 Max",
        "ram": "48GB Unified Memory",
        "price": "$3,499",
        "image_url": "https://images.unsplash.com/photo-1517336714739-489689fd1ca8?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "brand": "Dell",
        "model": "XPS 15 OLED",
        "cpu": "Intel Core i9-13900H",
        "ram": "32GB DDR5",
        "price": "$2,699",
        "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "brand": "Razer",
        "model": "Blade 16",
        "cpu": "Intel Core i9-14900HX",
        "ram": "32GB DDR5",
        "price": "$3,199",
        "image_url": "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?auto=format&fit=crop&w=1200&q=80",
    },
]


@app.route("/")
def home():
    return render_template("index.html", laptops=laptops)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
