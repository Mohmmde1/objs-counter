from django.db import models

# from image_handling.models import UploadedImage

# class DetectedObject(models.Model):
#     uploaded_image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
#     class_name = models.CharField(max_length=255)
#     confidence = models.FloatField()
#     selected_objects = models.JSONField()  # Store selected objects as a JSON array

#     def __str__(self):
#         return f"{self.class_name} (Confidence: {self.confidence})"
