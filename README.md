# Flask E-Commerce API

This project is a simple RESTful API built with Flask. It represents an e-commerce backend focused on managing products. Some classes and features are still under development.

## Features

- Basic Product model using SQLAlchemy
- RESTful endpoints for product management (to be implemented/expanded)
- OpenAPI/Swagger specification available in `swagger.yaml`

## Repository structure

# Flask E-Commerce API 🛒

This project is a simple RESTful API built with Flask. It represents an e-commerce backend focused on managing products. Some classes and features are still under development. 🚧

## Features ✨

- Basic Product model using SQLAlchemy 🗂️
- RESTful endpoints for product management (to be implemented/expanded) 🔁
- OpenAPI/Swagger specification available in `swagger.yaml` 📄

## Repository structure 📁

```
app.py
requirements.txt
swagger.yaml
controller/
        __init__.py
model/
        __init__.py
        product.py
```

The package follows simple conventions:
- Modules (filenames) are lowercase (e.g. `product.py`). 🧩
- Classes use CapWords (e.g. `Product`). 🏷️

## Quick setup ⚙️

> These instructions assume you have Python 3.8+ and pip installed.

1. Create and activate a virtual environment

PowerShell (Windows):

```powershell
python -m venv .venv
# Activate the venv in PowerShell
.\.venv\Scripts\Activate.ps1
```

bash / macOS / WSL / Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

PowerShell / bash:

```powershell
pip install -r requirements.txt
```

3. Initialize the database

If you use SQLite or another local DB, check `app.py` for the configured URI and create/migrate the database as needed. For a quick SQLite file, often nothing else is required beyond running the app.

4. Run the application

PowerShell / bash:

```powershell
python app.py
```

The API should be available at http://127.0.0.1:5000/ by default. 🚀

## API documentation 📚

An OpenAPI/Swagger file is provided as `swagger.yaml`. You can:

- Open it with the Swagger Editor: https://editor.swagger.io/
- Serve it with a local Swagger UI instance or integrate it into the Flask app.

## Example requests 🧪

GET all products (PowerShell):

```powershell
Invoke-RestMethod -Method Get -Uri http://127.0.0.1:5000/products
```

GET all products (curl / bash):

```bash
curl http://127.0.0.1:5000/products
```

Create a product (PowerShell):

```powershell
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:5000/products -ContentType 'application/json' -Body (@{name='Example';price=9.99;description='Sample product'} | ConvertTo-Json)
```

Create a product (curl / bash):

```bash
curl -X POST http://127.0.0.1:5000/products \
    -H "Content-Type: application/json" \
    -d '{"name":"Example","price":9.99,"description":"Sample product"}'
```

## Next steps / TODO 📝

- Implement controllers and routes for products (create, read, update, delete) 🔧
- Add more models (users, orders, categories) and relationships 🔗
- Add authentication and authorization 🔐
- Add unit and integration tests ✅
- Add deployment documentation (Docker, cloud provider) ☁️

## Contributing 🤝

Contributions are welcome. Please open issues or pull requests describing the change.

## License 📜

Add a license file to the project if you want to make the licensing terms explicit.
