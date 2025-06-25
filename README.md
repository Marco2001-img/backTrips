# LOPEZGAR API

Is a backend project developed using the Django REST Framework and integrated with a PostgreSQL database. The application is configured via a .yml file and deployed on AWS Elastic Beanstalk, enabling a scalable and reliable cloud infrastructure.

Project Overview
This API system is designed for the comprehensive management of clients and travel services, while also offering an intercity parcel delivery feature. The platform streamlines both user administration and the tracking of travel and delivery operations, enhancing the transportation of both people and goods through a secure and efficient solution.

Key Features
Client Management
Register, update, and retrieve user data with full CRUD functionality.

Travel Administration
Create and assign routes, manage schedules, and track ongoing journeys.

Parcel Delivery Service
Send and receive packages between cities with traceability and a focus on delivery security.

Authentication and Authorization (Token-Based)
Secure access to API endpoints using JWT (JSON Web Tokens). This ensures safe authentication and role-based permissions.

Cloud Deployment
Ready-to-deploy configuration using a .yml file for AWS Elastic Beanstalk, supporting production-grade infrastructure.

Tech Stack
Python

Django REST Framework

PostgreSQL

AWS Elastic Beanstalk

Docker (optional, if used for containerization)

YAML

Objective
To provide a modern, scalable, and secure solution for the mobility of people and delivery of goods, especially in environments where logistical efficiency, traceability, and ease of administration are essential.

Local Installation (Optional)
bash
Copiar
Editar
# Clone the repository
git clone https://github.com/your-username/lopezgar-api.git
cd lopezgar-api

# Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install project dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run the development server
python manage.py runserver
Deployment
The project is configured for automated deployment on AWS Elastic Beanstalk using a custom .yml configuration file. This file defines all necessary environments, dependencies, and settings to ensure smooth and scalable production deployment.