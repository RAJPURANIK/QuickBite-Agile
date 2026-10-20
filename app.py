from flask import Flask, render_template_string, request

app = Flask(__name__)

MENU = [
    {"id": 1, "name": "Paneer Tikka Wrap", "category": "Vegetarian", "price": 149},
    {"id": 2, "name": "Classic Veg Burger", "category": "Vegetarian", "price": 129},
    {"id": 3, "name": "Chicken Rice Bowl", "category": "Non-Vegetarian", "price": 219},
    {"id": 4, "name": "Masala Fries", "category": "Sides", "price": 89},
]

PAGE = """
<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>QuickBite | Food Delivery</title>
<style>
*{box-sizing:border-box}body{margin:0;font-family:Arial,sans-serif;background:#f5f7fb;color:#172033}
header{background:#14213d;color:white;padding:24px 7%;display:flex;justify-content:space-between;align-items:center}
header h1{margin:0;color:#ffb703}header span{color:#dce4f5}
main{max-width:1000px;margin:38px auto;padding:0 20px}.hero{background:white;padding:28px;border-radius:18px;box-shadow:0 8px 28px #17203312}
h2{margin-top:0}.search{display:flex;gap:10px;margin:22px 0}.search input{flex:1;padding:12px;border:1px solid #ccd3e0;border-radius:9px}
button{background:#fb8500;color:#14213d;border:0;padding:12px 18px;border-radius:9px;font-weight:bold;cursor:pointer}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px;margin-top:20px}
.item{background:white;padding:20px;border-radius:14px;border:1px solid #e5e9f1}.item h3{margin:8px 0}.tag{font-size:12px;color:#52627a}.price{font-weight:bold;font-size:20px;margin:14px 0;color:#14213d}
footer{text-align:center;color:#68758b;padding:35px}
</style></head><body>
<header><h1>QuickBite</h1><span>Fresh food. Fast delivery.</span></header>
<main><section class="hero"><h2>Find your next favourite meal</h2>
<p>Browse the menu and search by food name or category.</p>
<form class="search" method="get"><input name="q" value="{{ q }}" placeholder="Search food or category..."><button>Search</button></form>
<strong>{{ items|length }} menu item(s) found</strong></section>
<section class="grid">{% for item in items %}<article class="item"><span class="tag">{{ item.category }}</span>
<h3>{{ item.name }}</h3><div class="price">₹{{ item.price }}</div><button type="button" onclick="alert('Demo: {{ item.name }} selected')">Add to cart</button></article>
{% else %}<p>No menu items match your search. Try another keyword.</p>{% endfor %}</section></main>
<footer>QuickBite • Agile Assignment 1 • Demo food delivery application</footer></body></html>
"""

@app.route("/")
def home():
    q = request.args.get("q", "").strip().lower()
    items = [item for item in MENU if q in item["name"].lower() or q in item["category"].lower()]
    return render_template_string(PAGE, items=items, q=request.args.get("q", ""))

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
