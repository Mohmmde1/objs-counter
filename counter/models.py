from django.db import models
from image_handling.models import SubmittedFormData  # Import the model associated with image submissions

class DetectionResult(models.Model):
    submission = models.ForeignKey(SubmittedFormData, on_delete=models.CASCADE)
    detected_objects = models.TextField()
    image = models.ImageField(upload_to='detection_results/')  

    # Additional fields, if needed
    detection_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Detection Result #{self.pk} for Form Submission #{self.submission.pk}"
