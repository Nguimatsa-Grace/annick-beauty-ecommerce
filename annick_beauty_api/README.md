# Annick Beauty E-commerce API

## 📌 Project Overview
This is a professional-grade REST API built for **Annick Beauty**, an e-commerce platform specializing in luxury human hair wigs, skincare, and hair care products. This API serves as the backend for managing inventory, handling user authentication, and providing searchable product data.

## 🛠 Technologies Used
* **Framework:** Django 5.2 & Django REST Framework (DRF)
* **Database:** SQLite (Django ORM)
* **Authentication:** JWT (SimpleJWT) & Session Authentication
* **Deployment:** PythonAnywhere (Live with HTTPS)
* **Filtering:** Django-filter

## 🚀 Live Links
* **Live API Endpoint:** https://annickbeauty.pythonanywhere.com/api/products/
* **Admin Dashboard:** https://annickbeauty.pythonanywhere.com/admin/

## ✨ Features

### 1. Product Management (CRUD)
Fully functional Create, Read, Update, and Delete operations for products and categories.
* **Attributes:** Name, Description, Price, Category, Stock Quantity, Image URL, and Created Date.
* **Validation:** Strict validation for prices and stock levels.

### 2. Advanced Search & Filtering
The API includes powerful search capabilities to help frontend users find products easily:
* **Search:** Partial match searching by name (e.g., `?search=wig`).
* **Filtering:** Filter products by Category ID or Price range.
* **Pagination:** Results are paginated (5 items per page) to optimize performance.

### 3. Security & Authentication
* **Permissions:** Implemented `IsAuthenticatedOrReadOnly`. The public can view products, but only authenticated staff (Admins) can modify data.
* **JWT Support:** Secure token-based authentication ready for mobile app integration.

## 📁 API Endpoints

* **GET /api/products/**
  * **Description:** List all products in the database.
  * **Feature:** Includes pagination (5 items per page).

* **GET /api/products/{id}/**
  * **Description:** Retrieve full details for a specific product using its ID number.

* **POST /api/products/**
  * **Description:** Create a new product.
  * **Access:** Restricted to Admin users only (requires authentication).

* **PUT /api/products/{id}/**
  * **Description:** Update or edit all fields of an existing product.
  * **Access:** Restricted to Admin users only.

* **DELETE /api/products/{id}/**
  * **Description:** Permanently remove a product from the database.
  * **Access:** Restricted to Admin users only.

## 🧪 How to Test Search & Filters
You can test the functional requirements by appending these parameters to the base URL:
* **Search by Name:** `https://annickbeauty.pythonanywhere.com/api/products/?search=Water`
* **Filter by Category:** `https://annickbeauty.pythonanywhere.com/api/products/?category=1`
* **Ordering by Price:** `https://annickbeauty.pythonanywhere.com/api/products/?ordering=-price`