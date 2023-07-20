from django.db import models

# Create your mode is here.
class StudentForm (models.Model):
    firstname = models.CharField("Enter first name", max_length=50)
    lastname = models.CharField("Enter last name", max_length = 50)
    email = models.EmailField("Enter Email")
    file = models.FileField() # Creating file input

    class Meta:
        db_table = "student"

        