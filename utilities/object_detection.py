from decouple import config
from roboflow import Roboflow
import os
import io
import shutil

# Read the API key from the environment variable
api_key = config('ROBOFLOW_API_KEY')

def perform_object_detection(image_path):
    # Initialize the Roboflow client with the API key
    rf = Roboflow(api_key=api_key)

    # Retrieve the project and model
    project = rf.workspace().project("microsoft-coco")
    model = project.version(9).model
    
    # Perform object detection on the image
    prediction = model.predict(image_path, confidence=40, overlap=30)

    # Save the prediction result as a temporary image
    temp_image_path = os.path.join('media', 'uploads', 'temp_prediction.jpg')
    prediction.save(temp_image_path)

    # Read the temporary image data
    with open(temp_image_path, 'rb') as temp_image_file:
        image_data = temp_image_file.read()

    # Delete the temporary image
    os.remove(temp_image_path)

    return {
        "json": prediction.json(),
        "image": image_data
    }
