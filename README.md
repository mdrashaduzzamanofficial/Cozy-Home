# House Rental Management System

A Django-based web application for managing rental properties, connecting landlords and tenants.

## Features
- User authentication (Landlord, Tenant, Admin).
- Property listing, search, and booking.
- Tenant applications and lease agreement generation.
- Payment processing (simulated).
- AI-powered property recommendations.
- Landlord-tenant messaging.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <https://github.com/mahafuj-hasan-91/House-Rental-Management-System>
   cd house_rental_system
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Load sample data**:
   ```bash
   python manage.py loaddata properties/fixtures/sample_data.json
   ```

6. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the app**:
   - Open `http://localhost:8000` in your browser.
   - Admin panel: `http://localhost:8000/admin`.

## Credentials
- Landlord: `landlord1` / `password123`
- Tenant: `tenant1` / `password123`

## Deployment
- Use Heroku, AWS, or DigitalOcean with Gunicorn and Nginx.
- Set environment variables for `SECRET_KEY`, database credentials, and `DEBUG=False`.

## Future Enhancements
- Integrate Stripe for real payment processing.
- Add AI chatbots with Django Channels.
- Implement blockchain-based smart contracts.
