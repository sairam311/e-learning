# E-Learning Platform

This project is a simple e-learning platform built using Django for the backend and HTML, CSS, and JavaScript for the frontend. The platform features user signup, login, profile management, and referral code functionality. The backend is powered by Django and Django REST Framework (DRF) to expose RESTful APIs for communication between the frontend and backend.

Features:
- User Authentication: Sign up and log in functionality.
- Referral Code System: Referral code-based registration.
- Profile Management: Users can view and edit their profile.
- RESTful API: Backend exposed via Django REST Framework for seamless communication.

Prerequisites:
Before running the project, ensure you have the following installed:
- Python (version 3.6 or above)
- Django (version 3.0 or above)
- Django REST Framework (DRF)
- Node.js (for frontend dependencies)
- Git (for version control)

Installation & Setup:

1. Clone the Repository
Clone the repository to your local machine:

git clone https://github.com/sairam311/e-learning.git
cd e-learning

2. Setting Up Backend
Install Backend Dependencies
Navigate to the backend folder and install the required Python dependencies using pip:

cd backend
pip install -r requirements.txt

Setup the Database
Run the following commands to apply migrations and set up the database:

python manage.py makemigrations
python manage.py migrate

Create a Superuser
To access the Django Admin, create a superuser:

python manage.py createsuperuser

Start the Django Development Server
Run the Django development server:

python manage.py runserver

The backend will be running on http://127.0.0.1:8000/.

3. Setting Up Frontend

Run the frontend 

Usage:
1. Signup: Go to the signup page, provide your details and referral code (if any).
2. Login: After successfully signing up, you can log in using your credentials.
3. Profile: Once logged in, you can view your profile details like email, name, mobile number, and referral code.

Technologies Used:
- Backend: Django, Django REST Framework (DRF)
- Frontend: HTML, CSS, JavaScript (Bootstrap)
- Database: SQLite (default)

Troubleshooting:
- If you encounter a CORS issue when trying to access the backend from the frontend, ensure that CORS is properly configured in your Django settings (django-cors-headers library).
- If you face issues with the frontend not loading correctly, ensure you have installed all the required Node.js dependencies by running npm install.
