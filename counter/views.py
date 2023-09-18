from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404
from counter.models import DetectionResult
from image_handling.models import SubmittedFormData
from utilities.object_detection import perform_object_detection

def count(request, form_id):
    # Retrieve the SubmittedFormData object based on the form_id
    submission = get_object_or_404(SubmittedFormData, pk=form_id)

    # Access the image field from the retrieved object
    uploaded_image = submission.image

    # Perform object detection logic on the uploaded image
    detection_results = perform_object_detection(uploaded_image.path, submission.selected_objects)
    print(submission.selected_objects)
    
    # Create a ContentFile from the image data
    image_data = ContentFile(detection_results["image"], name="prediction.jpg")

    # Create a new DetectionResult instance and associate it with the submission
    detection_result = DetectionResult(submission=submission, detected_objects=detection_results['json'])
    detection_result.image.save("prediction.jpg", image_data)
    
    # Pass the results to the template for rendering
    context = {
        'detection_result': detection_result,
    }

    return render(request, 'count/count.html', context)
