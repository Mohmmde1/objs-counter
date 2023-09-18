from decouple import config
from numpy import double
from roboflow import Roboflow
import os
from PIL import Image, ImageDraw

# Read the API key from the environment variable
api_key = config('ROBOFLOW_API_KEY')

# Initialize the Roboflow client with the API key
rf = Roboflow(api_key=api_key)

# Retrieve the project and model
project = rf.workspace().project("microsoft-coco")
model = project.version(9).model


def perform_object_detection(image_path, _class):
    # Perform object detection on the image
    prediction = model.predict(image_path, confidence=10, overlap=30)

    # Filter the predictions to include only the specified _class
    filtered_predictions = [
        p for p in prediction.predictions if p['class'] == _class]

    # Create a PIL image from the input image
    input_image = Image.open(image_path)

    # Create a drawing context to draw boxes on the image
    draw = ImageDraw.Draw(input_image)

    # Draw boxes only for the specified _class
    for pred in filtered_predictions:
        x, y, width, height = pred['x'], pred['y'], pred['width'], pred['height']
         # Convert the coordinates to integers
        x, y, width, height = double(x)-100, double(y)-100, double(width), double(height)
        draw.rectangle([x, y, x + width, y + height], outline='red', width=3)

    # Save the modified image as a temporary image
    temp_image_path = os.path.join('media', 'uploads', 'temp_prediction.jpg')
    input_image.save(temp_image_path)

    # Read the temporary image data
    with open(temp_image_path, 'rb') as temp_image_file:
        image_data = temp_image_file.read()

    # Delete the temporary image
    os.remove(temp_image_path)

    return {
        "json": {"predictions": filtered_predictions},
        "image": image_data
    }
