
# Django File Upload Project

This is a simple Django project that allows users to upload files with various types and save them to a MySQL database. The project utilizes Django forms and Bootstrap for CSS styling.

## Features
- Users can upload files, providing their first name, last name, and email.
- Uploaded files are stored in a MySQL database.
- The dashboard displays a list of uploaded files with details such as ID, first name, last name, email, and a link to download the file.

## Requirements
- Python 3.x
- Django 3.x
- MySQL database

## Installation
1. Clone the repository to your local machine.
2. Configure your MySQL database settings in the `settings.py` file.
3. Run migrations using `python manage.py makemigrations` and `python manage.py migrate`.
4. Start the development server with `python manage.py runserver`.

## Usage
1. Access the application in your web browser at `http://localhost:8000/`.
2. Fill out the form and upload your file. Click the "Save" button to submit the form.
3. Uploaded files will be displayed on the dashboard at `http://localhost:8000/dashboard`.
4. The dashboard shows a list of uploaded files with details and download links.

## Author
Gideon Salami

## License
This project is licensed under the [MIT License](LICENSE).


https://github.com/SalamiTech/vidare_proj/assets/92346444/bf85407d-c33e-4a11-acfd-74dd934ed6c1



