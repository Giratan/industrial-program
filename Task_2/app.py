import logging

from flask import Flask, jsonify, request


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Ноутбук", "price": 899.99, "category": "Электроника"},
    {"id": 2, "name": "Смартфон", "price": 599.00, "category": "Электроника"},
    {"id": 3, "name": "Наушники", "price": 79.50, "category": "Аксессуары"},
    {"id": 4, "name": "Клавиатура", "price": 49.90, "category": "Аксессуары"},
    {"id": 5, "name": "Монитор", "price": 249.00, "category": "Электроника"},
]


@app.get("/api/products")
def get_products():
    app.logger.info("GET /api/products called")

    raw_limit = request.args.get("limit", "10")
    try:
        limit = int(raw_limit)
    except ValueError:
        app.logger.error("Invalid limit parameter: %r", raw_limit)
        return jsonify({"error": "Параметр limit должен быть целым числом от 1 до 100"}), 400

    if not 1 <= limit <= 100:
        app.logger.error("Invalid limit parameter: %r", raw_limit)
        return jsonify({"error": "Параметр limit должен быть целым числом от 1 до 100"}), 400

    products = PRODUCTS[:limit]
    return jsonify({"products": products, "count": len(products)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)