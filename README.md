Motoverse -- Car Selling Website

Welcome to the Car Selling Website project! This platform allows users to register, login, make inquiries about cars, and search for available vehicles.

Features:

    User Authentication and Registration:
        Users can register accounts with the site.
        Authentication system for secure login.
        Integration with django-allauth for additional authentication features.

    Admin Dashboard:
        Utilize django-jazzmin for a stylish and feature-rich admin dashboard.
        Admins can manage car listings, user inquiries, and user accounts.

    Rich Text Content Editing:
        Implement django-ckeditor to allow users to create rich text content for car descriptions or blog posts.

    Search Functionality:
        Implement advanced search features for cars (e.g., make, model, year, price range).
        Use sqlparse for SQL query parsing and formatting.

    Multiselect Fields:
        Utilize django-multiselectfield for allowing multiple selections in fields, such as car features or specifications.

    Debugging and Development Tools:
        django-debug-toolbar for debugging and profiling during development.

    Image Handling:
        Use Pillow for image processing and handling car images.


    OAuth and Social Authentication:
        Enable social authentication using python3-openid and oauthlib to allow users to sign in with their social media accounts.

    JWT Authentication:
        Utilize PyJWT for JSON Web Token authentication, adding an additional layer of security.


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

 
