from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_info = models.CharField(max_length=200)
    medical_condition = models.TextField()
    treatment_notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Supply(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name