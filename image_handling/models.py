from django.db import models

class SubmittedFormData(models.Model):
    image = models.ImageField(upload_to='uploads/')  # Field to store the uploaded image
    selected_objects = models.CharField(max_length=255)  # Field to store selected objects as a comma-separated string

    # Additional fields if needed
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of when the form was submitted

    # def __str__(self):
    #     return f"Form Submission #{self.pk} - {self.timestamp}"
