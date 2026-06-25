# Remarcable_Djanjo_Assessment
Submission for Remarcable Assessment

### Superuser credentials:
user<br>
test@test.com<br>
1234356

## Setup Instructions

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
    - Windows: `venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Apply migrations: `python manage.py migrate`
6. Create a superuser (if needed) or use credentials found above: `python manage.py createsuperuser`

## Running the Project

- Start the development server: `python manage.py runserver`
- Access the application at `http://127.0.0.1:8000/`
- Access the admin panel at `http://127.0.0.1:8000/admin/`

## Notes

- Ensure Python 3.8+ is installed