# 🍽️ Recipe App API

A RESTful API for managing personal recipes, ingredients, tags, and image uploads. Built with Django, Django REST Framework, and PostgreSQL — following Test-Driven Development (TDD) best practices.

## 🚀 Features

- **User authentication** (Token-based)
- **Create, read, update, and delete recipes**
- **Manage ingredients and tags**
- **Upload and manage recipe images**
- **Private endpoints for authenticated users**
- **Test-Driven Development (TDD) approach**
- **Dockerized environment for easy setup**

## 🧰 Tech Stack

- **Backend**: Python, Django, Django REST Framework  
- **Database**: PostgreSQL  
- **Authentication**: Token Authentication  
- **Testing**: Django TestCase, TDD  
- **Containerization**: Docker, Docker Compose  

---

## 📦 Getting Started

### Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/joaovicsa/recipe-app-api2.git
cd recipe-app-api2
```
Build and run the containers

```
  docker-compose up --build
``` 
Create the database and run migrations
```
    docker-compose run app sh -c "python manage.py migrate"
```
Create a superuser (optional, for admin access)
```
    docker-compose run app sh -c "python manage.py createsuperuser"
```
Access the API

    API Root: http://localhost:8000/api/

    Admin Panel: http://localhost:8000/admin/

📁 Project Structure

```
recipe-app-api2/
├── app/
│   ├── core/           # Custom user model and core utilities
│   ├── recipe/         # Recipe, Tag, Ingredient models and APIs
│   ├── user/           # Authentication and user management
├── Dockerfile
├── docker-compose.yml
└── manage.py
```

🔐 Authentication

The API uses Token Authentication.

    Register a new user
    POST /api/user/create/

    Generate a token
    POST /api/user/token/

    Authenticate requests
    Add the token to the Authorization header:

    Authorization: Token your_token_here

🖼️ Image Uploads

You can upload images for your recipes via:

    POST /api/recipe/recipes/{id}/upload-image/

Ensure your request includes a valid image file with multipart/form-data.

📌 TODO

API documentation with Swagger or Postman

Deployment configuration

Rate limiting and throttling

Advanced search and filtering

FrontEnd

🤝 Contributing

Contributions are welcome! Feel free to fork this project and submit a pull request.

📄 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Developed by @joaovicsa by following the instructions of @LondonAppDeveloper in the course https://www.udemy.com/course/django-python-advanced/ 
