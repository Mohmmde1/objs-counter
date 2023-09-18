# Objs Counter

ObjCounter is a web application built using Django that allows users to upload images and perform object detection on them and count the specified object. It uses a pre-trained deep learning model to identify objects within the uploaded images and provides users with information about the objects detected.

Users can select from a list of predefined object classes to specify which objects they want the model to detect. After uploading an image, the application processes it, draws bounding boxes around the detected objects, and displays the results to the user. Additionally, it provides the option to download the processed image with the bounding boxes.

ObjCounter is designed to be a user-friendly tool for object detection, making it accessible for various applications such as image analysis, content moderation, and more. It also serves as an educational resource for those interested in computer vision and deep learning.

The project utilizes popular libraries and tools, including Django, Roboflow, and deep learning frameworks, to achieve its functionality. By following the provided setup instructions, users can easily run the application locally or deploy it to a web server.

ObjCounter is an excellent starting point for developers interested in building and customizing object detection applications or for those seeking an out-of-the-box solution for their object detection needs.

## Table of Contents

- [Objs Counter](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)



## Getting Started



### Prerequisites

Must have  Robolflow Account, python, pipenv

### Installation

Step-by-step instructions on how to install and set up the project:

```bash
# Clone this repository
git clone https://github.com/Mohmmde1/objs-counter.git

# Change directory to your project
cd objs-counter

# Install Pipenv if not already installed
pip install pipenv

# Create a virtual environment with Pipenv
pipenv install

# Activate the virtual environment
pipenv shell

# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the application
python manage.py runserver

# Configure environment variables: Create a `.env` file and add your roboflow API keys.
