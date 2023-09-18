from django.db import models

class SubmittedFormData(models.Model):
    image = models.ImageField(upload_to='uploads/') 
    selected_objects = models.CharField(max_length=255)  

    # Additional fields if needed
    timestamp = models.DateTimeField(auto_now_add=True)  

    # def __str__(self):
    #     return f"Form Submission #{self.pk} - {self.timestamp}"
