Motoverse -- Car Selling Website using Django

Welcome to the Car Selling Website project! This platform allows users to register, login, make inquiries about cars, and search for available vehicles.

## Table of Contents

- [Features](#features)
  - [User Authentication and Registration](#user-authentication-and-registration)
  - [Admin Dashboard](#admin-dashboard)
  - [Rich Text Content Editing](#rich-text-content-editing)
  - [Search Functionality](#search-functionality)
  - [Multiselect Fields](#multiselect-fields)
  - [Debugging and Development Tools](#debugging-and-development-tools)
  - [Image Handling](#image-handling)
  - [OAuth and Social Authentication](#oauth-and-social-authentication)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration](#configuration)
  - [Environment Variables](#environment-variables)
  - [Database Setup](#database-setup)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Admin Dashboard](#admin-dashboard-usage)

## Features

### User Authentication and Registration

- Users can register accounts with the site.
- Authentication system for secure login.
- Integration with django-allauth for additional authentication features.

### Admin Dashboard

- Utilize django-jazzmin for a stylish and feature-rich admin dashboard.
- Admins can manage car listings, user inquiries, and user accounts.

### Rich Text Content Editing

- Implement django-ckeditor to allow users to create rich text content for car descriptions or blog posts.

### Search Functionality

- Implement advanced search features for cars (e.g., make, model, year, price range).
- Use sqlparse for SQL query parsing and formatting.

### Multiselect Fields

- Utilize django-multiselectfield for allowing multiple selections in fields, such as car features or specifications.

### Debugging and Development Tools

- Use django-debug-toolbar for debugging and profiling during development.

### Image Handling

- Use Pillow for image processing and handling car images.

### OAuth and Social Authentication

- Enable social authentication using python3-openid and oauthlib to allow users to sign in with their social media accounts.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python: [Download here](https://www.python.org/downloads/)
- Django: Install using `pip install django`
- PostgreSQL: [Download here](https://www.postgresql.org/download/)

## Installation

Follow these steps to set up the Car Selling Website on your local machine:

```bash```
# Clone the repository
git clone https://github.com/ripnoob/motverse

# Open terminal & go to project directory
cd motverse

# Create virtual env
python -m venv env
&& source env/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# Databse configuration
Create Database and Configure your own (/prime/settings.py)

# Run project
python manage.py makemigrations &&
python manage.py migrate && python manage.py runserver

 
