# 🌐 Django REST Blog API

A secure blog API built with Django REST Framework.

## ✅ Features
- JWT Authentication (`/api/token/`)
- CRUD for blog posts
- Only owners can edit/delete
- Tested with `curl`
- Uses `select_related` to avoid N+1

## 🔧 Tech Stack
- Python, Django, DRF
- djangorestframework-simplejwt
- SQLite (can upgrade to PostgreSQL)
- `curl` for testing

## 🚀 How to Run

1. Clone:
   ```bash
   git clone https://github.com/YOUR-USERNAME/drf-blog-api.git
   cd drf-blog-api   