# Remarcable Django Assessment
Submission for Remarcable Assessment — a Django-based product catalogue with search and filtering.

## Project Overview

This project demonstrates Django proficiency through a product catalogue application. It includes:

- **Models** for `Product`, `Category`, and `Tag` with appropriate relationships (ForeignKey, ManyToManyField)
- **Django Admin** configuration to populate the database with sample data
- **Search & Filter** page allowing users to filter products by description, category, and tags

## Superuser Credentials

| Field    | Value          |
|----------|----------------|
| Username | user           |
| Email    | test@test.com  |
| Password | 1234356        |

## Setup Instructions

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Apply migrations: `python manage.py migrate`
4. Create a superuser (or use credentials above): `python manage.py createsuperuser`

## Running the Project

- Start the development server: `python manage.py runserver`
- Access the application at `http://127.0.0.1:8000/`
- Access the admin panel at `http://127.0.0.1:8000/admin/`

## Populating Sample Data

Use the Django Admin panel to add sample `Categories`, `Tags`, and `Products`. The admin is pre-configured to support all three models.

## Notes

- Requires **Python 3.8+**
- Requires **Django 4.x+**
