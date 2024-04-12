from flask import Flask, request
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"

@app.get("/test")
def test():
    return "this is a test page"

@app.get("/about")
def test_about():
    me = {"name": "Jay"}
    return json.dumps(me)

@app.get("/api/versions")
def version():
    version = {"version":"dog", "name":"lukas", "description":"the real newest version"}
    return json.dumps(version)

@app.get("/admin")
def admin():
    return "hello from the admin"

products = []
@app.get("/api/products")
def get_products():
    return json.dumps(products)

@app.post("/api/products")
def save_products():
    prod = request.get_json()
    print (prod)
    #mock save
    products.append(prod)
    return json.dumps(prod)

@app.put("/api/products/<int:index>")
def update_products(index):
    updated_product = request.get_json()
    if 0<= index < len(products):
        products[index] = updated_product
        return json.dumps(updated_product)
    else:
        return "That index does not exist"

@app.delete("/api/products/<int:index>")
def delete_products(index):
    deleted_product = request.get_json()
    if 0<= index < len(products):
        deleted_product = products.pop(index)
        return json.dumps(deleted_product)
    else:
        return "That index does not exist"

@app.patch("/api/products/<int:index>")
def patch_products(index):
    updated_field = request.get_json()
    if 0<= index < len(products):
        products(index).update(updated_field)
        return json.dumps(updated_field)
    else:
        return "That index does not exist"


# use the same logic but remember that you need to use list.pop
# create the logic for the delete API
app.run(debug=True)


