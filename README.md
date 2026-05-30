# 🍦 The Ice Cream Shop

A full-stack multi-role e-commerce platform built with Django that enables customers to browse and purchase ice cream products while allowing vendors to manage products, inventory, and orders through dedicated dashboards.

---

## 🚀 Features

### Customer Features
- Customer Registration & Login
- Browse Products
- Product Details Page
- Add to Cart
- Cart Management
- Checkout System
- Order Placement
- Order History

### Vendor Features
- Vendor Registration & Login
- Vendor Dashboard
- Add Products
- Edit Products
- Delete Products
- Inventory Management
- Order Tracking

### Admin Features
- Django Admin Panel
- User Management
- Product Management
- Order Management

---

## 🏗️ Project Architecture

```text
The-Ice-Cream-Shop
│
├── accounts/
│   ├── Authentication
│   ├── Customer Dashboard
│   └── Vendor Dashboard
│
├── products/
│   ├── Product Catalog
│   ├── Product Management
│   └── Inventory
│
├── orders/
│   ├── Cart System
│   ├── Checkout
│   └── Order Processing
│
└── icecreamshop/
    └── Project Settings
```

---

## 🛠️ Tech Stack

### Backend
- Python
- Django
- Django ORM
- SQLite

### Frontend
- HTML5
- CSS3
- Bootstrap

### Authentication
- Django Authentication System
- OAuth Ready

### Deployment
- Render

### Version Control
- Git
- GitHub

---

## 📊 Database Design

```text
User
│
├── Customer
│
└── Vendor
      │
      └── Product
               │
               └── Cart
                      │
                      └── Order
```

---

## 🔄 Order Workflow

```text
Browse Products
       ↓
Add To Cart
       ↓
Checkout
       ↓
Create Order
       ↓
Update Inventory
       ↓
Order Confirmation
```

### Reliability Features

- Atomic database transactions
- Real-time inventory updates
- Stock validation during checkout
- Concurrent order handling
- Data consistency protection

---

## 📈 Key Highlights

- Multi-role authentication system
- Vendor and customer workflow separation
- Modular Django architecture
- Scalable relational database design
- End-to-end order processing pipeline
- Inventory synchronization
- Production deployment on Render

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/sarthakgit123/The-Ice-Cream-Shop.git
cd The-Ice-Cream-Shop
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---


## 🎯 Resume Project Description

**Ice Cream E-Commerce Management System**

- Built and deployed a scalable multi-role e-commerce platform using Django and Render supporting vendor/customer workflows and managing 100+ products.
- Designed normalized relational database models and modular backend architecture for Users, Vendors, Products, Carts, and Orders.
- Implemented complete order lifecycle (Cart → Checkout → Order) with inventory synchronization and transaction-safe order processing.
- Developed role-based authentication, vendor dashboards, and product management features.
- Technologies: Python, Django, SQLite, HTML, CSS, Bootstrap, Git, GitHub, Render.

---

## 👨‍💻 Author

**Sarthak Kumar Seth**

GitHub: https://github.com/sarthakgit123

---

--
