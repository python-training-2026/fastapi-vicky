from fastapi import FastAPI, HTTPException
from typing import List, Optional

app = FastAPI()

# In-memory database
products = []
students = []

# -------------------------------
# 1. PRODUCT API
# -------------------------------

# POST → Add product
@app.post("/products")
def add_product(product: dict):
    # Prevent duplicate ID
    for p in products:
        if p["id"] == product["id"]:
            raise HTTPException(status_code=400, detail="Product ID already exists")
    
    products.append(product)
    return {"message": "Product added", "product": product}


# GET → All products
@app.get("/products")
def get_products():
    return products


# GET → Product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")


# -------------------------------
# 3. DELETE by ID
# -------------------------------

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            products.remove(p)
            return {"message": "Product deleted"}
    
    raise HTTPException(status_code=404, detail="Product not found")


# -------------------------------
# 4. PUT (Full Update)
# -------------------------------

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: dict):
    for i, p in enumerate(products):
        if p["id"] == product_id:
            products[i] = updated_product
            return {"message": "Product updated", "product": updated_product}
    
    raise HTTPException(status_code=404, detail="Product not found")


# -------------------------------
# 5. PATCH (Partial Update)
# -------------------------------

@app.patch("/products/{product_id}")
def patch_product(product_id: int, updates: dict):
    for p in products:
        if p["id"] == product_id:
            p.update(updates)
            return {"message": "Product partially updated", "product": p}
    
    raise HTTPException(status_code=404, detail="Product not found")


# -------------------------------
# 2. STUDENT API
# -------------------------------

# POST → Add student
@app.post("/students")
def add_student(student: dict):
    students.append(student)
    return {"message": "Student added", "student": student}


# GET → All students
@app.get("/students")
def get_students():
    return students


# GET → Students with marks > value
@app.get("/students/filter/")
def get_students_by_marks(min_marks: int):
    result = [s for s in students if s["marks"] > min_marks]
    return result